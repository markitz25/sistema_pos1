from decimal import Decimal

import pytest
from django.urls import reverse

from tests.factories import (
    DetalleVentaFactory,
    ProductoFactory,
    UserFactory,
    VentaFactory,
)


@pytest.mark.django_db
def test_calcular_totales():
    venta = VentaFactory(descuento=Decimal("0.00"))
    producto = ProductoFactory(precio=Decimal("100.00"), precio_venta=Decimal("100.00"))

    DetalleVentaFactory(
        venta=venta,
        producto=producto,
        cantidad=2,
        precio_unitario=Decimal("100.00"),
        subtotal=Decimal("200.00"),
    )

    venta.calcular_totales()

    assert venta.subtotal == Decimal("200.00")
    assert venta.impuesto == Decimal("38.00")  # 19% IVA
    assert venta.total == Decimal("238.00")


@pytest.mark.django_db
def test_venta_rechaza_stock_insuficiente(client):
    usuario = UserFactory()
    client.force_login(usuario)

    producto = ProductoFactory(
        stock=1,
        precio=Decimal("50.00"),
        precio_venta=Decimal("50.00"),
    )

    resp = client.post(
        reverse("ventas:punto_venta"),
        {
            "producto_id[]": [producto.id],
            "cantidad[]": [5],
            "precio[]": ["50.00"],
            "descuento[]": ["0"],
            "metodo_pago": "efectivo",
            "monto_efectivo": "1000",
        },
        follow=True,
    )

    producto.refresh_from_db()
    assert producto.stock == 1  # No debe descontar stock por falta de unidades

    mensajes = list(resp.context["messages"]) if resp.context else []
    assert any("Stock insuficiente" in m.message for m in mensajes)
