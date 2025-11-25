"""
URLs para el módulo de ventas
"""
from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    # Punto de venta
    path('', views.punto_venta, name='punto_venta'),
    path('punto-venta/', views.punto_venta, name='nueva_venta'),
    
    # Búsqueda AJAX
    path('buscar-productos/', views.buscar_productos_ajax, name='buscar_productos_ajax'),
    path('api/buscar-productos/', views.buscar_productos_ajax, name='buscar_productos'),
    
    # Gestión de ventas
    path('listar/', views.listar_ventas, name='listar'),
    path('historial/', views.listar_ventas, name='historial'),
    path('detalle/<int:venta_id>/', views.detalle_venta, name='detalle'),
    path('cancelar/<int:venta_id>/', views.cancelar_venta, name='cancelar'),
]