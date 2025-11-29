# tablero/urls.py
from django.urls import path
from . import views

app_name = 'tablero'

urlpatterns = [
    path('', views.dashboard_redirect, name='index'),
    path('dashboard/', views.dashboard_redirect, name='dashboard'),
    path('admin/', views.dashboard_admin, name='dashboard_admin'),
    path('trabajador/', views.dashboard_trabajador, name='dashboard_trabajador'),
    
    # APIs para Chart.js
    path('api/ventas-por-mes/', views.api_ventas_por_mes, name='api_ventas_por_mes'),
    path('api/productos-mas-vendidos/', views.api_productos_mas_vendidos, name='api_productos_mas_vendidos'),
    path('api/ventas-por-categoria/', views.api_ventas_por_categoria, name='api_ventas_por_categoria'),
]