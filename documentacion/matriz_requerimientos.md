# MATRIZ DE REQUERIMIENTOS - SISTEMA POS

**Desarrollado por:** Marco Antonio Saavedra y Emanuel

---

## REQUERIMIENTOS FUNCIONALES

| ID | Módulo | Requerimiento | Descripción | Prioridad | Estado | Verificación |
|---|---|---|---|---|---|---|
| RF01 | Autenticación | Inicio de Sesión | Autenticación mediante usuario y contraseña con validación en BD | Alta | Implementado | Login exitoso con credenciales válidas |
| RF02 | Autenticación | Cierre de Sesión | Cerrar sesión de forma segura eliminando sesión activa | Alta | Implementado | Sesión eliminada y redirección a login |
| RF03 | Autenticación | Gestión de Contraseñas | Cambio de contraseña proporcionando actual y nueva | Media | Implementado | Contraseña actualizada correctamente |
| RF04 | Autenticación | Control de Acceso por Roles | Diferenciación entre Administrador y Trabajador | Alta | Implementado | Restricciones aplicadas según rol |
| RF05 | Autenticación | Configuración Inicial | Asistente para crear primer administrador | Alta | Implementado | Primer admin creado exitosamente |
| RF06 | Trabajadores | Registro de Trabajadores | Crear trabajadores con datos completos | Alta | Implementado | Trabajador registrado en BD |
| RF07 | Trabajadores | Edición de Trabajadores | Modificar información de trabajadores | Media | Implementado | Datos actualizados correctamente |
| RF08 | Trabajadores | Listado de Trabajadores | Mostrar listado paginado con búsqueda | Media | Implementado | Listado mostrado correctamente |
| RF09 | Trabajadores | Activar/Desactivar Trabajadores | Cambiar estado sin eliminar registro | Media | Implementado | Estado cambiado correctamente |
| RF10 | Trabajadores | Visualización de Perfil | Ver y editar perfil personal | Baja | Implementado | Perfil actualizado correctamente |
| RF11 | Clientes | Registro de Clientes | Registrar clientes con datos completos | Alta | Implementado | Cliente registrado en BD |
| RF12 | Clientes | Validación de Datos | Validar unicidad de cédula y correo | Alta | Implementado | Duplicados rechazados correctamente |
| RF13 | Clientes | Edición de Clientes | Modificar información de clientes | Media | Implementado | Datos actualizados correctamente |
| RF14 | Clientes | Búsqueda de Clientes | Búsqueda por nombre, cédula o correo | Alta | Implementado | Resultados de búsqueda correctos |
| RF15 | Clientes | Estadísticas de Clientes | Calcular totales, promedios y última compra | Media | Implementado | Estadísticas calculadas correctamente |
| RF16 | Clientes | Cliente Casual | Mantener cliente especial para ventas sin registro | Alta | Implementado | Cliente casual disponible |
| RF17 | Clientes | Activar/Desactivar Clientes | Cambiar estado de clientes | Baja | Implementado | Estado cambiado correctamente |
| RF18 | Inventario | Gestión de Categorías | CRUD de categorías de productos | Alta | Implementado | Categorías gestionadas correctamente |
| RF19 | Inventario | Registro de Productos | Registrar productos con todos los atributos | Alta | Implementado | Producto registrado en BD |
| RF20 | Inventario | Edición de Productos | Modificar información de productos | Alta | Implementado | Datos actualizados correctamente |
| RF21 | Inventario | Control de Stock | Actualizar stock automáticamente en ventas | Alta | Implementado | Stock actualizado correctamente |
| RF22 | Inventario | Alertas de Stock Bajo | Identificar productos bajo stock mínimo | Media | Implementado | Alertas mostradas correctamente |
| RF23 | Inventario | Búsqueda de Productos | Búsqueda por nombre/código con filtros | Alta | Implementado | Búsqueda funcional correctamente |
| RF24 | Inventario | Imágenes de Productos | Cargar y almacenar imágenes | Media | Implementado | Imágenes guardadas correctamente |
| RF25 | Ventas | Interfaz de Punto de Venta | Interfaz intuitiva para procesar ventas | Alta | Implementado | Ventas procesadas correctamente |
| RF26 | Ventas | Selección de Cliente | Buscar y seleccionar cliente o usar casual | Alta | Implementado | Cliente asignado correctamente |
| RF27 | Ventas | Cálculo de IVA | Calcular IVA automáticamente (19%) | Alta | Implementado | IVA calculado correctamente |
| RF28 | Ventas | Aplicación de Descuentos | Aplicar descuentos por producto o total | Media | Implementado | Descuentos aplicados correctamente |
| RF29 | Ventas | Métodos de Pago | Soportar efectivo, tarjeta, transferencia y mixto | Alta | Implementado | Métodos registrados correctamente |
| RF30 | Ventas | Validación de Stock | Validar disponibilidad antes de procesar | Alta | Implementado | Validación funcional correctamente |
| RF31 | Ventas | Registro de Venta | Guardar venta con detalle completo | Alta | Implementado | Venta registrada en BD |
| RF32 | Ventas | Actualización Datos Cliente | Actualizar totales y fecha última compra | Media | Implementado | Datos actualizados automáticamente |
| RF33 | Ventas | Generación de Factura | Generar factura/recibo de venta | Alta | Implementado | Factura generada correctamente |
| RF34 | Ventas | Cancelación de Ventas | Cancelar venta y restaurar stock (solo admin) | Media | Implementado | Venta cancelada y stock restaurado |
| RF35 | Ventas | Historial de Ventas | Mantener historial con filtros | Media | Implementado | Historial mostrado correctamente |
| RF36 | Ventas | Detalle de Venta | Mostrar información completa de venta | Media | Implementado | Detalle mostrado correctamente |
| RF37 | Reportes | Dashboard por Rol | Mostrar dashboard según rol de usuario | Alta | Implementado | Dashboard personalizado correctamente |
| RF38 | Reportes | Estadísticas de Ventas | Calcular totales y comparativas | Alta | Implementado | Estadísticas calculadas correctamente |
| RF39 | Reportes | Productos Más Vendidos | Ranking por cantidad e ingresos | Media | Implementado | Ranking generado correctamente |
| RF40 | Reportes | Ventas por Categoría | Agrupar ventas por categoría | Media | Implementado | Agrupación correcta |
| RF41 | Reportes | Top Clientes | Identificar clientes con mayor volumen | Media | Implementado | Top clientes identificados |
| RF42 | Reportes | Gráficos Estadísticos | Generar gráficos de ventas y productos | Media | Implementado | Gráficos generados correctamente |
| RF43 | Reportes | Alertas Automáticas | Mostrar alertas de stock bajo y sin ventas | Media | Implementado | Alertas mostradas correctamente |
| RF44 | Reportes | Reporte de Ventas Detallado | Generar reportes con filtros avanzados | Alta | Implementado | Reportes generados correctamente |
| RF45 | Reportes | Reporte de Productos | Reporte de vendidos, sin ventas y stock bajo | Media | Implementado | Reportes generados correctamente |
| RF46 | Reportes | Exportación a Excel | Exportar reportes a formato Excel | Media | Implementado | Exportación exitosa |

