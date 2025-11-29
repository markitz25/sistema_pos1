# inventario/urls.py
from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    # Productos - múltiples nombres para compatibilidad
    path('', views.lista_productos, name='lista_productos'),
    path('listar/', views.lista_productos, name='listar'),  # Alias para templates
    path('productos/', views.lista_productos, name='productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    
    # Categorías
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),
    
    # AJAX endpoints
    path('categoria/crear-ajax/', views.crear_categoria_ajax, name='crear_categoria_ajax'),
]