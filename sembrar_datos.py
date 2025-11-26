"""
Script para poblar datos de prueba en el Sistema POS.
Ejecutar con: python sembrar_datos.py
"""
import os
import random
from decimal import Decimal
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_pos.settings")
import django  # noqa: E402

django.setup()

from django.contrib.auth.models import User  # noqa: E402
from django.utils import timezone  # noqa: E402

from trabajadores.models import Trabajador  # noqa: E402
from clientes.models import Cliente  # noqa: E402
from inventario.models import Categoria, Producto  # noqa: E402
from ventas.models import Venta, DetalleVenta  # noqa: E402


def ensure_admins(target=3):
    created = 0
    base = [
        ("admin_demo1", "Admin Uno"),
        ("admin_demo2", "Admin Dos"),
        ("admin_demo3", "Admin Tres"),
    ]
    for username, full_name in base[:target]:
        if Trabajador.objects.filter(rol="admin", usuario__username=username).exists():
            continue
        first, last = (full_name.split(" ", 1) + [""])[:2]
        user = User.objects.create_user(
            username=username,
            email=f"{username}@demo.com",
            password="Admin123!",
            first_name=first,
            last_name=last,
            is_staff=True,
            is_superuser=True,
        )
        Trabajador.objects.create(
            usuario=user,
            rol="admin",
            nombre=first,
            apellido=last,
            telefono="3000000000",
            direccion="Oficina central",
            activo=True,
        )
        created += 1
    return created


def ensure_trabajadores(target=10):
    created = 0
    existing = Trabajador.objects.filter(rol="trabajador").count()
    start = existing + 1
    for i in range(start, target + 1):
        username = f"trabajador{i:02d}"
        if Trabajador.objects.filter(usuario__username=username).exists():
            continue
        user = User.objects.create_user(
            username=username,
            email=f"{username}@demo.com",
            password="Trabajador123!",
            first_name=f"Trabajador{i}",
            last_name="Demo",
        )
        Trabajador.objects.create(
            usuario=user,
            rol="trabajador",
            nombre=f"Trabajador{i}",
            apellido="Demo",
            telefono=f"300111{i:04d}",
            direccion="Sucursal principal",
            activo=True,
        )
        created += 1
    return created


def ensure_clientes(target=40):
    created = 0
    current = Cliente.objects.count()
    for i in range(current + 1, target + 1):
        cedula = f"CC{i:05d}"
        if Cliente.objects.filter(cedula=cedula).exists():
            continue
        Cliente.objects.create(
            nombre=f"Cliente {i}",
            cedula=cedula,
            correo=f"cliente{i:02d}@demo.com",
            telefono=f"301{i:07d}"[:12],
            direccion="Calle Demo 123",
            notas="Cliente de prueba",
            activo=True,
        )
        created += 1
    return created


