import pytest
from django.urls import reverse
from django.utils import timezone
from django.test import override_settings
from django.core import mail

from tests.factories import AdminUserFactory, UserFactory, TrabajadorFactory


@pytest.mark.django_db
def test_login_valido_admin_otp_unico(client):
    user = AdminUserFactory(username="Admin", email="admin@pos.com")
    user.set_password("Admin123456")
    user.save()
    resp = client.post(
        reverse("autenticacion:login"),
        {"username": "Admin", "password": "Admin123456"},
    )
    assert resp.status_code == 302
    assert reverse("autenticacion:otp") in resp.url


@pytest.mark.django_db
def test_login_admin_sin_otp_para_otro_correo(client):
    user = AdminUserFactory(username="Admin", email="otro@pos.com")
    user.set_password("Admin123456")
    user.save()
    resp = client.post(
        reverse("autenticacion:login"),
        {"username": "Admin", "password": "Admin123456"},
        follow=False,
    )
    assert resp.status_code == 302
    assert reverse("tablero:dashboard_admin") in resp.url


@pytest.mark.django_db
def test_otp_codigo_invalido(client):
    user = AdminUserFactory(username="Admin", email="admin@pos.com")
    session = client.session
    session["otp_user_id"] = user.id
    session["otp_code"] = "123456"
    session["otp_expires"] = (timezone.now() + timezone.timedelta(minutes=5)).isoformat()
    session.save()

    resp = client.post(reverse("autenticacion:otp"), {"codigo": "000000"})
    assert resp.status_code == 200
    assert "invalido" in resp.content.decode().lower()


@pytest.mark.django_db
def test_otp_codigo_expirado(client):
    user = AdminUserFactory(username="Admin", email="admin@pos.com")
    session = client.session
    session["otp_user_id"] = user.id
    session["otp_code"] = "123456"
    session["otp_expires"] = (timezone.now() - timezone.timedelta(minutes=1)).isoformat()
    session.save()

    resp = client.get(reverse("autenticacion:otp"))
    assert resp.status_code == 302
    assert reverse("autenticacion:login") in resp.url


@pytest.mark.django_db
def test_login_invalido(client):
    UserFactory()
    resp = client.post(
        reverse("autenticacion:login"),
        {"username": "x", "password": "y"},
    )
    assert resp.status_code == 200
    assert "incorrectos" in resp.content.decode().lower()


@override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
@pytest.mark.django_db
def test_notificacion_login_trabajador(client):
    trabajador = TrabajadorFactory()
    user = trabajador.usuario
    user.set_password("12345")
    user.save()

    resp = client.post(
        reverse("autenticacion:login"),
        {"username": user.username, "password": "12345"},
    )
    assert resp.status_code == 302
    assert reverse("tablero:dashboard_trabajador") in resp.url
    assert len(mail.outbox) == 1
    assert "Inicio de sesion" in mail.outbox[0].subject
