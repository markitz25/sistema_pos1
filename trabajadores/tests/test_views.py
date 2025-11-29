import pytest
from django.urls import reverse

from tests.factories import AdminUserFactory, TrabajadorFactory, UserFactory
from trabajadores.models import Trabajador


@pytest.mark.django_db
def test_listar_trabajadores_restringe_no_admin(client):
    user = UserFactory()
    Trabajador.objects.create(
        usuario=user, rol="trabajador", nombre="NoAdmin", apellido="User"
    )
    client.force_login(user)
    resp = client.get(reverse("trabajadores:listar"))
    assert resp.status_code == 302  # redirige sin permisos


@pytest.mark.django_db
def test_listar_trabajadores_admin(client):
    admin = AdminUserFactory()
    client.force_login(admin)
    resp = client.get(reverse("trabajadores:listar"))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_toggle_estado_trabajador(client):
    admin = AdminUserFactory()
    client.force_login(admin)
    otro = TrabajadorFactory()

    resp = client.get(reverse("trabajadores:toggle_estado", args=[otro.id]))
    assert resp.status_code == 302
    otro.refresh_from_db()
    assert otro.activo is False
    assert otro.usuario.is_active is False
