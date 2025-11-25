# crear_trabajador1.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_pos.settings')
django.setup()

from django.contrib.auth.models import User
from trabajadores.models import Trabajador

# Verificar si ya existe
if User.objects.filter(username='trabajador1').exists():
    print("⚠️ trabajador1 ya existe")
else:
    # Crear usuario
    user = User.objects.create_user(
        username='trabajador1',
        email='trabajador1@pos.com',
        password='trabajador123',
        first_name='Juan',
        last_name='Pérez'
    )
    
    # Crear trabajador
    Trabajador.objects.create(
        usuario=user,
        rol='trabajador',
        nombre='Juan',
        apellido='Pérez',
        telefono='3001234567',
        activo=True
    )
    
    print("✅ Trabajador creado:")
    print("   Usuario: trabajador1")
    print("   Contraseña: trabajador123")