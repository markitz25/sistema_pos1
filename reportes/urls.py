"""
URLs para reportes
"""
from django.urls import path
from . import views

app_name = 'reportes'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('ventas/', views.reporte_ventas, name='reporte_ventas'),
    path('productos/', views.reporte_productos, name='reporte_productos'),
    path('clientes/', views.reporte_clientes, name='reporte_clientes'),
    path('exportar-excel/', views.exportar_excel, name='exportar_excel'),
]