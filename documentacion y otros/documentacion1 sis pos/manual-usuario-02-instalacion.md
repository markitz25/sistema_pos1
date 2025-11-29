# Instalación básica del Sistema POS

Guía rápida para un entorno de desarrollo o pruebas. Para producción se requieren pasos extra (BD externa, HTTPS, copias de seguridad, servicio como daemon, etc.).

## Requisitos previos
- Windows o Linux con Python 3 instalado y pip disponible.
- Acceso a internet para instalar dependencias.
- Permiso para crear un entorno virtual.
- Navegador web actualizado.

## Pasos
1. **Obtener el código**
   - Clonar el repo o descomprimir el zip en una carpeta, por ejemplo sistema_pos/.
2. **Crear entorno virtual (recomendado)**
   `ash
   python -m venv .venv
   `
3. **Activar el entorno**
   - Windows (PowerShell): .\.venv\Scripts\activate
   - Linux/macOS: source .venv/bin/activate
4. **Instalar dependencias**
   `ash
   pip install -r requirements.txt
   `
5. **Aplicar migraciones**
   `ash
   python manage.py migrate
   `
6. **Crear usuario administrador**
   `ash
   python manage.py createsuperuser
   `
7. **(Opcional) Cargar datos de ejemplo**
   `ash
   python sembrar_datos.py
   `
8. **Iniciar el servidor de desarrollo**
   `ash
   python manage.py runserver
   `
9. **Acceder desde el navegador**
   - http://localhost:8000/
   - Si no hay sesión iniciada: /login/
   - Si ya está autenticado: /tablero/

## Uso del script instalar.ps1 (Windows)
- Ayuda a validar que estás en la carpeta correcta, instala dependencias y guía parte de la configuración.
- Úsalo en entornos de desarrollo o pruebas. Si PowerShell bloquea scripts, ejecuta Set-ExecutionPolicy -Scope CurrentUser RemoteSigned (con cuidado y según políticas de tu organización).

