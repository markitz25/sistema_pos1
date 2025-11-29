from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Trabajador
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import TrabajadorForm

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
    
    trabajadores = Trabajador.objects.select_related('usuario').all()

    busqueda = request.GET.get('busqueda', '').strip()
    rol_filtro = request.GET.get('rol', '')
    estado_filtro = request.GET.get('estado', '')

    if busqueda:
        trabajadores = trabajadores.filter(
            Q(nombre__icontains=busqueda) |
            Q(apellido__icontains=busqueda) |
            Q(usuario__username__icontains=busqueda)
        )
    if rol_filtro in ['admin', 'trabajador']:
        trabajadores = trabajadores.filter(rol=rol_filtro)
    if estado_filtro == 'activo':
        trabajadores = trabajadores.filter(activo=True)
    elif estado_filtro == 'inactivo':
        trabajadores = trabajadores.filter(activo=False)

    trabajadores = trabajadores.order_by('-creado_en')

    paginator = Paginator(trabajadores, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'trabajadores': page_obj,
        'busqueda': busqueda,
        'rol_filtro': rol_filtro,
        'estado_filtro': estado_filtro,
    }
    return render(request, 'trabajadores/listar.html', context)

@login_required
def crear_trabajador(request):
    """Crear nuevo trabajador"""
    if not es_admin(request.user):
        messages.error(request, 'No tienes permisos para esta acci?n')
        return redirect('tablero:dashboard')

    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['nombre']
            last_name = form.cleaned_data['apellido']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            trabajador = form.save(commit=False)
            trabajador.usuario = user
            trabajador.save()

            messages.success(request, 'Trabajador creado correctamente')
            return redirect('trabajadores:listar')
    else:
        form = TrabajadorForm()

    context = {
        'form': form,
        'titulo': 'Crear Trabajador',
        'boton': 'Crear Trabajador',
        'es_nuevo': True,
    }
    return render(request, 'trabajadores/form.html', context)

@login_required
def editar_trabajador(request, trabajador_id):
    """Editar trabajador existente"""
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    if not es_admin(request.user):
        messages.error(request, 'No tienes permisos para esta acción')
        return redirect('trabajadores:listar')

    user_instance = trabajador.usuario

    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador, instance_user=user_instance, is_new=False)
        if form.is_valid():
            user_instance.username = form.cleaned_data['username']
            user_instance.email = form.cleaned_data['email']
            password = form.cleaned_data.get('password')
            password_confirm = form.cleaned_data.get('password_confirm')
            if password:
                if password != password_confirm:
                    messages.error(request, 'Las contraseñas no coinciden')
                    return render(request, 'trabajadores/form.html', {
                        'form': form,
                        'titulo': 'Editar Trabajador',
                        'boton': 'Guardar Cambios',
                        'es_nuevo': False,
                    })
                user_instance.set_password(password)
            user_instance.save()

            form.save()
            messages.success(request, 'Trabajador actualizado correctamente')
            return redirect('trabajadores:listar')
    else:
        form = TrabajadorForm(
            instance=trabajador,
            instance_user=user_instance,
            is_new=False
        )

    context = {
        'form': form,
        'titulo': 'Editar Trabajador',
        'boton': 'Guardar Cambios',
        'es_nuevo': False,
    }
    return render(request, 'trabajadores/form.html', context)

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
    context = {
        'trabajador': trabajador,
        'es_admin': es_admin(request.user),
    }
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

    puede_editar = es_admin(request.user)
    
    if request.method == 'POST':
        if not puede_editar:
            messages.error(request, 'Solo un administrador puede editar este perfil')
            return redirect('trabajadores:mi_perfil')

        nombre = request.POST.get('nombre', '').strip() or trabajador.nombre
        apellido = request.POST.get('apellido', '').strip() or trabajador.apellido
        telefono = request.POST.get('telefono', '')
        direccion = request.POST.get('direccion', '')
        email = request.POST.get('email', '')
        
        trabajador.nombre = nombre
        trabajador.apellido = apellido
        trabajador.telefono = telefono
        trabajador.direccion = direccion
        trabajador.save()
        
        request.user.email = email
        request.user.first_name = nombre
        request.user.last_name = apellido
        request.user.save()
        
        messages.success(request, 'Perfil actualizado exitosamente')
        return redirect('trabajadores:mi_perfil')
    
    context = {
        'trabajador': trabajador,
        'puede_editar': puede_editar,
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
