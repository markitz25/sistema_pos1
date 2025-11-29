import pytest
from django.urls import reverse

from tests.factories import AdminUserFactory, ClienteFactory


@pytest.mark.django_db
def test_listar_clientes_responde(client):
    user = AdminUserFactory()
    client.force_login(user)
    ClienteFactory()
    resp = client.get(reverse("clientes:listar"))
    assert resp.status_code == 200
    assert "clientes" in resp.context


@pytest.mark.django_db
def test_toggle_estado_cliente(client):
    user = AdminUserFactory()
    client.force_login(user)
    cliente = ClienteFactory(activo=True)
    resp = client.get(reverse("clientes:toggle_estado", args=[cliente.id]))
    assert resp.status_code == 302
    cliente.refresh_from_db()
    assert cliente.activo is False
