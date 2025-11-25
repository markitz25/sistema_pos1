"""
Views para autenticación
Sistema de login con redirección inteligente según rol
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):
    """
    Vista de login con redirección inteligente
    - Admin → dashboard_admin
    - Trabajador → dashboard_trabajador
    """
    
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


@login_required
def logout_view(request):
    """Vista de logout"""
    username = request.user.username
    logout(request)
    messages.success(request, f'👋 Hasta pronto, {username}')
    return redirect('autenticacion:login')