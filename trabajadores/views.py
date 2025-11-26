from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Trabajador
from django.contrib.auth.models import User

# ==================== FUNCIÓN HELPER ====================

def es_admin(user):
    """Verifica si el usuario es administrador"""
    try:
        return user.trabajador.rol == 'admin'
    except:
        return False

# ==================== GESTIÓN DE TRABAJADORES ====================

@login_required
def listar_trabajadores(request):
    """Lista todos los trabajadores"""
    # Verificar que el usuario es admin
    if not es_admin(request.user):
        messages.error(request, 'No tienes permisos para ver esta página')
        return redirect('tablero:dashboard')
    
    trabajadores = Trabajador.objects.all()
    context = {
        'trabajadores': trabajadores
    }
    return render(request, 'trabajadores/listar.html', context)

@login_required
def crear_trabajador(request):
    """Crear nuevo trabajador"""
    if request.method == 'POST':
        # Lógica para crear trabajador
        pass
    return render(request, 'trabajadores/crear.html')

@login_required
def editar_trabajador(request, trabajador_id):
    """Editar trabajador existente"""
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    if request.method == 'POST':
        # Lógica para editar
        pass
    context = {'trabajador': trabajador}
    return render(request, 'trabajadores/editar.html', context)

@login_required
def eliminar_trabajador(request, trabajador_id):
    """Eliminar trabajador"""
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    if request.method == 'POST':
        trabajador.delete()
        messages.success(request, 'Trabajador eliminado exitosamente')
        return redirect('trabajadores:listar')
    context = {'trabajador': trabajador}
    return render(request, 'trabajadores/confirmar_eliminar.html', context)

@login_required
def detalle_trabajador(request, trabajador_id):
    """Ver detalle de trabajador"""
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    context = {'trabajador': trabajador}
    return render(request, 'trabajadores/detalle.html', context)

# ==================== ACTIVAR/DESACTIVAR TRABAJADOR ====================

@login_required
def toggle_estado_trabajador(request, trabajador_id):
    """Activar o desactivar un trabajador"""
    
    # Verificar que el usuario es admin
    try:
        if request.user.trabajador.rol != 'admin':
            messages.error(request, 'No tienes permisos para esta acción')
            return redirect('tablero:dashboard')
    except:
        messages.error(request, 'No tienes permisos')
        return redirect('tablero:dashboard')
    
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    
    # No permitir desactivarse a sí mismo
    if trabajador.usuario == request.user:
        messages.error(request, 'No puedes desactivarte a ti mismo')
        return redirect('trabajadores:listar')
    
    # Toggle estado
    trabajador.activo = not trabajador.activo
    trabajador.save()
    
    # También activar/desactivar el usuario de Django
    trabajador.usuario.is_active = trabajador.activo
    trabajador.usuario.save()
    
    estado = "activado" if trabajador.activo else "desactivado"
    messages.success(request, f'Trabajador {trabajador.nombre} {estado} exitosamente')
    
    return redirect('trabajadores:listar')

# ==================== PERFIL Y CONTRASEÑA ====================

@login_required
def mi_perfil(request):
    """Ver y editar perfil propio"""
    
    try:
        trabajador = request.user.trabajador
    except:
        messages.error(request, 'No tienes un perfil de trabajador')
        return redirect('tablero:dashboard')
    
    if request.method == 'POST':
        telefono = request.POST.get('telefono', '')
        direccion = request.POST.get('direccion', '')
        email = request.POST.get('email', '')
        
        trabajador.telefono = telefono
        trabajador.direccion = direccion
        trabajador.save()
        
        request.user.email = email
        request.user.save()
        
        messages.success(request, 'Perfil actualizado exitosamente')
        return redirect('trabajadores:mi_perfil')
    
    context = {
        'trabajador': trabajador,
    }
    
    return render(request, 'trabajadores/perfil.html', context)


@login_required
def cambiar_contrasena(request):
    """Cambiar contraseña del usuario"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña ha sido actualizada')
            return redirect('trabajadores:mi_perfil')
        else:
            messages.error(request, 'Por favor corrige los errores')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form
    }
    
    return render(request, 'trabajadores/cambiar_contrasena.html', context)