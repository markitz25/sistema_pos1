from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.listar_clientes, name='listar'),
    path('nuevo/', views.crear_cliente, name='crear'),
    path('<int:cliente_id>/', views.detalle_cliente, name='detalle'),
    path('<int:cliente_id>/editar/', views.editar_cliente, name='editar'),
    path('<int:cliente_id>/eliminar/', views.eliminar_cliente, name='eliminar'),
    
    # Toggle estado - AMBOS nombres para compatibilidad
    path('<int:cliente_id>/toggle/', views.toggle_estado_cliente, name='toggle_estado'),
    path('<int:cliente_id>/toggle-estado/', views.toggle_estado_cliente, name='toggle'),
    
    path('buscar-ajax/', views.buscar_cliente_ajax, name='buscar_ajax'),
    path('estadisticas/', views.estadisticas_clientes, name='estadisticas'),
]