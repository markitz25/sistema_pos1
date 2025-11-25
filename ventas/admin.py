from django.contrib import admin
from .models import Venta, DetalleVenta

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 0

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'usuario', 'fecha', 'total', 'metodo_pago', 'estado']
    list_filter = ['estado', 'metodo_pago', 'fecha']
    search_fields = ['cliente__nombre', 'id']
    inlines = [DetalleVentaInline]
    readonly_fields = ['subtotal', 'impuesto', 'total']

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal']
    list_filter = ['venta__fecha']