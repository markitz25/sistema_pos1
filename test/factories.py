import factory
from django.contrib.auth import get_user_model
from inventario.models import Producto
from ventas.models import Venta, VentaDetalle

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f"user{n}")
    password = factory.PostGenerationMethodCall("set_password", "12345")
    is_staff = False

class ProductoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Producto
    nombre = factory.Sequence(lambda n: f"Prod{n}")
    precio = 10
    impuesto = 0.16
    stock = 20
    stock_minimo = 5

class VentaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Venta
    cliente = None

class VentaDetalleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = VentaDetalle
    venta = factory.SubFactory(VentaFactory)
    producto = factory.SubFactory(ProductoFactory)
    cantidad = 2
