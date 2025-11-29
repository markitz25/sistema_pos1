from decimal import Decimal

import pytest

from tests.factories import ClienteFactory


@pytest.mark.django_db
def test_actualizar_total_compras():
    cliente = ClienteFactory()
    cliente.actualizar_total_compras(Decimal("100.00"))
    cliente.refresh_from_db()
    assert cliente.total_compras == Decimal("100.00")
    assert cliente.ultima_compra is not None


@pytest.mark.django_db
def test_cliente_frecuente():
    cliente = ClienteFactory()
    cliente.actualizar_total_compras(Decimal("10.00"))
    assert cliente.es_cliente_frecuente() is False
    # Simula 5 compras
    cliente.ventas.set([])  # asegura relación inicial
    assert cliente.get_numero_compras() == 0
