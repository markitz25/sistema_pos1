# Flujos de trabajo principales

## 1. Gestión de productos e inventario (/inventario/)
- **Ver productos**: /inventario/, /inventario/listar/ o /inventario/productos/ muestran tabla con búsqueda y filtros por categoría.
- **Agregar producto** (dmin): /inventario/agregar/. Datos: nombre, categoría, precio, stock inicial, descripción (opcional), imagen (opcional).
- **Editar producto** (dmin): /inventario/editar/<producto_id>/.
- **Eliminar producto** (dmin): /inventario/eliminar/<producto_id>/ (pide confirmación).
- **Categorías** (dmin): listar /inventario/categorias/, crear /inventario/categorias/crear/, editar /inventario/categorias/editar/<id>/, eliminar /inventario/categorias/eliminar/<id>/.
- **Crear categoría rápida (AJAX)** (dmin): /inventario/categoria/crear-ajax/ desde formularios.

## 2. Gestión de clientes (/clientes/)
- **Listar**: /clientes/.
- **Crear**: /clientes/nuevo/ (nombre, documento, teléfono; correo/dirección opcionales).
- **Detalle/editar/eliminar**: /clientes/<id>/, /clientes/<id>/editar/, /clientes/<id>/eliminar/.
- **Activar/desactivar**: /clientes/<id>/toggle/ o /clientes/<id>/toggle-estado/.
- **Estadísticas**: /clientes/estadisticas/.

## 3. Registrar una venta (punto de venta)
- Rutas: /ventas/ o /ventas/punto-venta/ (requiere login).
- Pasos típicos:
  1) Buscar/seleccionar cliente (si no se envía, se usa “cliente casual” por defecto).
  2) Buscar productos (AJAX) y agregarlos con cantidades.
  3) Aplicar descuento por producto (porcentaje) si corresponde.
  4) Elegir método de pago: efectivo, mixto (efectivo + tarjeta/transferencia) u otro definido.
  5) Confirmar la venta. El sistema descuenta stock, calcula IVA (19%), registra subtotal/impuesto/total y notas de pago.
- Si el stock es insuficiente o el monto no cubre el total, la venta no se procesa.

## 4. Consultar ventas y facturas
- **Listar ventas**: /ventas/listar/ o /ventas/historial/. Trabajadores ven solo sus ventas; administradores ven todas.
- **Detalle de venta**: /ventas/detalle/<venta_id>/ (respeta permisos anteriores).
- **Cancelar venta** (dmin): /ventas/cancelar/<venta_id>/ restaura stock y ajusta total del cliente.
- **Factura/recibo**: /ventas/factura/<venta_id>/.

## 5. Reportes y exportaciones
- **Dashboard**: /tablero/ o /tablero/dashboard/ (redirige a admin/trabajador según rol).
- **Reportes**: /reportes/ con secciones de ventas (/reportes/ventas/), productos (/reportes/productos/) y clientes (/reportes/clientes/).
- **Exportar a Excel**: /reportes/exportar-excel/.

