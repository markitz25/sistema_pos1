import factory
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.utils import timezone

from clientes.models import Cliente
from inventario.models import Categoria, Producto
from ventas.models import Venta, DetalleVenta
from trabajadores.models import Trabajador

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    username = factory.Sequence(lambda n: f"user{n}")
    password = factory.PostGenerationMethodCall("set_password", "12345")
    is_staff = True
    is_superuser = False
    email = factory.Sequence(lambda n: f"user{n}@example.com")

    @factory.post_generation
    def ensure_saved(self, create, extracted, **kwargs):
        if create:
            self.save()


class AdminUserFactory(UserFactory):
    is_superuser = True

    @factory.post_generation
    def crear_trabajador(self, create, extracted, **kwargs):
        # Crea el perfil de trabajador con rol admin para pasar los decoradores de reportes
        if not create:
            return
        Trabajador.objects.create(
            usuario=self,
            rol="admin",
            nombre=self.username,
            apellido="Admin",
        )


class TrabajadorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Trabajador

    usuario = factory.SubFactory(UserFactory)
    rol = "trabajador"
    nombre = factory.Sequence(lambda n: f"Trab{n}")
    apellido = "Prueba"
    activo = True


class CategoriaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categoria

    nombre = factory.Sequence(lambda n: f"Categoria {n}")
    descripcion = "Categoria de prueba"


class ProductoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Producto

    nombre = factory.Sequence(lambda n: f"Producto {n}")
    categoria = factory.SubFactory(CategoriaFactory)
    codigo_barras = factory.Sequence(lambda n: f"COD{n:05d}")
    precio = Decimal("10.00")
    precio_venta = Decimal("12.00")
    stock = 20
    stock_minimo = 5
    descripcion = "Producto de prueba"


class ClienteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cliente

    nombre = factory.Sequence(lambda n: f"Cliente {n}")
    cedula = factory.Sequence(lambda n: f"C{n:05d}")
    correo = factory.Sequence(lambda n: f"cliente{n}@example.com")
    telefono = "123456789"
    direccion = "Calle Falsa 123"
    activo = True
    total_compras = Decimal("0.00")


class VentaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Venta

    cliente = factory.SubFactory(ClienteFactory)
    usuario = factory.SubFactory(AdminUserFactory)
    fecha = factory.LazyFunction(timezone.now)
    subtotal = Decimal("0.00")
    impuesto = Decimal("0.00")
    descuento = Decimal("0.00")
    total = Decimal("0.00")
    metodo_pago = "efectivo"
    estado = "completada"
    notas = ""


class DetalleVentaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DetalleVenta

    venta = factory.SubFactory(VentaFactory)
    producto = factory.SubFactory(ProductoFactory)
    cantidad = 2
    precio_unitario = factory.LazyAttribute(lambda o: o.producto.precio_venta)
    subtotal = factory.LazyAttribute(lambda o: o.precio_unitario * o.cantidad)
