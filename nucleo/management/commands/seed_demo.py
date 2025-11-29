from datetime import timedelta
import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal
from django.db import transaction

from inventario.models import Categoria, Producto
from clientes.models import Cliente
from ventas.models import Venta, DetalleVenta
from trabajadores.models import Trabajador


class Command(BaseCommand):
    help = "Carga datos de demo (categorías, productos, clientes, ventas) para probar reportes."

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING("Cargando datos de demo..."))
            self._crear_usuarios_demo()
            categorias = self._crear_categorias()
            productos = self._crear_productos(categorias)
            clientes = self._crear_clientes()
            self._crear_ventas(productos, clientes)
            self.stdout.write(self.style.SUCCESS("Datos de demo cargados correctamente."))

    def _crear_usuarios_demo(self):
        admin_user, _ = User.objects.get_or_create(
            username="demo_admin",
            defaults={"email": "demo_admin@sipos.com", "is_staff": True, "is_superuser": True},
        )
        if not admin_user.password:
            admin_user.set_password("demo1234")
            admin_user.save()
        Trabajador.objects.get_or_create(
            usuario=admin_user, defaults={"nombre": "Demo", "apellido": "Admin", "rol": "admin", "activo": True}
        )

        worker_user, _ = User.objects.get_or_create(
            username="demo_worker",
            defaults={"email": "demo_worker@sipos.com", "is_staff": False, "is_superuser": False},
        )
        if not worker_user.password:
            worker_user.set_password("demo1234")
            worker_user.save()
        Trabajador.objects.get_or_create(
            usuario=worker_user, defaults={"nombre": "Demo", "apellido": "Trabajador", "rol": "trabajador", "activo": True}
        )

    def _crear_categorias(self):
        nombres = ["Alimentos", "Bebidas", "Papelería", "Electrónica", "Limpieza"]
        cats = {}
        for nombre in nombres:
            cat, _ = Categoria.objects.get_or_create(nombre=nombre, defaults={"descripcion": f"Categoría {nombre}"})
            cats[nombre] = cat
        return cats

    def _crear_productos(self, cats):
        catalogo = [
            ("Arroz Diana 500g", "Alimentos", Decimal("3500")),
            ("Pasta Doria 500g", "Alimentos", Decimal("4200")),
            ("Bolígrafos BIC x10", "Papelería", Decimal("10000")),
            ("Coca-Cola 2L", "Bebidas", Decimal("8500")),
            ("Agua Manantial 600ml", "Bebidas", Decimal("2000")),
            ("Resma Papel A4", "Papelería", Decimal("18000")),
            ("Sal Refisal 500g", "Alimentos", Decimal("1500")),
            ("Aceite Girasol 1L", "Alimentos", Decimal("12000")),
            ("Cloro Clorox 1L", "Limpieza", Decimal("6500")),
            ("Jugo Hit Naranja 1L", "Bebidas", Decimal("5500")),
        ]
        productos = []
        for nombre, cat, precio in catalogo:
            p, _ = Producto.objects.get_or_create(
                nombre=nombre,
                defaults={
                    "categoria": cats.get(cat),
                    "precio": precio,
                    "precio_venta": precio,
                    "stock": 100,
                    "stock_minimo": 5,
                    "descripcion": f"Producto de demo: {nombre}",
                },
            )
            productos.append(p)
        return productos

    def _crear_clientes(self):
        data = [
            ("Cliente Casual", "CASUAL", "0000000000", None),
            ("Pedro Gómez", "5566778899", "3005566778", "pedro@sipos.com"),
            ("Ana Martínez", "5544332211", "3005544332", "ana@sipos.com"),
            ("Luis Rodríguez", "6677889900", "3006677889", "luis@sipos.com"),
            ("Carlos López", "1122334455", "3001122334", "carlos@sipos.com"),
            ("Juan Pérez", "9988776655", "3009988776", "juan@sipos.com"),
        ]
        clientes = []
        for nombre, cedula, tel, correo in data:
            cliente, _ = Cliente.objects.get_or_create(
                cedula=cedula,
                defaults={
                    "nombre": nombre,
                    "telefono": tel,
                    "correo": correo,
                    "direccion": "Demo dirección",
                    "activo": True,
                },
            )
            clientes.append(cliente)
        return clientes

    def _crear_ventas(self, productos, clientes):
        metodos = ["efectivo", "tarjeta", "transferencia", "mixto"]
        ventas_creadas = 0
        cliente_casual = next((c for c in clientes if c.cedula == "CASUAL"), None)
        # limpiar ventas existentes de demo? no, solo añadir
        for i in range(12):
            cliente = random.choice(clientes)
            productos_seleccionados = random.sample(productos, k=random.randint(2, 4))
            detalles = []
            subtotal = Decimal("0")
            for prod in productos_seleccionados:
                cantidad = random.randint(1, 4)
                precio = prod.precio
                subtotal += precio * cantidad
                detalles.append((prod, cantidad, precio))
                # ajustar stock
                prod.stock = max(0, prod.stock - cantidad)
                prod.save()
            impuesto = subtotal * Decimal("0.19")
            total = subtotal + impuesto
            metodo = random.choice(metodos)
            venta = Venta.objects.create(
                cliente=cliente if cliente.cedula != "CASUAL" else cliente_casual,
                usuario=User.objects.filter(username="demo_admin").first() or User.objects.first(),
                subtotal=subtotal,
                impuesto=impuesto,
                descuento=Decimal("0"),
                total=total,
                metodo_pago=metodo,
                estado="completada",
                fecha=timezone.now() - timedelta(days=random.randint(0, 20)),
                notas=f"Venta demo {i+1}",
            )
            for prod, cantidad, precio in detalles:
                DetalleVenta.objects.create(
                    venta=venta,
                    producto=prod,
                    cantidad=cantidad,
                    precio_unitario=precio,
                    subtotal=precio * cantidad,
                )
            # actualizar cliente
            if venta.cliente:
                venta.cliente.total_compras = (venta.cliente.total_compras or Decimal("0")) + total
                venta.cliente.ultima_compra = venta.fecha
                venta.cliente.save()
            ventas_creadas += 1

        self.stdout.write(self.style.SUCCESS(f"Ventas de demo creadas: {ventas_creadas}"))