---

## REQUERIMIENTOS NO FUNCIONALES

| ID | Categoría | Requerimiento | Descripción | Prioridad | Estado | Métrica de Verificación |
|---|---|---|---|---|---|---|
| RNF01 | Rendimiento | Tiempo de Respuesta | Respuesta menor a 2 segundos en operación normal | Alta | Implementado | Tiempo medido < 2s |
| RNF02 | Rendimiento | Capacidad de Procesamiento | Procesar 100 ventas simultáneas sin degradación | Media | Implementado | Pruebas de carga exitosas |
| RNF03 | Rendimiento | Carga de Páginas | Páginas cargando en menos de 3 segundos | Media | Implementado | Tiempo medido < 3s |
| RNF04 | Seguridad | Autenticación Obligatoria | Requerir autenticación para todas las funcionalidades | Alta | Implementado | Acceso bloqueado sin login |
| RNF05 | Seguridad | Almacenamiento Seguro | Contraseñas con hash seguro, nunca texto plano | Alta | Implementado | Passwords hasheadas en BD |
| RNF06 | Seguridad | Control de Sesiones | Implementar expiración por inactividad | Alta | Implementado | Sesión expira correctamente |
| RNF07 | Seguridad | Validación de Datos | Validar entradas en cliente y servidor | Alta | Implementado | Validaciones funcionando |
| RNF08 | Seguridad | Control de Acceso | Verificar permisos antes de operaciones críticas | Alta | Implementado | Permisos verificados |
| RNF09 | Usabilidad | Interfaz Intuitiva | Interfaz clara y fácil de usar | Alta | Implementado | Pruebas de usuario exitosas |
| RNF10 | Usabilidad | Responsive Design | Funcional en diferentes tamaños de pantalla | Media | Implementado | Compatible con dispositivos |
| RNF11 | Usabilidad | Mensajes de Error | Mensajes claros orientados a solución | Media | Implementado | Mensajes comprensibles |
| RNF12 | Usabilidad | Confirmaciones | Solicitar confirmación en acciones críticas | Alta | Implementado | Confirmaciones funcionando |
| RNF13 | Confiabilidad | Integridad de Datos | Garantizar integridad con validaciones y transacciones | Alta | Implementado | Datos íntegros |
| RNF14 | Confiabilidad | Respaldos | Permitir creación de respaldos de BD | Media | Implementado | Respaldos funcionando |
| RNF15 | Confiabilidad | Recuperación de Errores | Manejar errores sin pérdida de datos | Alta | Implementado | Errores manejados correctamente |
| RNF16 | Confiabilidad | Trazabilidad | Registrar operaciones críticas para auditoría | Media | Implementado | Logs creados correctamente |
| RNF17 | Mantenibilidad | Código Modular | Código organizado en módulos independientes | Alta | Implementado | Módulos separados |
| RNF18 | Mantenibilidad | Documentación | Código con comentarios y documentación | Media | Implementado | Documentación presente |
| RNF19 | Mantenibilidad | Estándares de Codificación | Seguir estándares de Python y Django | Alta | Implementado | Código cumple estándares |
| RNF20 | Mantenibilidad | Escalabilidad | Arquitectura permite agregar funcionalidades | Alta | Implementado | Extensible correctamente |
| RNF21 | Portabilidad | Independencia de Plataforma | Funcionar en Windows, Linux, macOS | Alta | Implementado | Compatible con todas |
| RNF22 | Portabilidad | Compatibilidad Navegadores | Compatible con Chrome, Firefox, Safari, Edge | Alta | Implementado | Compatible con navegadores |
| RNF23 | Portabilidad | BD Configurable | Configurar diferentes motores de BD | Media | Implementado | Configuración funcional |

