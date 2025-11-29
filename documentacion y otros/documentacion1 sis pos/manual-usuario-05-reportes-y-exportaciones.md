# Reportes y exportaciones

## Tablero de control
- Rutas: /tablero/ o /tablero/dashboard/ (redirige según rol a admin/trabajador).
- Muestra datos resumidos: ventas por mes, productos más vendidos, ventas por categoría y accesos rápidos. Usa APIs internas (Chart.js).

## Reporte de ventas (/reportes/ventas/)
- Listado de ventas con filtros por rango de fechas, estado y cliente.
- Totales y resúmenes.

## Reporte de productos (/reportes/productos/)
- Datos relacionados con ventas para cada producto (cuáles se venden más, stock relevante según implementación).

## Reporte de clientes (/reportes/clientes/)
- Estadísticas de clientes y, según la lógica implementada, identificación de clientes frecuentes.

## Exportar a Excel (/reportes/exportar-excel/)
- Genera archivo Excel con la información de reportes para respaldo o análisis externo.
- Si el navegador bloquea la descarga, revisar configuraciones de seguridad o probar otro navegador.