def ensure_categorias_y_productos():
    categorias = [
        "Bebidas",
        "Bebidas Energeticas",
        "Snacks",
        "Limpieza",
        "Tecnologia",
        "Hogar",
        "Abarrotes",
        "Cuidado Personal",
        "Panaderia",
        "Carnes",
        "Lacteos",
        "Frutas y Verduras",
        "Desayuno",
        "Papeleria",
        "Congelados",
    ]
    cat_objs = {}
    for nombre in categorias:
        cat, _ = Categoria.objects.get_or_create(nombre=nombre, defaults={"descripcion": f"Categoria de {nombre}"})
        cat_objs[nombre] = cat

    productos_data = [
        # Bebidas
        ("Agua 600ml", "Bebidas", Decimal("1500"), Decimal("2500"), 120),
        ("Gaseosa 1.5L", "Bebidas", Decimal("4000"), Decimal("5500"), 80),
        ("Jugo de Naranja", "Bebidas", Decimal("3500"), Decimal("4800"), 90),
        ("Cafe Americano 355ml", "Bebidas", Decimal("3200"), Decimal("4800"), 70),
        ("Te Frio Limon 500ml", "Bebidas", Decimal("2800"), Decimal("4200"), 85),
        # Bebidas Energeticas
        ("Energy Max 473ml", "Bebidas Energeticas", Decimal("5200"), Decimal("6800"), 60),
        ("Focus Energy 350ml", "Bebidas Energeticas", Decimal("4800"), Decimal("6400"), 55),
        # Snacks
        ("Papas Fritas", "Snacks", Decimal("2000"), Decimal("3200"), 150),
        ("Chocolate Barra", "Snacks", Decimal("1800"), Decimal("3000"), 130),
        ("Mani Salado 100g", "Snacks", Decimal("2200"), Decimal("3400"), 140),
        ("Mix Frutos Secos 120g", "Snacks", Decimal("4800"), Decimal("6500"), 90),
        # Limpieza
        ("Detergente 1L", "Limpieza", Decimal("5000"), Decimal("7200"), 70),
        ("Cloro 1L", "Limpieza", Decimal("3200"), Decimal("4800"), 65),
        ("Limpiavidrios 500ml", "Limpieza", Decimal("2600"), Decimal("4200"), 80),
        ("Toallas Desinfectantes", "Limpieza", Decimal("6500"), Decimal("8900"), 50),
        # Tecnologia
        ("Mouse Inalambrico", "Tecnologia", Decimal("35000"), Decimal("52000"), 40),
        ("Teclado Mecanico", "Tecnologia", Decimal("120000"), Decimal("165000"), 25),
        ("Funda para Laptop", "Tecnologia", Decimal("25000"), Decimal("39000"), 50),
        ("USB 32GB", "Tecnologia", Decimal("18000"), Decimal("26000"), 90),
        ("Audifonos Bluetooth", "Tecnologia", Decimal("60000"), Decimal("85000"), 35),
        # Hogar
        ("Sarten Antiadherente", "Hogar", Decimal("28000"), Decimal("42000"), 55),
        ("Juego de Vasos", "Hogar", Decimal("15000"), Decimal("26000"), 60),
        ("Almohada Ortopedica", "Hogar", Decimal("38000"), Decimal("52000"), 45),
        ("Cobija Polar", "Hogar", Decimal("32000"), Decimal("46000"), 40),
        # Abarrotes
        ("Arroz 1kg", "Abarrotes", Decimal("3800"), Decimal("5200"), 200),
        ("Aceite 1L", "Abarrotes", Decimal("7200"), Decimal("9200"), 120),
        ("Azucar 1kg", "Abarrotes", Decimal("3600"), Decimal("5200"), 150),
        ("Sal 500g", "Abarrotes", Decimal("1200"), Decimal("2200"), 200),
        ("Pasta Spaghetti 500g", "Abarrotes", Decimal("2800"), Decimal("4200"), 160),
        ("Atun en Agua 170g", "Abarrotes", Decimal("4200"), Decimal("6200"), 140),
        # Cuidado Personal
        ("Shampoo 400ml", "Cuidado Personal", Decimal("12000"), Decimal("16500"), 90),
        ("Jabon de Tocador", "Cuidado Personal", Decimal("1500"), Decimal("2600"), 180),
        ("Crema Dental 100ml", "Cuidado Personal", Decimal("5800"), Decimal("8200"), 120),
        ("Desodorante Roll-on", "Cuidado Personal", Decimal("6500"), Decimal("9200"), 110),
        # Panaderia
        ("Pan Tajado", "Panaderia", Decimal("3500"), Decimal("5200"), 110),
        ("Croissant", "Panaderia", Decimal("2500"), Decimal("3800"), 90),
        ("Baguette", "Panaderia", Decimal("2800"), Decimal("4200"), 95),
        # Carnes
        ("Pechuga de Pollo kg", "Carnes", Decimal("15000"), Decimal("21000"), 85),
        ("Carne de Res kg", "Carnes", Decimal("20000"), Decimal("28000"), 70),
        ("Costillas de Cerdo kg", "Carnes", Decimal("18000"), Decimal("25500"), 65),
        # Lacteos
        ("Leche 1L", "Lacteos", Decimal("4200"), Decimal("5800"), 140),
        ("Queso 500g", "Lacteos", Decimal("13000"), Decimal("18000"), 60),
        ("Yogurt 1L", "Lacteos", Decimal("6200"), Decimal("8600"), 90),
        # Frutas y Verduras
        ("Manzana Roja kg", "Frutas y Verduras", Decimal("5200"), Decimal("7800"), 120),
        ("Banano kg", "Frutas y Verduras", Decimal("3200"), Decimal("5200"), 140),
        ("Tomate Chonto kg", "Frutas y Verduras", Decimal("2800"), Decimal("4600"), 130),
        ("Cebolla Cabezona kg", "Frutas y Verduras", Decimal("2400"), Decimal("4200"), 125),
        ("Papa Pastusa kg", "Frutas y Verduras", Decimal("2500"), Decimal("4200"), 150),
        # Desayuno
        ("Cereal 500g", "Desayuno", Decimal("12000"), Decimal("16500"), 80),
        ("Avena 500g", "Desayuno", Decimal("5200"), Decimal("7600"), 90),
        ("Mermelada 250g", "Desayuno", Decimal("6800"), Decimal("9200"), 70),
        # Papeleria
        ("Cuaderno Argollado", "Papeleria", Decimal("3500"), Decimal("5200"), 180),
        ("Boligrafo Azul Packx3", "Papeleria", Decimal("2800"), Decimal("4600"), 200),
        ("Resma Papel Carta", "Papeleria", Decimal("15000"), Decimal("21000"), 60),
        ("Marcadores Colores x6", "Papeleria", Decimal("5200"), Decimal("7600"), 90),
        # Congelados
        ("Pizza Congelada", "Congelados", Decimal("18000"), Decimal("26000"), 55),
        ("Vegetales Congelados 500g", "Congelados", Decimal("8500"), Decimal("12000"), 70),
        ("Helado Vainilla 1L", "Congelados", Decimal("12000"), Decimal("16500"), 65),
    ]

    def unique_codigo(base_codigo: str, nombre: str) -> str:
        """
        Asegura un codigo de barras unico. Si ya existe el codigo en otro producto,
        agrega sufijos incrementales.
        """
        codigo = base_codigo
        sufijo = 1
        while Producto.objects.filter(codigo_barras=codigo).exclude(nombre=nombre).exists():
            sufijo += 1
            codigo = f"{base_codigo}-{sufijo}"
        return codigo

    prod_created = 0
    for idx, (nombre, cat_name, precio, precio_venta, stock) in enumerate(productos_data, start=1):
        cat = cat_objs[cat_name]
        base_codigo = f"COD{idx:05d}"
        prod = Producto.objects.filter(nombre=nombre).first()

        if prod:
            # Actualizar datos del producto existente
            prod.categoria = cat
            prod.precio = precio
            prod.precio_venta = precio_venta
            prod.codigo_barras = prod.codigo_barras or unique_codigo(base_codigo, nombre)
            if prod.stock < stock:
                prod.stock = stock
            prod.descripcion = prod.descripcion or f"{nombre} de la categoria {cat_name}"
            prod.save()
        else:
            codigo = unique_codigo(base_codigo, nombre)
            prod = Producto.objects.create(
                nombre=nombre,
                categoria=cat,
                precio=precio,
                precio_venta=precio_venta,
                stock=stock,
                stock_minimo=5,
                codigo_barras=codigo,
                descripcion=f"{nombre} de la categoria {cat_name}",
            )
            prod_created += 1

    return len(cat_objs), prod_created


