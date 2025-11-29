import pytest
from django.urls import reverse
from django.utils import timezone

from tests.factories import AdminUserFactory, VentaFactory


@pytest.mark.django_db
def test_reporte_filtrado_por_fecha(client):
    usuario = AdminUserFactory()
    client.force_login(usuario)

    inicio = timezone.now().replace(day=1).isoformat()
    fin = timezone.now().isoformat()

    resp = client.get(
        reverse("reportes:reporte_ventas"),
        {"fecha_inicio": inicio, "fecha_fin": fin},
    )

    assert resp.status_code == 200


@pytest.mark.django_db
def test_exportar_excel(client):
    usuario = AdminUserFactory()
    client.force_login(usuario)
    VentaFactory()

    resp = client.get(reverse("reportes:exportar_excel"))

    assert resp.status_code == 200
    assert resp["Content-Type"].startswith(
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
