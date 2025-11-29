# trabajadores/models.py
from django.db import models
from django.contrib.auth.models import User

class Trabajador(models.Model):
    ROLES = [
        ('admin', 'Administrador'),
        ('trabajador', 'Trabajador'),
    ]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES, default='trabajador')
    # Campos agregados
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    activo = models.BooleanField(default=True)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, 
                                   related_name='trabajadores_creados', blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario.username} - {self.get_rol_display()}"