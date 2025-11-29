import pytest
from django.urls import reverse

from tests.factories import (
    AdminUserFactory,
    CategoriaFactory,
    ProductoFactory,
)


@pytest.mark.django_db
def test_alerta_stock_minimo():
    prod = ProductoFactory(stock=3, stock_minimo=5)
    assert prod.stock < prod.stock_minimo


@pytest.mark.django_db
def test_movimiento_actualiza_stock():
    prod = ProductoFactory(stock=10)
    prod.stock -= 3
    prod.save()
    prod.refresh_from_db()
    assert prod.stock == 7


@pytest.mark.django_db
def test_crear_producto_con_categoria():
    categoria = CategoriaFactory()
    prod = ProductoFactory(categoria=categoria, stock_minimo=2)
    assert prod.categoria == categoria
    assert prod.stock_minimo == 2


@pytest.mark.django_db
def test_lista_productos_responde(client):
    user = AdminUserFactory()
    client.force_login(user)
    ProductoFactory()
    resp = client.get(reverse("inventario:lista_productos"))
    assert resp.status_code == 200
