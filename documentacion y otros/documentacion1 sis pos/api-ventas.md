# API de Ventas

Todas las rutas requieren sesión iniciada. La búsqueda de productos está disponible para administradores y trabajadores.

## Buscar productos para el punto de venta
- **GET** `/ventas/api/buscar-productos/` (alias `/ventas/buscar-productos/`)
- **Query params**:
  - `q` (opcional): texto a buscar en nombre o código.
  - `categoria_id` (opcional): filtra por categoría.
- **Respuesta 200 (ejemplo)**
```json
{
  "productos": [
    {
      "id": 1,
      "nombre": "Leche Entera 1L",
      "codigo": "LEC001",
      "precio": 3500.0,
      "stock": 20,
      "categoria": "Lácteos",
      "imagen_url": "/media/productos/leche1l.jpg"
    }
  ]
}
```
- **Notas**:
  - Solo devuelve productos con `stock > 0`.
  - Limita a 20 resultados.
  - Si no hay sesión, redirige a `/login/` (302). No se devuelve JSON en ese caso.

## Rutas HTML relacionadas (para contexto, no JSON)
- Listar/historial: `/ventas/listar/`, `/ventas/historial/`
- Detalle: `/ventas/detalle/<venta_id>/`
- Cancelar (solo admin): `/ventas/cancelar/<venta_id>/`
- Factura: `/ventas/factura/<venta_id>/`

