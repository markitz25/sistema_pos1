from django.urls import path
from . import views

app_name = 'trabajadores'

urlpatterns = [
    path('', views.listar_trabajadores, name='listar'),
    path('lista/', views.listar_trabajadores, name='lista'),
    path('crear/', views.crear_trabajador, name='crear'),
    path('editar/<int:trabajador_id>/', views.editar_trabajador, name='editar'),
    path('eliminar/<int:trabajador_id>/', views.eliminar_trabajador, name='eliminar'),
    path('detalle/<int:trabajador_id>/', views.detalle_trabajador, name='detalle'),
    
    # Toggle estado - CORREGIDO
    path('toggle/<int:trabajador_id>/', views.toggle_estado_trabajador, name='toggle_estado'),
    
    path('perfil/', views.mi_perfil, name='mi_perfil'),
    path('cambiar-contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
]