"""
Vistas para el módulo de tablero/dashboard
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count, F, Q
from django.utils import timezone
from datetime import timedelta, datetime
from decimal import Decimal

from ventas.models import Venta, DetalleVenta
from inventario.models import Producto
from clientes.models import Cliente


# ==================== REDIRECCIÓN INTELIGENTE ====================

@login_required
def dashboard_redirect(request):
    """Redirige al dashboard apropiado según el rol"""
    try:
        trabajador = request.user.trabajador
        if trabajador.rol == 'admin':
            return redirect('tablero:dashboard_admin')
        else:
            return redirect('tablero:dashboard_trabajador')
    except:
        # Si no tiene trabajador, mostrar dashboard básico
        return dashboard_admin(request)


# ==================== DASHBOARD ADMINISTRADOR ====================

@login_required
def dashboard_admin(request):
    """Dashboard completo para administradores"""
    
    # Fecha actual y rangos
    ahora = timezone.localtime(timezone.now())
    hoy = ahora.date()
    inicio_mes = hoy.replace(day=1)
    inicio_semana = hoy - timedelta(days=hoy.weekday())
    
    # ==================== CORRECCIÓN: VENTAS HOY ====================
    
    # Rango correcto para hoy
    inicio_hoy = timezone.make_aware(datetime.combine(hoy, datetime.min.time()))
    fin_hoy = timezone.make_aware(datetime.combine(hoy, datetime.max.time()))

    ventas_hoy = Venta.objects.filter(
        fecha__gte=inicio_hoy,
        fecha__lte=fin_hoy,
        estado='completada'
    )

    total_ventas_hoy = ventas_hoy.aggregate(
        total=Sum('total')
    )['total'] or Decimal('0')

    cantidad_ventas_hoy = ventas_hoy.count()
    
    # ==================== ESTADÍSTICAS GENERALES ====================
    
    # Ventas del mes
    ventas_mes = Venta.objects.filter(
        fecha__gte=inicio_mes,
        estado='completada'
    )
    
    total_ventas_mes = ventas_mes.aggregate(
        total=Sum('total')
    )['total'] or Decimal('0')
    
    cantidad_ventas_mes = ventas_mes.count()
    
    # Ventas de la semana
    ventas_semana = Venta.objects.filter(
        fecha__gte=inicio_semana,
        estado='completada'
    )
    
    total_ventas_semana = ventas_semana.aggregate(
        total=Sum('total')
    )['total'] or Decimal('0')
    
    # ==================== TRABAJADOR TOP VENDEDOR ====================
    
    # Trabajador con más ventas
    trabajador_top = Venta.objects.filter(
        estado='completada'
    ).values(
        'usuario__username',
        'usuario__first_name',
        'usuario__last_name'
    ).annotate(
        total_ventas=Sum('total'),
        cantidad_ventas=Count('id')
    ).order_by('-total_ventas').first()
    
    # ==================== PRODUCTOS ====================
    
    # Total productos
    total_productos = Producto.objects.count()
    
    # Productos con stock bajo (menos de 10)
    productos_stock_bajo = Producto.objects.filter(stock__lt=10).count()
    
    # Productos más vendidos (top 5)
    productos_mas_vendidos = DetalleVenta.objects.filter(
        venta__estado='completada'
    ).values(
        'producto__nombre'
    ).annotate(
        total_vendido=Sum('cantidad')
    ).order_by('-total_vendido')[:5]
    
    # ==================== CLIENTES ====================
    
    # Total clientes activos
    total_clientes = Cliente.objects.filter(activo=True).count()
    
    # Clientes con más compras (top 5)
    clientes_top = Cliente.objects.filter(
        activo=True
    ).order_by('-total_compras')[:5]
    
    # ==================== VENTAS RECIENTES ====================
    
    ventas_recientes = Venta.objects.select_related(
        'cliente', 'usuario'
    ).prefetch_related(
        'detalles__producto'
    ).order_by('-fecha')[:10]
    
    # ==================== ALERTAS ====================
    
    alertas = []
    
    # Productos con stock crítico
    if productos_stock_bajo > 0:
        alertas.append({
            'tipo': 'warning',
            'icono': 'exclamation-triangle',
            'titulo': 'Stock Bajo',
            'mensaje': f'{productos_stock_bajo} producto(s) con stock menor a 10 unidades'
        })
    
    # Sin ventas hoy
    if cantidad_ventas_hoy == 0:
        alertas.append({
            'tipo': 'info',
            'icono': 'info-circle',
            'titulo': 'Sin Ventas Hoy',
            'mensaje': 'No se han registrado ventas el día de hoy'
        })
    
    context = {
        # Estadísticas
        'total_ventas_mes': total_ventas_mes,
        'cantidad_ventas_mes': cantidad_ventas_mes,
        'total_ventas_semana': total_ventas_semana,
        'total_ventas_hoy': total_ventas_hoy,
        'cantidad_ventas_hoy': cantidad_ventas_hoy,
        
        # Trabajador top
        'trabajador_top': trabajador_top,
        
        # Productos
        'total_productos': total_productos,
        'productos_stock_bajo': productos_stock_bajo,
        'productos_mas_vendidos': productos_mas_vendidos,
        
        # Clientes
        'total_clientes': total_clientes,
        'clientes_top': clientes_top,
        
        # Ventas recientes
        'ventas_recientes': ventas_recientes,
        
        # Alertas
        'alertas': alertas,
        
        # Info del usuario
        'es_admin': True,
    }
    
    return render(request, 'tablero/dashboard_admin.html', context)


# ==================== DASHBOARD TRABAJADOR ====================

@login_required
def dashboard_trabajador(request):
    """Dashboard limitado para trabajadores"""
    
    # Fecha actual y rangos
    hoy = timezone.now().date()
    inicio_mes = hoy.replace(day=1)
    
    # ==================== MIS VENTAS ====================
    
    # Ventas del trabajador este mes
    mis_ventas_mes = Venta.objects.filter(
        usuario=request.user,
        fecha__gte=inicio_mes,
        estado='completada'
    )
    
    total_mis_ventas = mis_ventas_mes.aggregate(
        total=Sum('total')
    )['total'] or Decimal('0')
    
    cantidad_mis_ventas = mis_ventas_mes.count()
    
    # Ventas de hoy
    mis_ventas_hoy = Venta.objects.filter(
        usuario=request.user,
        fecha__date=hoy,
        estado='completada'
    )
    
    total_ventas_hoy = mis_ventas_hoy.aggregate(
        total=Sum('total')
    )['total'] or Decimal('0')
    
    cantidad_ventas_hoy = mis_ventas_hoy.count()
    
    # ==================== VENTAS RECIENTES ====================
    
    mis_ventas_recientes = Venta.objects.filter(
        usuario=request.user
    ).select_related(
        'cliente'
    ).order_by('-fecha')[:10]
    
    # ==================== ESTADÍSTICAS GENERALES ====================
    
    # Total clientes
    total_clientes = Cliente.objects.filter(activo=True).count()
    
    # Total productos disponibles
    total_productos = Producto.objects.filter(stock__gt=0).count()
    
    context = {
        # Mis estadísticas
        'total_mis_ventas': total_mis_ventas,
        'cantidad_mis_ventas': cantidad_mis_ventas,
        'total_ventas_hoy': total_ventas_hoy,
        'cantidad_ventas_hoy': cantidad_ventas_hoy,
        
        # Mis ventas recientes
        'mis_ventas_recientes': mis_ventas_recientes,
        
        # Estadísticas generales
        'total_clientes': total_clientes,
        'total_productos': total_productos,
        
        # Info del usuario
        'es_admin': False,
    }
    
    return render(request, 'tablero/dashboard_trabajador.html', context)


# ==================== APIs PARA GRÁFICOS (Chart.js) ====================

@login_required
def api_ventas_por_mes(request):
    """API: Ventas de los últimos 12 meses"""
    
    # Calcular los últimos 12 meses
    hoy = timezone.now().date()
    meses = []
    totales = []
    
    for i in range(11, -1, -1):
        fecha = hoy - timedelta(days=30*i)
        inicio_mes = fecha.replace(day=1)
        
        if i > 0:
            fin_mes = (inicio_mes + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        else:
            fin_mes = hoy
        
        # Calcular total del mes
        total = Venta.objects.filter(
            fecha__gte=inicio_mes,
            fecha__lte=fin_mes,
            estado='completada'
        ).aggregate(total=Sum('total'))['total'] or 0
        
        meses.append(inicio_mes.strftime('%B'))
        totales.append(float(total))
    
    return JsonResponse({
        'labels': meses,
        'data': totales
    })


@login_required
def api_productos_mas_vendidos(request):
    """API: Top 10 productos más vendidos"""
    
    productos = DetalleVenta.objects.filter(
        venta__estado='completada'
    ).values(
        'producto__nombre'
    ).annotate(
        total=Sum('cantidad')
    ).order_by('-total')[:10]
    
    labels = [p['producto__nombre'] for p in productos]
    data = [p['total'] for p in productos]
    
    return JsonResponse({
        'labels': labels,
        'data': data
    })


@login_required
def api_ventas_por_categoria(request):
    """API: Ventas por categoría de producto"""
    
    categorias = DetalleVenta.objects.filter(
        venta__estado='completada'
    ).values(
        'producto__categoria__nombre'
    ).annotate(
        total=Sum(F('cantidad') * F('precio_unitario'))
    ).order_by('-total')[:5]
    
    labels = [c['producto__categoria__nombre'] or 'Sin categoría' for c in categorias]
    data = [float(c['total']) for c in categorias]
    
    return JsonResponse({
        'labels': labels,
        'data': data
    })