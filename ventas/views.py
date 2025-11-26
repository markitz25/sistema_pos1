"""
Vistas para el módulo de ventas
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db import transaction
from django.db.models import Q, Sum, F
from decimal import Decimal

from .models import Venta, DetalleVenta
from inventario.models import Producto, Categoria
from clientes.models import Cliente


# ==================== FUNCIÓN LEGACY ====================

@login_required
def dashboard(request):
    """Función legacy - redirige a dashboard_redirect"""
    return redirect('tablero:dashboard')


# ==================== PUNTO DE VENTA ====================

@login_required
def punto_venta(request):
    """Vista principal del punto de venta con categorías"""
    
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # Obtener datos del formulario
                cliente_id = request.POST.get('cliente_id')
                productos_ids = request.POST.getlist('producto_id[]')
                cantidades = request.POST.getlist('cantidad[]')
                precios = request.POST.getlist('precio[]')
                descuentos = request.POST.getlist('descuento[]')  # NUEVO: descuento por producto
                metodo_pago = request.POST.get('metodo_pago', 'efectivo')
                
                # Validaciones
                if not productos_ids:
                    messages.error(request, 'Debe agregar al menos un producto')
                    return redirect('ventas:punto_venta')
                
                # Cliente opcional
                cliente = None
                if cliente_id:
                    try:
                        cliente = Cliente.objects.get(id=cliente_id)
                    except Cliente.DoesNotExist:
                        pass
                
                # Calcular totales con descuento por producto
                subtotal = Decimal('0')
                
                # Validar stock y calcular subtotal CON descuento por producto
                for i, producto_id in enumerate(productos_ids):
                    producto = Producto.objects.get(id=producto_id)
                    cantidad = int(cantidades[i])
                    precio_base = Decimal(precios[i])
                    
                    # CORRECCIÓN: Calcular descuento como porcentaje
                    porcentaje_descuento = Decimal(descuentos[i]) if i < len(descuentos) and descuentos[i] else Decimal('0')
                    descuento_producto = precio_base * (porcentaje_descuento / Decimal('100'))
                    precio_con_descuento = precio_base - descuento_producto
                    
                    if producto.stock < cantidad:
                        messages.error(
                            request,
                            f'Stock insuficiente para {producto.nombre}. '
                            f'Disponible: {producto.stock}'
                        )
                        return redirect('ventas:punto_venta')
                    
                    # Calcular subtotal con descuento aplicado por producto
                    subtotal += precio_con_descuento * cantidad
                
                # Calcular IVA sobre el subtotal YA con descuento
                impuesto = subtotal * Decimal('0.19')
                total = subtotal + impuesto
                
                # Crear venta (descuento = 0 porque ya se aplicó por producto)
                venta = Venta.objects.create(
                    cliente=cliente,
                    usuario=request.user,
                    subtotal=subtotal,
                    impuesto=impuesto,
                    descuento=Decimal('0'),  # Ya aplicado por producto
                    total=total,
                    metodo_pago=metodo_pago,
                    estado='completada'
                )
                
                # Crear detalles con precios con descuento
                for i, producto_id in enumerate(productos_ids):
                    producto = Producto.objects.get(id=producto_id)
                    cantidad = int(cantidades[i])
                    precio_base = Decimal(precios[i])
                    
                    # CORRECCIÓN: Calcular descuento como porcentaje
                    porcentaje_descuento = Decimal(descuentos[i]) if i < len(descuentos) and descuentos[i] else Decimal('0')
                    descuento_producto = precio_base * (porcentaje_descuento / Decimal('100'))
                    precio_con_descuento = precio_base - descuento_producto
                    
                    # Crear detalle
                    DetalleVenta.objects.create(
                        venta=venta,
                        producto=producto,
                        cantidad=cantidad,
                        precio_unitario=precio_con_descuento,
                        subtotal=precio_con_descuento * cantidad
                    )
                    
                    # Actualizar stock
                    producto.stock -= cantidad
                    producto.save()
                
                # Actualizar cliente si existe
                if cliente:
                    cliente.total_compras += total
                    cliente.ultima_compra = venta.fecha
                    cliente.save()
                
                messages.success(
                    request,
                    f'✅ Venta #{venta.id} procesada exitosamente. Total: ${total:,.0f}'
                )
                return redirect('ventas:detalle', venta_id=venta.id)
                
        except Producto.DoesNotExist:
            messages.error(request, 'Producto no encontrado')
        except Exception as e:
            messages.error(request, f'Error al procesar la venta: {str(e)}')
        
        return redirect('ventas:punto_venta')
    
    # GET request
    clientes = Cliente.objects.filter(activo=True).order_by('nombre')
    productos = Producto.objects.filter(stock__gt=0).select_related('categoria')
    categorias = Categoria.objects.all().order_by('nombre')
    
    context = {
        'clientes': clientes,
        'productos': productos,
        'categorias': categorias,
    }
    
    return render(request, 'ventas/punto_venta.html', context)


# ==================== BÚSQUEDA AJAX ====================

@login_required
def buscar_productos_ajax(request):
    """API para buscar productos (AJAX)"""
    
    query = request.GET.get('q', '').strip()
    categoria_id = request.GET.get('categoria_id', '')
    
    # Filtrar productos
    productos = Producto.objects.filter(stock__gt=0)
    
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) |
            Q(codigo__icontains=query)
        )
    
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    
    productos = productos.select_related('categoria')[:20]
    
    # Preparar datos
    data = []
    for producto in productos:
        data.append({
            'id': producto.id,
            'nombre': producto.nombre,
            'codigo': producto.codigo,
            'precio': float(producto.precio),
            'stock': producto.stock,
            'categoria': producto.categoria.nombre if producto.categoria else 'Sin categoría',
            'imagen_url': producto.imagen.url if producto.imagen else None,
        })
    
    return JsonResponse({'productos': data})


# ==================== LISTAR VENTAS ====================

@login_required
def listar_ventas(request):
    """Listar ventas según el rol del usuario"""
    
    try:
        trabajador = request.user.trabajador
        es_admin = trabajador.rol == 'admin'
    except:
        es_admin = False
    
    # Filtros
    if es_admin:
        ventas = Venta.objects.all()
    else:
        # Trabajadores solo ven sus propias ventas
        ventas = Venta.objects.filter(usuario=request.user)
    
    # Filtros adicionales
    cliente_id = request.GET.get('cliente')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    estado = request.GET.get('estado')
    
    if cliente_id:
        ventas = ventas.filter(cliente_id=cliente_id)
    
    if fecha_inicio:
        ventas = ventas.filter(fecha__gte=fecha_inicio)
    
    if fecha_fin:
        ventas = ventas.filter(fecha__lte=fecha_fin)
    
    if estado:
        ventas = ventas.filter(estado=estado)
    
    # Ordenar y optimizar consultas
    ventas = ventas.select_related(
        'cliente', 'usuario'
    ).prefetch_related(
        'detalles__producto'
    ).order_by('-fecha')
    
    # Estadísticas
    total_ventas = ventas.filter(estado='completada').aggregate(
        total=Sum('total')
    )['total'] or Decimal('0')
    
    cantidad_ventas = ventas.count()
    
    # Clientes para filtro
    clientes = Cliente.objects.filter(activo=True).order_by('nombre')
    
    context = {
        'ventas': ventas,
        'clientes': clientes,
        'total_ventas': total_ventas,
        'cantidad_ventas': cantidad_ventas,
        'es_admin': es_admin,
        
        # Mantener filtros
        'cliente_id': cliente_id,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'estado': estado,
    }
    
    return render(request, 'ventas/listar.html', context)


# ==================== DETALLE DE VENTA ====================

@login_required
def detalle_venta(request, venta_id):
    """Ver detalle completo de una venta"""
    
    venta = get_object_or_404(
        Venta.objects.select_related('cliente', 'usuario').prefetch_related('detalles__producto'),
        id=venta_id
    )
    
    # Verificar permisos
    try:
        trabajador = request.user.trabajador
        es_admin = trabajador.rol == 'admin'
    except:
        es_admin = False
    
    # Trabajadores solo ven sus propias ventas
    if not es_admin and venta.usuario != request.user:
        messages.error(request, 'No tienes permiso para ver esta venta')
        return redirect('ventas:listar')
    
    context = {
        'venta': venta,
        'es_admin': es_admin,
    }
    
    return render(request, 'ventas/detalle.html', context)


# ==================== CANCELAR VENTA ====================

@login_required
def cancelar_venta(request, venta_id):
    """Cancelar una venta y restaurar stock (solo admin)"""
    
    # Verificar que sea admin
    try:
        trabajador = request.user.trabajador
        if trabajador.rol != 'admin':
            messages.error(request, 'Solo los administradores pueden cancelar ventas')
            return redirect('ventas:listar')
    except:
        messages.error(request, 'No tienes permisos suficientes')
        return redirect('ventas:listar')
    
    venta = get_object_or_404(Venta, id=venta_id)
    
    if venta.estado == 'cancelada':
        messages.warning(request, 'Esta venta ya está cancelada')
        return redirect('ventas:detalle', venta_id=venta_id)
    
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # Restaurar stock de productos
                for detalle in venta.detalles.all():
                    producto = detalle.producto
                    producto.stock += detalle.cantidad
                    producto.save()
                
                # Actualizar cliente si existe
                if venta.cliente:
                    cliente = venta.cliente
                    cliente.total_compras -= venta.total
                    cliente.save()
                
                # Marcar venta como cancelada
                venta.estado = 'cancelada'
                venta.save()
                
                messages.success(request, f'✅ Venta #{venta.id} cancelada y stock restaurado')
                return redirect('ventas:detalle', venta_id=venta_id)
                
        except Exception as e:
            messages.error(request, f'Error al cancelar la venta: {str(e)}')
    
    return redirect('ventas:detalle', venta_id=venta_id)


# ==================== FACTURA/RECIBO ====================

@login_required
def factura_venta(request, venta_id):
    """Generar factura/recibo de una venta"""
    
    venta = get_object_or_404(
        Venta.objects.select_related('cliente', 'usuario').prefetch_related('detalles__producto'),
        id=venta_id
    )
    
    context = {
        'venta': venta,
    }
    
    return render(request, 'ventas/factura.html', context)