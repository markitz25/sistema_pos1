import pytest
from django.urls import reverse

from tests.factories import AdminUserFactory, TrabajadorFactory


@pytest.mark.django_db
def test_dashboard_redirect_admin(client):
    admin = AdminUserFactory()
    client.force_login(admin)
    resp = client.get(reverse("tablero:dashboard"))
    assert resp.status_code == 302
    assert resp.url.endswith(reverse("tablero:dashboard_admin"))


@pytest.mark.django_db
def test_dashboard_admin_responde(client):
    admin = AdminUserFactory()
    client.force_login(admin)
    resp = client.get(reverse("tablero:dashboard_admin"))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_dashboard_trabajador_responde(client):
    trabajador = TrabajadorFactory()
    client.force_login(trabajador.usuario)
    resp = client.get(reverse("tablero:dashboard_trabajador"))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_api_ventas_por_mes(client):
    admin = AdminUserFactory()
    client.force_login(admin)
    resp = client.get(reverse("tablero:api_ventas_por_mes"))
    assert resp.status_code == 200
    assert resp.headers["Content-Type"].startswith("application/json")
