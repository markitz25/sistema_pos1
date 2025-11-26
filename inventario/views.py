"""
Views para el módulo de inventario
Gestiona productos y categorías
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.db import models

from .models import Producto, Categoria


# ==================== FUNCIÓN HELPER ====================

def es_admin(user):
    """Verifica si el usuario es administrador"""
    try:
        return user.trabajador.rol == 'admin'
    except:
        return False


# ==================== GESTIÓN DE PRODUCTOS ====================

@login_required
def lista_productos(request):
    """Lista de productos con búsqueda y filtros"""
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')
    
    productos = Producto.objects.all().select_related('categoria')
    
    # Búsqueda
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | 
            Q(descripcion__icontains=query)
        )
    
    # Filtro por categoría
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    
    # Ordenar por nombre
    productos = productos.order_by('nombre')
    
    # Obtener categorías para el filtro
    categorias = Categoria.objects.all().order_by('nombre')
    
    context = {
        'productos': productos,
        'categorias': categorias,
        'query': query,
        'categoria_seleccionada': categoria_id,
        'es_admin': es_admin(request.user),  # AGREGAR ESTA LÍNEA
    }
    
    return render(request, 'inventario/lista_productos.html', context)


@login_required
def agregar_producto(request):
    """Agregar nuevo producto"""
    # Verificar permisos
    if not es_admin(request.user):
        messages.error(request, '❌ Solo los administradores pueden realizar esta acción')
        return redirect('inventario:lista_productos')
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        stock_minimo = request.POST.get('stock_minimo', 5)
        categoria_id = request.POST.get('categoria')
        imagen = request.FILES.get('imagen')
        
        try:
            producto = Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                stock=stock,
                stock_minimo=stock_minimo,
                categoria_id=categoria_id if categoria_id else None,
                imagen=imagen
            )
            messages.success(request, f'✅ Producto "{nombre}" agregado exitosamente')
            return redirect('inventario:lista_productos')
            
        except Exception as e:
            messages.error(request, f'❌ Error al agregar producto: {str(e)}')
    
    # Obtener categorías para el formulario
    categorias = Categoria.objects.all().order_by('nombre')
    
    context = {
        'categorias': categorias
    }
    
    return render(request, 'inventario/agregar_producto.html', context)


@login_required
def editar_producto(request, producto_id):
    """Editar producto existente"""
    # Verificar permisos
    if not es_admin(request.user):
        messages.error(request, '❌ Solo los administradores pueden realizar esta acción')
        return redirect('inventario:lista_productos')
    
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion', '')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.stock_minimo = request.POST.get('stock_minimo', 5)
        
        categoria_id = request.POST.get('categoria')
        if categoria_id:
            producto.categoria_id = categoria_id
        
        # Solo actualizar imagen si se sube una nueva
        if request.FILES.get('imagen'):
            producto.imagen = request.FILES.get('imagen')
        
        try:
            producto.save()
            messages.success(request, f'✅ Producto "{producto.nombre}" actualizado exitosamente')
            return redirect('inventario:lista_productos')
            
        except Exception as e:
            messages.error(request, f'❌ Error al actualizar producto: {str(e)}')
    
    categorias = Categoria.objects.all().order_by('nombre')
    
    context = {
        'producto': producto,
        'categorias': categorias
    }
    
    return render(request, 'inventario/editar_producto.html', context)


@login_required
def eliminar_producto(request, producto_id):
    """Eliminar producto"""
    # Verificar permisos
    if not es_admin(request.user):
        messages.error(request, '❌ Solo los administradores pueden realizar esta acción')
        return redirect('inventario:lista_productos')
    
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        nombre = producto.nombre
        try:
            producto.delete()
            messages.success(request, f'✅ Producto "{nombre}" eliminado exitosamente')
        except Exception as e:
            messages.error(request, f'❌ Error al eliminar producto: {str(e)}')
        
        return redirect('inventario:lista_productos')
    
    context = {
        'producto': producto
    }
    
    return render(request, 'inventario/eliminar_producto.html', context)


# ==================== GESTIÓN DE CATEGORÍAS ====================

@login_required
def lista_categorias(request):
    """Lista de categorías"""
    query = request.GET.get('q', '').strip()
    categorias = Categoria.objects.all()
    if query:
        categorias = categorias.filter(nombre__icontains=query)
    categorias = categorias.order_by('nombre')
    
    context = {
        'categorias': categorias,
        'query': query,
        'es_admin': es_admin(request.user),  # Agregar al contexto
    }
    
    return render(request, 'inventario/lista_categorias.html', context)


@login_required
def crear_categoria(request):
    """Crear nueva categoría"""
    # Verificar permisos
    if not es_admin(request.user):
        messages.error(request, '❌ Solo los administradores pueden realizar esta acción')
        return redirect('inventario:lista_categorias')
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        
        try:
            Categoria.objects.create(
                nombre=nombre,
                descripcion=descripcion
            )
            messages.success(request, f'✅ Categoría "{nombre}" creada exitosamente')
            return redirect('inventario:lista_categorias')
            
        except Exception as e:
            messages.error(request, f'❌ Error al crear categoría: {str(e)}')
    
    return render(request, 'inventario/crear_categoria.html')


@login_required
def editar_categoria(request, categoria_id):
    """Editar categoria y mover productos entre categorias (solo admin)"""
    if not es_admin(request.user):
        messages.error(request, 'Solo los administradores pueden realizar esta accion')
        return redirect('inventario:lista_categorias')

    categoria = get_object_or_404(Categoria, id=categoria_id)
    otras_categorias = Categoria.objects.exclude(id=categoria_id).order_by('nombre')
    productos_categoria = categoria.producto_set.select_related('categoria').order_by('nombre')

    if request.method == 'POST':
        if request.POST.get('producto_id') and request.POST.get('nueva_categoria'):
            producto_id = request.POST.get('producto_id')
            nueva_categoria_id = request.POST.get('nueva_categoria')
            try:
                producto = Producto.objects.get(id=producto_id, categoria=categoria)
                producto.categoria_id = nueva_categoria_id
                producto.save()
                messages.success(request, f'Producto "{producto.nombre}" movido de {categoria.nombre} a {producto.categoria.nombre}.')
            except Producto.DoesNotExist:
                messages.error(request, 'Producto no encontrado en esta categoria.')
            return redirect('inventario:editar_categoria', categoria_id=categoria_id)

        categoria.nombre = request.POST.get('nombre')
        categoria.descripcion = request.POST.get('descripcion', '')

        try:
            categoria.save()
            messages.success(request, f'Categoria "{categoria.nombre}" actualizada exitosamente')
            return redirect('inventario:lista_categorias')
        except Exception as e:
            messages.error(request, f'Error al actualizar categoria: {str(e)}')

    context = {
        'categoria': categoria,
        'otras_categorias': otras_categorias,
        'productos_categoria': productos_categoria,
    }

    return render(request, 'inventario/editar_categoria.html', context)

@login_required
def eliminar_categoria(request, categoria_id):
    """Eliminar categoría"""
    # Verificar permisos
    if not es_admin(request.user):
        messages.error(request, '❌ Solo los administradores pueden realizar esta acción')
        return redirect('inventario:lista_categorias')
    
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    if request.method == 'POST':
        # Verificar si tiene productos asociados
        if categoria.producto_set.exists():
            messages.error(
                request, 
                '❌ No se puede eliminar una categoría que tiene productos asignados'
            )
        else:
            nombre = categoria.nombre
            try:
                categoria.delete()
                messages.success(request, f'✅ Categoría "{nombre}" eliminada exitosamente')
            except Exception as e:
                messages.error(request, f'❌ Error al eliminar categoría: {str(e)}')
        
        return redirect('inventario:lista_categorias')
    
    context = {
        'categoria': categoria
    }
    
    return render(request, 'inventario/eliminar_categoria.html', context)


# ==================== VISTAS AJAX ====================

@login_required
def crear_categoria_ajax(request):
    """
    Crear categoría mediante AJAX
    Usado en formularios que tienen un botón de crear categoría rápida
    """
    # Verificar permisos
    if not es_admin(request.user):
        return JsonResponse({
            'success': False,
            'error': '❌ Solo los administradores pueden realizar esta acción'
        })
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        
        if not nombre:
            return JsonResponse({
                'success': False,
                'error': 'El nombre de la categoría es requerido'
            })
        
        try:
            categoria = Categoria.objects.create(
                nombre=nombre,
                descripcion=descripcion
            )
            return JsonResponse({
                'success': True,
                'categoria_id': categoria.id,
                'categoria_nombre': categoria.nombre,
                'message': f'Categoría "{nombre}" creada exitosamente'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'Error al crear categoría: {str(e)}'
            })
    
    return JsonResponse({
        'success': False,
        'error': 'Método no permitido'
    })


@login_required
def buscar_producto_ajax(request):
    """
    Buscar productos mediante AJAX
    Usado en el punto de venta
    """
    query = request.GET.get('q', '')
    
    if len(query) < 2:
        return JsonResponse({'productos': []})
    
    productos = Producto.objects.filter(
        Q(nombre__icontains=query) | 
        Q(descripcion__icontains=query),
        stock__gt=0
    ).select_related('categoria')[:10]
    
    resultados = [{
        'id': p.id,
        'nombre': p.nombre,
        'precio': float(p.precio),
        'stock': p.stock,
        'categoria': p.categoria.nombre if p.categoria else 'Sin categoría',
    } for p in productos]
    
    return JsonResponse({'productos': resultados})


# ==================== DASHBOARD DE INVENTARIO ====================

@login_required
def dashboard_inventario(request):
    """
    Dashboard principal del inventario
    Muestra estadísticas y alertas
    """
    # Productos con stock bajo
    productos_bajo_stock = Producto.objects.filter(
        stock__lte=models.F('stock_minimo')
    ).select_related('categoria')
    
    # Estadísticas generales
    total_productos = Producto.objects.count()
    total_categorias = Categoria.objects.count()
    productos_sin_stock = Producto.objects.filter(stock=0).count()
    
    context = {
        'total_productos': total_productos,
        'total_categorias': total_categorias,
        'productos_sin_stock': productos_sin_stock,
        'productos_bajo_stock': productos_bajo_stock,
        'es_admin': es_admin(request.user),  # Agregar al contexto
    }
    
    return render(request, 'inventario/dashboard.html', context)
