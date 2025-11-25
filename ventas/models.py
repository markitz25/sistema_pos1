from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from inventario.models import Producto
from clientes.models import Cliente
from decimal import Decimal

class Venta(models.Model):
    """
    Modelo para registrar las ventas realizadas
    """
    # Relaciones
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.PROTECT,
        related_name='ventas',
        verbose_name='Cliente'
    )
    
    usuario = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='ventas_realizadas',
        verbose_name='Usuario que realizó la venta'
    )
    
    # Información de la venta
    fecha = models.DateTimeField(
        default=timezone.now,
        verbose_name='Fecha de Venta'
    )
    
    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        verbose_name='Subtotal'
    )
    
    impuesto = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        verbose_name='Impuesto (IVA)',
        help_text='Impuesto calculado sobre el subtotal'
    )
    
    descuento = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        verbose_name='Descuento',
        help_text='Descuento aplicado a la venta'
    )
    
    total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        verbose_name='Total'
    )
    
    # Método de pago
    METODOS_PAGO = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
        ('mixto', 'Mixto'),
    ]
    
    metodo_pago = models.CharField(
        max_length=20,
        choices=METODOS_PAGO,
        default='efectivo',
        verbose_name='Método de Pago'
    )
    
    # Estado de la venta
    ESTADOS = [
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
        ('pendiente', 'Pendiente'),
    ]
    
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='completada',
        verbose_name='Estado'
    )
    
    # Notas adicionales
    notas = models.TextField(
        blank=True,
        verbose_name='Notas',
        help_text='Observaciones sobre la venta'
    )
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['-fecha']
        indexes = [
            models.Index(fields=['-fecha']),
            models.Index(fields=['cliente']),
            models.Index(fields=['usuario']),
        ]
    
    def __str__(self):
        return f"Venta #{self.id} - {self.cliente.nombre} - ${self.total}"
    
    def calcular_totales(self):
        """
        Calcula los totales de la venta basándose en los detalles
        """
        detalles = self.detalles.all()
        
        # Calcular subtotal
        self.subtotal = sum(detalle.subtotal for detalle in detalles)
        
        # Calcular impuesto (19% en Colombia, ajusta según tu país)
        self.impuesto = self.subtotal * Decimal('0.19')
        
        # Calcular total
        self.total = self.subtotal + self.impuesto - self.descuento
        
        self.save()
    
    def get_numero_productos(self):
        """Retorna el número total de productos en la venta"""
        return sum(detalle.cantidad for detalle in self.detalles.all())
    
    def cancelar_venta(self):
        """
        Cancela la venta y restaura el inventario
        """
        if self.estado == 'completada':
            # Restaurar inventario
            for detalle in self.detalles.all():
                producto = detalle.producto
                producto.stock += detalle.cantidad
                producto.save()
            
            # Actualizar estado
            self.estado = 'cancelada'
            self.save()
            
            # Actualizar datos del cliente
            self.cliente.total_compras -= self.total
            self.cliente.save()
            
            return True
        return False


class DetalleVenta(models.Model):
    """
    Modelo para los detalles de cada venta (productos vendidos)
    """
    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        related_name='detalles',
        verbose_name='Venta'
    )
    
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='ventas_detalle',
        verbose_name='Producto'
    )
    
    cantidad = models.IntegerField(
        default=1,
        verbose_name='Cantidad'
    )
    
    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio Unitario',
        help_text='Precio del producto al momento de la venta'
    )
    
    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Subtotal'
    )
    
    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'
        ordering = ['id']
    
    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"
    
    def save(self, *args, **kwargs):
        """
        Calcula el subtotal automáticamente antes de guardar
        """
        self.subtotal = self.precio_unitario * self.cantidad
        super().save(*args, **kwargs)
    
    def actualizar_inventario(self):
        """
        Reduce el stock del producto
        """
        self.producto.stock -= self.cantidad
        self.producto.save()