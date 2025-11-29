# API del Tablero (Dashboard)

Todas las rutas requieren sesión iniciada. Se usan para renderizar gráficos (Chart.js) en el dashboard.

## Ventas por mes
- **GET** `/tablero/api/ventas-por-mes/`
- **Respuesta 200 (ejemplo)**
```json
{
  "labels": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
  "data": [1500000.0, 2100000.0, 1800000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
}
```
- **Notas**: devuelve los últimos 12 meses; nombres según configuración regional del servidor; solo incluye ventas con estado `completada`.

## Productos más vendidos
- **GET** `/tablero/api/productos-mas-vendidos/`
- **Respuesta 200 (ejemplo)**
```json
{
  "labels": ["Leche Entera 1L", "Pan Blanco"],
  "data": [120, 90]
}
```
- **Notas**: top 10 por cantidad vendida; solo ventas con estado `completada`.

## Ventas por categoría
- **GET** `/tablero/api/ventas-por-categoria/`
- **Respuesta 200 (ejemplo)**
```json
{
  "labels": ["Lácteos", "Bebidas", "Sin categoría"],
  "data": [500000.0, 350000.0, 80000.0]
}
```
- **Notas**: calcula total por categoría (cantidad × precio_unitario); top 5; si una categoría es nula se etiqueta como "Sin categoría".

