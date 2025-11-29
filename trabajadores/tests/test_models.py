import pytest

from trabajadores.models import Trabajador
from tests.factories import AdminUserFactory, TrabajadorFactory, UserFactory


@pytest.mark.django_db
def test_trabajador_admin_rol():
    user = AdminUserFactory()
    assert user.trabajador.rol == "admin"


@pytest.mark.django_db
def test_trabajador_creado_para_usuario():
    user = UserFactory()
    trabajador = Trabajador.objects.create(
        usuario=user,
        rol="trabajador",
        nombre="Nombre",
        apellido="Apellido",
    )
    assert trabajador.usuario.username == user.username


@pytest.mark.django_db
def test_trabajador_factory_activo():
    trabajador = TrabajadorFactory()
    assert trabajador.activo is True