---

## MATRIZ DE TRAZABILIDAD

| Requerimiento Funcional | Módulo Sistema | Caso de Uso | Prioridad | Dependencias |
|---|---|---|---|---|
| RF01-RF05 | autenticacion | Autenticación y Autorización | Alta | Ninguna |
| RF06-RF10 | trabajadores | Gestión de Trabajadores | Alta | RF01-RF04 |
| RF11-RF17 | clientes | Gestión de Clientes | Alta | RF01-RF04 |
| RF18-RF24 | inventario | Gestión de Inventario | Alta | RF01-RF04 |
| RF25-RF36 | ventas | Punto de Venta | Alta | RF01-RF04, RF11-RF17, RF18-RF24 |
| RF37-RF46 | reportes, tablero | Reportes y Dashboard | Media | RF25-RF36 |

---

## COBERTURA DE REQUERIMIENTOS

| Módulo | Total Requerimientos | Implementados | Porcentaje |
|---|---|---|---|
| Autenticación | 5 | 5 | 100% |
| Trabajadores | 5 | 5 | 100% |
| Clientes | 7 | 7 | 100% |
| Inventario | 7 | 7 | 100% |
| Ventas | 12 | 12 | 100% |
| Reportes | 10 | 10 | 100% |
| **TOTAL** | **46** | **46** | **100%** |

---

## NOTAS

Todos los requerimientos funcionales han sido implementados completamente en el sistema.
Los requerimientos no funcionales cumplen con los estándares establecidos.
El sistema está listo para despliegue en ambiente de producción.

---

**Fecha de elaboración:** Noviembre 2024
**Elaborado por:** Marco Antonio Saavedra y Emanuel
