from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Sum  # <-- Importación necesaria
from decimal import Decimal      # <-- Importación necesaria
from .models import Cliente
from .forms import ClienteForm, BuscarClienteForm

# ==================== LISTAR CLIENTES - VERSIÓN OPTIMIZADA ====================
@login_required
def listar_clientes(request):
    """
    Lista todos los clientes - VERSIÓN ESTABLE Y FUNCIONAL
    """
    # Obtener clientes con orden por defecto
    clientes = Cliente.objects.all().order_by('-fecha_registro')
    
    # Búsqueda simple por parámetro GET
    query = request.GET.get('q', '')
    if query:
        clientes = clientes.filter(
            Q(nombre__icontains=query) |
            Q(cedula__icontains=query) |
            Q(telefono__icontains=query) |
            Q(correo__icontains=query)
        )
    
    # Filtro por estado
    estado = request.GET.get('estado', '')
    if estado == 'activos':
        clientes = clientes.filter(activo=True)
    elif estado == 'inactivos':
        clientes = clientes.filter(activo=False)
    
    # Estadísticas básicas y SEGURAS
    total_clientes = clientes.count()
    clientes_activos = clientes.filter(activo=True).count()
    
    # Paginación
    paginator = Paginator(clientes, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'clientes': page_obj,
        'total_clientes': total_clientes,
        'clientes_activos': clientes_activos,
        'clientes_frecuentes': 0,  # Valor seguro por ahora
        'query': query,  # Para mostrar en template
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
    total_clientes = Cliente.objects.count()
    clientes_activos = Cliente.objects.filter(activo=True).count()
    
    # Clientes nuevos este mes
    inicio_mes = timezone.now().replace(day=1, hour=0, minute=0, second=0)
    clientes_nuevos_mes = Cliente.objects.filter(
        fecha_registro__gte=inicio_mes
    ).count()
    
    context = {
        'total_clientes': total_clientes,
        'clientes_activos': clientes_activos,
        'clientes_inactivos': total_clientes - clientes_activos,
        'clientes_nuevos_mes': clientes_nuevos_mes,
    }
    
    return render(request, 'clientes/estadisticas.html', context)

# ==================== ESTADÍSTICAS DETALLADAS DE CLIENTES ====================
@login_required
def estadisticas_clientes_detalladas(request):
    """Estadísticas generales de clientes"""
    
    # Total clientes
    total_clientes = Cliente.objects.count()
    clientes_activos = Cliente.objects.filter(activo=True).count()
    
    # Total compras
    total_compras = Cliente.objects.aggregate(
        total=Sum('total_compras')
    )['total'] or Decimal('0')
    
    # Promedio de compra
    if clientes_activos > 0:
        promedio_compra = total_compras / clientes_activos
    else:
        promedio_compra = Decimal('0')
    
    # Top 20 clientes
    top_clientes = Cliente.objects.filter(
        activo=True
    ).order_by('-total_compras')[:20]
    
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