from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    # Listar clientes
    path('', views.listar_clientes, name='listar'),
    
    # CRUD básico
    path('nuevo/', views.crear_cliente, name='crear'),
    path('<int:cliente_id>/', views.detalle_cliente, name='detalle'),
    path('<int:cliente_id>/editar/', views.editar_cliente, name='editar'),
    path('<int:cliente_id>/eliminar/', views.eliminar_cliente, name='eliminar'),
    
    # Activar/Desactivar
    path('<int:cliente_id>/toggle/', views.toggle_estado_cliente, name='toggle_estado'),
    
    # Búsqueda AJAX (para ventas)
    path('buscar-ajax/', views.buscar_cliente_ajax, name='buscar_ajax'),
    
    # Estadísticas - ambas versiones
    path('estadisticas/simple/', views.estadisticas_clientes, name='estadisticas_simple'),
    path('estadisticas/detalladas/', views.estadisticas_clientes_detalladas, name='estadisticas_detalladas'),
    
    # Exportar (funcionalidad futura)
    path('exportar/', views.exportar_clientes, name='exportar'),
    
    # Nueva ruta para estadísticas generales
    path('estadisticas/', views.estadisticas_clientes, name='estadisticas'),
]