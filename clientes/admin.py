from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cedula', 'telefono', 'total_compras', 'activo', 'fecha_registro']
    list_filter = ['activo', 'fecha_registro']
    search_fields = ['nombre', 'cedula', 'telefono', 'correo']
    readonly_fields = ['fecha_registro', 'ultima_compra', 'total_compras']
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'cedula')
        }),
        ('Contacto', {
            'fields': ('telefono', 'correo', 'direccion')
        }),
        ('Estadísticas', {
            'fields': ('total_compras', 'ultima_compra', 'fecha_registro')
        }),
        ('Estado', {
            'fields': ('activo', 'notas')
        }),
    )