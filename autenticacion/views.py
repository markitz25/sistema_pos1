"""
Views para autenticación
Sistema de login con redirección inteligente según rol
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction

from trabajadores.models import Trabajador


def login_view(request):
    """
    Vista de login con redirección inteligente
    - Admin → dashboard_admin
    - Trabajador → dashboard_trabajador
    """
    
    # Si no hay usuarios, mostrar asistente de primer administrador
    if not User.objects.exists():
        return redirect('autenticacion:setup_admin')

    # Si ya está autenticado, redirigir al dashboard apropiado
    if request.user.is_authenticated:
        try:
            trabajador = request.user.trabajador
            if trabajador.rol == 'admin':
                return redirect('tablero:dashboard_admin')
            else:
                return redirect('tablero:dashboard_trabajador')
        except:
            # Si no tiene trabajador, ir al dashboard genérico
            return redirect('tablero:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Autenticar
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Verificar si tiene trabajador y está activo
            try:
                trabajador = user.trabajador
                
                if not trabajador.activo:
                    messages.error(request, '❌ Tu cuenta ha sido desactivada. Contacta al administrador.')
                    return render(request, 'autenticacion/login.html')
                
                # Login exitoso
                login(request, user)
                
                # Redirección según rol
                if trabajador.rol == 'admin':
                    messages.success(request, f'✅ Bienvenido Administrador {trabajador.nombre}')
                    return redirect('tablero:dashboard_admin')
                else:
                    messages.success(request, f'✅ Bienvenido {trabajador.nombre}')
                    return redirect('tablero:dashboard_trabajador')
            
            except:
                # Usuario sin trabajador asociado
                messages.error(request, '❌ Usuario no autorizado en el sistema')
                return render(request, 'autenticacion/login.html')
        else:
            messages.error(request, '❌ Usuario o contraseña incorrectos')
    
    return render(request, 'autenticacion/login.html')


def setup_admin(request):
    """
    Asistente para crear el primer administrador cuando la base esta vacia.
    """
    # Si ya hay usuarios, ir al login normal
    if User.objects.exists():
        return redirect('autenticacion:login')

    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')

        errors = []

        if not full_name:
            errors.append('Ingresa el nombre completo.')
        if not email:
            errors.append('Ingresa el correo electronico.')
        if len(password) < 6:
            errors.append('La contrasena debe tener al menos 6 caracteres.')
        if password != password_confirm:
            errors.append('Las contrasenas no coinciden.')

        first_name = ''
        last_name = ''
        if full_name:
            parts = full_name.split(' ', 1)
            first_name = parts[0]
            if len(parts) > 1:
                last_name = parts[1]

        username_base = email.split('@')[0] if email else 'admin'
        username = username_base
        suffix = 1
        while username and User.objects.filter(username=username).exists():
            suffix += 1
            username = f'{username_base}{suffix}'

        if errors:
            for err in errors:
                messages.error(request, err)
            return render(request, 'autenticacion/setup_admin.html', {
                'full_name': full_name,
                'email': email,
            })

        with transaction.atomic():
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_staff=True,
                is_superuser=True,
            )
            Trabajador.objects.create(
                usuario=user,
                rol='admin',
                nombre=first_name or 'Admin',
                apellido=last_name,
                activo=True,
            )

        login(request, user)
        messages.success(request, 'Administrador creado correctamente.')
        return redirect('tablero:dashboard_admin')

    return render(request, 'autenticacion/setup_admin.html')


@login_required
def logout_view(request):
    """Vista de logout"""
    username = request.user.username
    logout(request)
    messages.success(request, f'👋 Hasta pronto, {username}')
    return redirect('autenticacion:login')
