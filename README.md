# Sistema de Punto de Venta (POS)

**Desarrollado por:** Marco Antonio Saavedra y Emanuel
**Versión:** 1.0
**Fecha:** Noviembre 2024

## Descripción

Sistema integral de punto de venta desarrollado con Django para la gestión completa de ventas, inventario, clientes y reportes en establecimientos comerciales.

## Características Principales

- **Punto de Venta Intuitivo:** Interfaz rápida y fácil de usar para procesar ventas
- **Gestión de Inventario:** Control completo de productos, categorías y stock
- **Gestión de Clientes:** Registro y seguimiento de clientes con historial de compras
- **Reportes y Estadísticas:** Dashboard con métricas en tiempo real y gráficos
- **Control de Acceso:** Sistema de roles (Administrador/Trabajador)
- **Exportación de Datos:** Reportes exportables a Excel
- **Múltiples Métodos de Pago:** Efectivo, tarjeta, transferencia y pago mixto

## Tecnologías Utilizadas

- **Backend:** Python 3.8+, Django 4.2.7
- **Frontend:** HTML5, CSS3, Bootstrap, JavaScript
- **Base de Datos:** SQLite (desarrollo), MySQL/PostgreSQL (producción)
- **Librerías:** Pillow, openpyxl, PyMySQL

## Requisitos del Sistema

- Python 3.8 o superior
- Navegador web moderno (Chrome, Firefox, Edge, Safari)
- 2 GB RAM mínimo
- Conexión a red/internet

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/markitz25/sistema_pos1.git
cd sistema_pos1
```

2. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar migraciones:
```bash
python manage.py migrate
```

5. Crear usuario administrador:
```bash
python manage.py createsuperuser
```

O usar el script de datos de prueba:
```bash
python sembrar_datos.py
```

6. Iniciar servidor de desarrollo:
```bash
python manage.py runserver
```

7. Acceder al sistema:
```
http://localhost:8000
```

## Estructura del Proyecto

```
sistema_pos1/
├── sistema_pos/              # Configuración principal del proyecto
├── autenticacion/            # Módulo de autenticación y autorización
├── clientes/                 # Gestión de clientes
├── inventario/               # Gestión de productos y categorías
├── ventas/                   # Punto de venta y gestión de ventas
├── trabajadores/             # Gestión de usuarios del sistema
├── tablero/                  # Dashboard y métricas
├── reportes/                 # Reportes y estadísticas
├── nucleo/                   # Configuración central
├── templates/                # Templates HTML globales
├── static/                   # Archivos estáticos (CSS, JS, imágenes)
├── media/                    # Archivos subidos por usuarios
└── documentacion/            # Documentación completa del proyecto
```

## Documentación

Toda la documentación del proyecto se encuentra en el directorio `/documentacion/`:

### Documentación Técnica

- **requerimientos_software.txt** - Especificación completa de requerimientos funcionales y no funcionales
- **matriz_requerimientos.md** - Matriz de trazabilidad de requerimientos con estado de implementación
- **arquitectura_sistema.md** - Documentación detallada de la arquitectura monolítica modular
- **matriz_pruebas_unitarias.md** - Plan completo de pruebas unitarias con casos de prueba
- **diagrama_casos_uso_completo.drawio** - Diagrama completo de casos de uso (formato Draw.io)
- **diagrama_casos_uso_optimizado.drawio** - Diagrama optimizado de casos de uso

### Documentación de Usuario

- **manual_usuario.md** - Manual completo de usuario con instrucciones paso a paso

### Documentación de Gestión

- **cierre_proyecto.md** - Documento de cierre del proyecto con métricas y resultados

## Módulos del Sistema

### 1. Autenticación
- Inicio y cierre de sesión
- Control de acceso por roles
- Cambio de contraseña
- Gestión de perfiles

### 2. Clientes
- CRUD completo de clientes
- Búsqueda rápida (AJAX)
- Estadísticas de clientes
- Historial de compras
- Cliente casual para ventas rápidas

### 3. Inventario
- CRUD de productos con imágenes
- CRUD de categorías
- Control automático de stock
- Alertas de stock bajo
- Búsqueda avanzada

### 4. Ventas
- Interfaz intuitiva de punto de venta
- Cálculo automático de IVA (19%)
- Aplicación de descuentos
- Múltiples métodos de pago
- Generación de facturas
- Historial de ventas

### 5. Trabajadores
- CRUD de trabajadores
- Asignación de roles
- Activación/desactivación de cuentas

### 6. Reportes y Dashboard
- Dashboard personalizado por rol
- Reportes de ventas con filtros
- Reportes de productos más vendidos
- Top clientes
- Gráficos estadísticos
- Exportación a Excel

## Usuarios de Prueba

Si ejecutó `sembrar_datos.py`, puede usar estos usuarios de prueba:

**Administrador:**
- Usuario: admin_demo1
- Contraseña: admin123

**Trabajador:**
- Usuario: vendedor1
- Contraseña: vendedor123

## Errores Corregidos

En esta versión se corrigieron los siguientes errores críticos:

1. Archivos de configuración faltantes (settings.py, urls.py, wsgi.py, asgi.py)
2. Modelo Cliente duplicado en inventario/models.py
3. Import faltante de redirect en reportes/views.py
4. Referencia incorrecta a producto.codigo en ventas/views.py

## Estado del Proyecto

**PROYECTO COMPLETADO - 100% de requerimientos implementados**

- 46 requerimientos funcionales implementados
- 23 requerimientos no funcionales cumplidos
- 7 módulos completamente operativos
- Documentación completa entregada
- Sistema listo para despliegue en producción

## Licencia

Este proyecto ha sido desarrollado como parte de un proyecto académico/comercial.

## Contacto

**Desarrolladores:**
- Marco Antonio Saavedra
- Emanuel

---

**Última actualización:** Noviembre 2024
