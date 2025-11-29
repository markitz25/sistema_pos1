# Roles, accesos y seguridad básica

## Inicio de sesión
1. Abrir el navegador y acceder a la URL del sistema.
2. Si no hay sesión iniciada, se redirige a /login/ (todas las vistas requieren autenticación).
3. Ingresar usuario y contraseña asignados.
4. Al autenticar, se redirige al tablero (/tablero/).

## Cerrar sesión
- Usar la opción **Cerrar sesión** del menú (/logout/).
- Confirmar si se solicita y verificar que vuelve a la pantalla de login.

## Roles
### Administrador
- Acceso completo a todos los módulos.
- Gestiona trabajadores (/trabajadores/), productos y categorías (/inventario/), clientes (/clientes/).
- Revisa reportes/exportaciones (/reportes/) y tablero admin (/tablero/admin/).
- Puede cancelar ventas (/ventas/cancelar/<id>/) y emitir facturas (/ventas/factura/<id>/).

### Trabajador
- Acceso limitado al punto de venta (/ventas/, /ventas/punto-venta/) y tablero de trabajador (/tablero/trabajador/).
- Puede consultar listados básicos y su perfil/cambiar contraseña (/trabajadores/perfil/, /trabajadores/cambiar-contrasena/).

## Buenas prácticas de seguridad
- No compartir usuarios ni contraseñas; cambiarlas periódicamente.
- Cerrar sesión al terminar el turno.
- Asignar rol de administrador solo a personal de confianza.
- Desactivar cuentas de trabajadores que ya no usan el sistema.

