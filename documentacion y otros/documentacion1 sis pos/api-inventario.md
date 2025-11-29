# API de Inventario

Todas las rutas requieren sesión iniciada. Las acciones de creación están restringidas a administradores.

## Crear categoría vía AJAX
- **POST** `/inventario/categoria/crear-ajax/`
- **Permiso**: administrador.
- **Body** (form-data o x-www-form-urlencoded):
  - `nombre` (obligatorio)
  - `descripcion` (opcional)
- **Respuesta 200 en éxito**
```json
{
  "success": true,
  "categoria_id": 10,
  "categoria_nombre": "Bebidas Energéticas",
  "message": "Categoría \"Bebidas Energéticas\" creada exitosamente"
}
```
- **Respuesta 200 en error de permisos**
```json
{
  "success": false,
  "error": "¡O Solo los administradores pueden realizar esta acción"
}
```
- **Respuesta 200 en validación fallida**
```json
{
  "success": false,
  "error": "El nombre de la categoría es requerido"
}
```
- **Notas**:
  - Si no hay sesión, se redirige a `/login/` (no retorna JSON útil).
  - Usar HTTPS y validaciones en servidor y cliente para evitar datos inconsistentes.

