# Problemas frecuentes y soluciones

## El sistema no carga en el navegador
Posibles causas:
- URL mal escrita.
- Servidor del sistema apagado.
- Problemas en la red local.

Soluciones:
- Verificar la URL.
- Preguntar al responsable técnico si el servidor está encendido.
- Probar desde otro equipo para descartar problemas locales.

## El stock no se actualiza después de una venta
Posibles causas:
- La venta no se completó (no se confirmó).
- Ocurrió un error al registrar la venta.
- Caché del navegador mostrando una versión antigua.

Soluciones:
- Revisar si la venta aparece en `/ventas/listar/` o `/ventas/historial/`.
- Refrescar la página (F5).
- Cerrar sesión y volver a entrar.

## No puedo exportar a Excel
Posibles causas:
- El navegador bloquea descargas.
- El usuario no tiene permisos para `/reportes/`.
- Error puntual en el servidor.

Soluciones:
- Probar en otro navegador.
- Confirmar acceso al módulo de reportes.
- Si persiste, informar al responsable técnico con capturas.

## Error de permisos al crear categoría rápida
- Solo administradores pueden usar `/inventario/categoria/crear-ajax/`.
- Si eres trabajador, pide a un administrador que cree la categoría en `/inventario/categorias/crear/`.

## El tablero no muestra datos o gráficos
Posibles causas:
- No hay ventas en el período consultado.
- Alguna API del tablero falla.

Soluciones:
- Registrar una venta de prueba y verificar.
- Pedir revisión técnica de:
  - `/tablero/api/ventas-por-mes/`
  - `/tablero/api/productos-mas-vendidos/`
  - `/tablero/api/ventas-por-categoria/`

