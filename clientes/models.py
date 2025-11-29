from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Cliente(models.Model):
    """
    Modelo para gestionar clientes del sistema POS
    """
    # Validador para teléfono (formato colombiano)
    telefono_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="El número de teléfono debe tener entre 9 y 15 dígitos."
    )
    
    # Campos principales
    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre Completo",
        help_text="Nombre completo del cliente"
    )
    
    cedula = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Cédula/DNI",
        help_text="Número de identificación único"
    )
    
    correo = models.EmailField(
        unique=True,
        blank=True,
        null=True,
        verbose_name="Correo Electrónico",
        help_text="Email del cliente (opcional)"
    )
    
    telefono = models.CharField(
        max_length=20,
        validators=[telefono_validator],
        verbose_name="Teléfono",
        help_text="Número de teléfono del cliente"
    )
    
    direccion = models.TextField(
        blank=True,
        verbose_name="Dirección",
        help_text="Dirección física del cliente (opcional)"
    )
    
    # Campos de seguimiento
    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Registro"
    )
    
    ultima_compra = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Última Compra"
    )
    
    total_compras = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        verbose_name="Total en Compras",
        help_text="Monto total acumulado en compras"
    )
    
    activo = models.BooleanField(
        default=True,
        verbose_name="Cliente Activo",
        help_text="Indica si el cliente está activo en el sistema"
    )
    
    # Notas adicionales
    notas = models.TextField(
        blank=True,
        verbose_name="Notas",
        help_text="Observaciones o notas sobre el cliente"
    )
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-fecha_registro']
        indexes = [
            models.Index(fields=['cedula']),
            models.Index(fields=['nombre']),
            models.Index(fields=['-fecha_registro']),
        ]
    
    def __str__(self):
        return f"{self.nombre} - {self.cedula}"
    
    def actualizar_total_compras(self, monto):
        """Actualiza el total de compras del cliente"""
        self.total_compras += monto
        self.ultima_compra = timezone.now()
        self.save()
    
    def get_numero_compras(self):
        """Retorna el número total de compras realizadas"""
        return self.ventas.count()
    
    def get_ultima_compra_fecha(self):
        """Retorna la fecha de la última compra formateada"""
        if self.ultima_compra:
            return self.ultima_compra.strftime('%d/%m/%Y')
        return "Sin compras"
    
    def es_cliente_frecuente(self):
        """Determina si es un cliente frecuente (más de 5 compras)"""
        return self.get_numero_compras() >= 5
    
    def get_promedio_compra(self):
        """Calcula el promedio de compra del cliente"""
        num_compras = self.get_numero_compras()
        if num_compras > 0:
            return self.total_compras / num_compras
        return 0