def ensure_ventas(target=30):
    created = 0
    if Venta.objects.count() >= target:
        return created

    productos = list(Producto.objects.all())
    clientes = list(Cliente.objects.all())
    usuarios = list(User.objects.filter(trabajador__activo=True))
    if not productos or not clientes or not usuarios:
        return created

    ventas_a_crear = target - Venta.objects.count()
    for _ in range(ventas_a_crear):
        cliente = random.choice(clientes)
        usuario = random.choice(usuarios)
        fecha = timezone.now() - timedelta(days=random.randint(0, 60))
        venta = Venta.objects.create(
            cliente=cliente,
            usuario=usuario,
            fecha=fecha,
            metodo_pago=random.choice([m[0] for m in Venta.METODOS_PAGO]),
            estado="completada",
            descuento=Decimal("0.00"),
            notas="Venta de demostracion",
        )

        detalles_count = random.randint(2, 4)
        usados = random.sample(productos, k=min(detalles_count, len(productos)))
        for prod in usados:
            cantidad = random.randint(1, 4)
            precio_unitario = prod.precio_venta or prod.precio
            DetalleVenta.objects.create(
                venta=venta,
                producto=prod,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                subtotal=precio_unitario * cantidad,
            )
            # actualizar stock simple
            prod.stock = max(0, prod.stock - cantidad)
            prod.save()

        venta.calcular_totales()
        cliente.actualizar_total_compras(venta.total)
        created += 1
    return created


def main():
    admins = ensure_admins()
    trabajadores = ensure_trabajadores()
    clientes = ensure_clientes()
    categorias, productos = ensure_categorias_y_productos()
    ventas = ensure_ventas()

    print(f"Admins creados: {admins}")
    print(f"Trabajadores creados: {trabajadores}")
    print(f"Clientes creados: {clientes}")
    print(f"Categorias cargadas: {categorias}, productos nuevos: {productos}")
    print(f"Ventas creadas: {ventas}")


if __name__ == "__main__":
    main()
