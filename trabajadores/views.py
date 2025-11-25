from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Trabajador
from django.contrib.auth.models import User

@login_required
def listar_trabajadores(request):
    """Lista todos los trabajadores"""
    # Verificar que el usuario es admin
    if not hasattr(request.user, 'trabajador') or request.user.trabajador.rol != 'admin':
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

@login_required
def cambiar_contrasena(request):
    """Cambiar contraseña del usuario"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantiene la sesión activa
            messages.success(request, 'Tu contraseña ha sido actualizada correctamente.')
            return redirect('trabajadores:detalle', trabajador_id=request.user.trabajador.id)
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = PasswordChangeForm(request.user)

    context = {'form': form}
    return render(request, 'trabajadores/cambiar_contrasena.html', context)