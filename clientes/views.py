from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from django.db.models import Q, Count, Value, Max, Sum, F
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils import timezone
from decimal import Decimal
from .models import Cliente
from .forms import ClienteForm, BuscarClienteForm

# ==================== LISTAR CLIENTES - VERSIÓN OPTIMIZADA ====================
@login_required
def listar_clientes(request):
    """
    Lista todos los clientes - VERSIÓN ESTABLE Y FUNCIONAL
    """
    form_busqueda = BuscarClienteForm(request.GET or None)

    # Base queryset con agregados de compras
    clientes = Cliente.objects.all().annotate(
        num_compras=Count('ventas', filter=Q(ventas__estado='completada'), distinct=True),
        total_gastado=Coalesce(
            Sum('ventas__total', filter=Q(ventas__estado='completada')),
            F('total_compras'),
            Value(0),
            output_field=models.DecimalField(max_digits=12, decimal_places=2)
        )
    )
    
    # Búsqueda
    busqueda = form_busqueda['busqueda'].data if form_busqueda.is_bound else ''
    if busqueda:
        clientes = clientes.filter(
            Q(nombre__icontains=busqueda) |
            Q(cedula__icontains=busqueda) |
            Q(telefono__icontains=busqueda) |
            Q(correo__icontains=busqueda)
        )
    
    # Filtro por estado
    estado = form_busqueda['estado'].data if form_busqueda.is_bound else ''
    if estado == 'activos':
        clientes = clientes.filter(activo=True)
    elif estado == 'inactivos':
        clientes = clientes.filter(activo=False)

    # Orden
    ordenar = form_busqueda['ordenar'].data if form_busqueda.is_bound else ''
    orden_valido = ordenar or '-fecha_registro'
    clientes = clientes.order_by(orden_valido)
    
    # Estadísticas
    total_clientes = clientes.count()
    clientes_activos = clientes.filter(activo=True).count()
    clientes_frecuentes = clientes.filter(num_compras__gte=3).count()
    
    # Paginación
    paginator = Paginator(clientes, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Flag de admin/trabajador
    try:
        es_admin = request.user.trabajador.rol == 'admin'
    except Exception:
        es_admin = False
    
    context = {
        'clientes': page_obj,
        'total_clientes': total_clientes,
        'clientes_activos': clientes_activos,
        'clientes_frecuentes': clientes_frecuentes,
        'query': busqueda,
        'form_busqueda': form_busqueda,
        'es_admin': es_admin,
    }
    
    return render(request, 'clientes/listar.html', context)

# ==================== CREAR CLIENTE ====================
@login_required
def crear_cliente(request):
    """
    Crea un nuevo cliente en el sistema
    """
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            messages.success(request, f'Cliente {cliente.nombre} creado exitosamente.')
            return redirect('clientes:listar')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ClienteForm()
    
    context = {
        'form': form,
        'titulo': 'Nuevo Cliente',
        'boton': 'Crear Cliente'
    }
    
    return render(request, 'clientes/form.html', context)

# ==================== VER DETALLE CLIENTE ====================
@login_required
def detalle_cliente(request, cliente_id):
    """
    Muestra el detalle completo de un cliente
    """
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    
    context = {
        'cliente': cliente,
        'numero_compras': cliente.get_numero_compras(),
        'promedio_compra': cliente.get_promedio_compra(),
    }
    
    return render(request, 'clientes/detalle.html', context)

# ==================== EDITAR CLIENTE ====================
@login_required
def editar_cliente(request, cliente_id):
    """
    Edita los datos de un cliente existente
    """
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    try:
        es_admin = request.user.trabajador.rol == 'admin'
    except Exception:
        es_admin = False
    if cliente.cedula == 'CASUAL' and not es_admin:
        messages.error(request, 'No tienes permisos para modificar el cliente casual.')
        return redirect('clientes:listar')
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cliente {cliente.nombre} actualizado exitosamente.')
            return redirect('clientes:detalle', cliente_id=cliente.id)
    else:
        form = ClienteForm(instance=cliente)
    
    context = {
        'form': form,
        'cliente': cliente,
        'titulo': 'Editar Cliente',
        'boton': 'Actualizar Cliente'
    }
    
    return render(request, 'clientes/form.html', context)

# ==================== ELIMINAR CLIENTE ====================
@login_required
def eliminar_cliente(request, cliente_id):
    """
    Elimina (desactiva) un cliente del sistema
    """
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    try:
        es_admin = request.user.trabajador.rol == 'admin'
    except Exception:
        es_admin = False
    if cliente.cedula == 'CASUAL' and not es_admin:
        messages.error(request, 'No tienes permisos para modificar el cliente casual.')
        return redirect('clientes:listar')
    
    if request.method == 'POST':
        cliente.activo = False
        cliente.save()
        messages.success(request, f'Cliente {cliente.nombre} desactivado exitosamente.')
        return redirect('clientes:listar')
    
    return render(request, 'clientes/eliminar.html', {'cliente': cliente})

# ==================== ACTIVAR/DESACTIVAR CLIENTE ====================
@login_required
def toggle_estado_cliente(request, cliente_id):
    """
    Activa o desactiva un cliente
    """
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    try:
        es_admin = request.user.trabajador.rol == 'admin'
    except Exception:
        es_admin = False
    if cliente.cedula == 'CASUAL' and not es_admin:
        messages.error(request, 'No tienes permisos para modificar el cliente casual.')
        return redirect('clientes:listar')
    cliente.activo = not cliente.activo
    cliente.save()
    
    estado = "activado" if cliente.activo else "desactivado"
    messages.success(request, f'Cliente {cliente.nombre} {estado} exitosamente.')
    
    return redirect('clientes:listar')

# ==================== BÚSQUEDA AJAX ====================
@login_required
def buscar_cliente_ajax(request):
    """
    Busca clientes mediante AJAX
    """
    busqueda = request.GET.get('q', '')
    
    if len(busqueda) < 2:
        return JsonResponse({'clientes': []})
    
    clientes = Cliente.objects.filter(
        Q(nombre__icontains=busqueda) |
        Q(cedula__icontains=busqueda) |
        Q(telefono__icontains=busqueda),
        activo=True
    )[:10]
    
    resultados = [{
        'id': c.id,
        'nombre': c.nombre,
        'cedula': c.cedula,
        'telefono': c.telefono,
        'correo': c.correo or 'Sin correo',
    } for c in clientes]
    
    return JsonResponse({'clientes': resultados})

# ==================== ESTADÍSTICAS DE CLIENTES (SIMPLE) ====================
@login_required
def estadisticas_clientes(request):
    """
    Muestra estadísticas generales de los clientes
    """
    clientes = Cliente.objects.annotate(
        num_compras=Count('ventas', filter=Q(ventas__estado='completada'), distinct=True),
        total_gastado=Coalesce(
            Sum('ventas__total', filter=Q(ventas__estado='completada')),
            F('total_compras'),
            Value(0),
            output_field=models.DecimalField(max_digits=12, decimal_places=2)
        ),
        ultima_compra_fecha=Max('ventas__fecha', filter=Q(ventas__estado='completada'))
    )

    total_clientes = clientes.count()
    clientes_activos = clientes.filter(activo=True).count()
    inicio_mes = timezone.now().replace(day=1, hour=0, minute=0, second=0)
    clientes_nuevos_mes = clientes.filter(fecha_registro__gte=inicio_mes).count()
    total_compras = clientes.aggregate(total=Sum('total_gastado'))['total'] or Decimal('0')
    promedio_compra = total_compras / clientes_activos if clientes_activos else Decimal('0')
    top_clientes = clientes.filter(activo=True).order_by('-total_gastado')[:20]

    context = {
        'total_clientes': total_clientes,
        'clientes_activos': clientes_activos,
        'clientes_inactivos': total_clientes - clientes_activos,
        'clientes_nuevos_mes': clientes_nuevos_mes,
        'total_compras': total_compras,
        'promedio_compra': promedio_compra,
        'top_clientes': top_clientes,
    }
    
    return render(request, 'clientes/estadisticas.html', context)

# ==================== ESTADÍSTICAS DETALLADAS DE CLIENTES ====================
@login_required
def estadisticas_clientes_detalladas(request):
    """Estadísticas generales de clientes"""
    
    # Total clientes
    clientes = Cliente.objects.annotate(
        num_compras=Count('ventas', filter=Q(ventas__estado='completada'), distinct=True),
        total_gastado=Coalesce(
            Sum('ventas__total', filter=Q(ventas__estado='completada')),
            F('total_compras'),
            Value(0),
            output_field=models.DecimalField(max_digits=12, decimal_places=2)
        ),
        ultima_compra=Max('ventas__fecha', filter=Q(ventas__estado='completada'))
    )
    total_clientes = clientes.count()
    clientes_activos = clientes.filter(activo=True).count()
    
    total_compras = clientes.aggregate(total=Sum('total_gastado'))['total'] or Decimal('0')
    promedio_compra = total_compras / clientes_activos if clientes_activos else Decimal('0')
    
    top_clientes = clientes.filter(activo=True).order_by('-total_gastado')[:20]
    
    context = {
        'total_clientes': total_clientes,
        'clientes_activos': clientes_activos,
        'total_compras': total_compras,
        'promedio_compra': promedio_compra,
        'top_clientes': top_clientes,
    }
    
    return render(request, 'clientes/estadisticas.html', context)

# ==================== EXPORTAR CLIENTES ====================
@login_required
def exportar_clientes(request):
    """
    Exporta la lista de clientes
    """
    messages.info(request, 'Funcionalidad de exportación en desarrollo.')
    return redirect('clientes:listar')
