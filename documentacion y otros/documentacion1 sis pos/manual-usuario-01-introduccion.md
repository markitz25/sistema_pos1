# Introducción al Sistema POS

## Qué es el Sistema POS
Aplicación web (Django) para puntos de venta. Permite:
- Registrar ventas de forma rápida.
- Administrar productos y categorías.
- Llevar registro de clientes.
- Gestionar trabajadores del sistema.
- Consultar reportes y estadísticas.

Se usa vía navegador dentro de la red donde está instalado el servidor.

## Módulos principales
- **Autenticación**: login (/login/), logout (/logout/), setup inicial (/setup/).
- **Tablero (dashboard)**: /tablero/ y /tablero/dashboard/ muestran ventas por mes, productos más vendidos, ventas por categoría y accesos rápidos.
- **Trabajadores**: /trabajadores/ para crear, editar y activar/desactivar usuarios internos.
- **Inventario**: /inventario/ para productos (nombre, precio, stock, categoría, imagen) y categorías.
- **Clientes**: /clientes/ para registrar, consultar y actualizar clientes, con estadísticas básicas.
- **Ventas**: /ventas/ (punto de venta) para registrar ventas, buscar productos, aplicar descuentos y generar factura.
- **Reportes**: /reportes/ para reportes de ventas, productos y clientes, y exportar a Excel.

## Roles de usuario
1. **Administrador**: acceso completo; crea/edita trabajadores; gestiona productos, categorías y clientes; revisa reportes y estadísticas; puede cancelar ventas y hacer configuraciones sensibles.
2. **Trabajador**: acceso limitado; se enfoca en registrar ventas y consultas básicas; puede ver su perfil y cambiar contraseña.

Definir roles protege la información y evita cambios críticos por usuarios no autorizados.

