# MANUAL DE USUARIO
## SISTEMA DE PUNTO DE VENTA (POS)

**Versión:** 1.0
**Desarrollado por:** Marco Antonio Saavedra y Emanuel
**Fecha:** Noviembre 2024

---

## TABLA DE CONTENIDO

1. Introducción
2. Requisitos del Sistema
3. Acceso al Sistema
4. Panel Principal (Dashboard)
5. Gestión de Clientes
6. Gestión de Inventario
7. Punto de Venta
8. Historial de Ventas
9. Reportes y Estadísticas
10. Gestión de Trabajadores
11. Perfil de Usuario
12. Preguntas Frecuentes
13. Solución de Problemas

---

## 1. INTRODUCCIÓN

### 1.1 Objetivo del Manual

Este manual proporciona instrucciones completas para el uso del Sistema de Punto de Venta (POS). Está diseñado para ayudar a los usuarios a familiarizarse con todas las funcionalidades del sistema y realizar sus tareas de manera eficiente.

### 1.2 A Quién Está Dirigido

Este manual está dirigido a:
- Administradores del sistema
- Personal de ventas
- Supervisores y gerentes
- Personal de inventario

### 1.3 Descripción del Sistema

El Sistema POS es una aplicación web integral que permite:
- Procesar ventas de manera rápida y eficiente
- Gestionar inventario de productos
- Administrar información de clientes
- Generar reportes y estadísticas
- Controlar accesos mediante roles de usuario

---

## 2. REQUISITOS DEL SISTEMA

### 2.1 Requisitos de Hardware

- Computadora con procesador de 1.5 GHz o superior
- Mínimo 2 GB de memoria RAM
- Conexión a red local o internet
- Monitor con resolución mínima de 1024x768
- Mouse y teclado

### 2.2 Requisitos de Software

- Navegador web actualizado:
  - Google Chrome (recomendado)
  - Mozilla Firefox
  - Microsoft Edge
  - Safari
- Conexión a internet o red local
- JavaScript habilitado en el navegador

### 2.3 Recomendaciones

- Usar navegador Google Chrome para mejor experiencia
- Mantener navegador actualizado a la última versión
- Conexión estable a internet
- No cerrar navegador durante operaciones de venta

---

## 3. ACCESO AL SISTEMA

### 3.1 Inicio de Sesión

**Paso 1:** Abrir el navegador web e ingresar la dirección del sistema proporcionada por el administrador.

Ejemplo: `http://sistemapos.empresa.com` o `http://192.168.1.100:8000`

**Paso 2:** Se mostrará la pantalla de inicio de sesión con los siguientes campos:
- Usuario
- Contraseña

**Paso 3:** Ingresar sus credenciales proporcionadas por el administrador.

**Paso 4:** Hacer clic en el botón "Iniciar Sesión".

**Resultado:** El sistema validará sus credenciales y lo redirigirá al panel principal según su rol (Administrador o Trabajador).

### 3.2 Primer Acceso al Sistema

Si es el primer acceso al sistema y no existen usuarios:

**Paso 1:** El sistema mostrará automáticamente el asistente de configuración inicial.

**Paso 2:** Complete el formulario con la siguiente información:
- Nombre de usuario
- Contraseña (mínimo 8 caracteres)
- Confirmación de contraseña
- Nombre completo
- Correo electrónico
- Teléfono

**Paso 3:** Haga clic en "Crear Administrador".

**Resultado:** Se creará el primer usuario administrador y será redirigido al inicio de sesión.

### 3.3 Cerrar Sesión

**Paso 1:** Haga clic en su nombre de usuario en la esquina superior derecha.

**Paso 2:** Seleccione "Cerrar Sesión" del menú desplegable.

**Resultado:** Su sesión será cerrada y será redirigido a la pantalla de inicio de sesión.

---

## 4. PANEL PRINCIPAL (DASHBOARD)

### 4.1 Dashboard de Administrador

Al iniciar sesión como administrador, verá el dashboard completo con:

**Tarjetas de Métricas:**
- Total de ventas del día
- Total de ventas del mes
- Número de ventas realizadas
- Promedio de venta

**Productos Más Vendidos:**
- Top 10 productos con mayor cantidad vendida
- Ingresos generados por producto

**Alertas Importantes:**
- Productos con stock bajo
- Días sin ventas

**Gráficos:**
- Ventas de los últimos 12 meses
- Ventas por categoría
- Top productos

**Accesos Rápidos:**
- Botón "Nueva Venta" para acceder al punto de venta
- Enlaces a módulos principales

### 4.2 Dashboard de Trabajador

El dashboard de trabajador muestra información limitada:
- Total de sus ventas del día
- Número de ventas realizadas
- Acceso directo al punto de venta
- Sus últimas ventas

### 4.3 Navegación Principal

El menú de navegación se encuentra en la parte superior y contiene:

**Para Administradores:**
- Inicio (Dashboard)
- Ventas
- Clientes
- Inventario
- Trabajadores
- Reportes

**Para Trabajadores:**
- Inicio (Dashboard)
- Ventas
- Clientes
- Inventario (solo lectura)

---

## 5. GESTIÓN DE CLIENTES

### 5.1 Ver Lista de Clientes

**Paso 1:** Haga clic en "Clientes" en el menú principal.

**Paso 2:** Se mostrará la lista de clientes con la siguiente información:
- Nombre
- Cédula
- Correo electrónico
- Teléfono
- Total de compras
- Estado (Activo/Inactivo)

**Funcionalidades disponibles:**
- Búsqueda por nombre, cédula o correo
- Paginación de resultados
- Botones de acción (Ver, Editar, Desactivar)

### 5.2 Registrar Nuevo Cliente

**Paso 1:** En la página de clientes, haga clic en el botón "Nuevo Cliente".

**Paso 2:** Complete el formulario con los siguientes datos:

**Campos Obligatorios:**
- Nombre completo
- Cédula (única en el sistema)
- Correo electrónico (único en el sistema)
- Teléfono (formato: 10 dígitos)

**Campos Opcionales:**
- Dirección
- Notas adicionales

**Paso 3:** Haga clic en "Guardar Cliente".

**Resultado:** El cliente será registrado y aparecerá en la lista de clientes.

**Validaciones:**
- La cédula no debe estar registrada previamente
- El correo no debe estar registrado previamente
- El teléfono debe tener formato válido

### 5.3 Editar Cliente

**Paso 1:** En la lista de clientes, haga clic en el botón "Editar" del cliente deseado.

**Paso 2:** Modifique los datos necesarios en el formulario.

**Paso 3:** Haga clic en "Actualizar Cliente".

**Resultado:** Los cambios serán guardados y se mostrará un mensaje de confirmación.

### 5.4 Ver Detalle de Cliente

**Paso 1:** Haga clic en el nombre del cliente o en el botón "Ver Detalle".

**Información mostrada:**
- Datos personales completos
- Fecha de registro
- Última fecha de compra
- Total acumulado de compras
- Número total de compras
- Promedio de compra
- Historial de compras recientes

### 5.5 Buscar Cliente

**Método 1: Búsqueda en Lista**

**Paso 1:** En la página de clientes, use el campo de búsqueda.

**Paso 2:** Ingrese nombre, cédula o correo del cliente.

**Paso 3:** Presione Enter o haga clic en el botón de búsqueda.

**Método 2: Búsqueda Rápida (en Punto de Venta)**

**Paso 1:** En el punto de venta, comience a escribir el nombre del cliente.

**Paso 2:** Aparecerá una lista desplegable con sugerencias.

**Paso 3:** Seleccione el cliente deseado.

### 5.6 Estadísticas de Clientes

**Paso 1:** En la página de clientes, haga clic en "Estadísticas".

**Información disponible:**
- Total de clientes registrados
- Clientes activos
- Top 10 clientes por volumen de compras
- Clientes nuevos del mes
- Clientes frecuentes (más de 10 compras)

---

## 6. GESTIÓN DE INVENTARIO

### 6.1 Ver Productos

**Paso 1:** Haga clic en "Inventario" en el menú principal.

**Paso 2:** Se mostrará la lista de productos con:
- Imagen del producto
- Nombre
- Categoría
- Código de barras
- Precio de venta
- Stock disponible
- Estado

**Funcionalidades:**
- Filtrar por categoría
- Buscar por nombre o código de barras
- Ver productos con stock bajo
- Ordenar por diferentes criterios

### 6.2 Agregar Nuevo Producto (Solo Administrador)

**Paso 1:** En la página de inventario, haga clic en "Agregar Producto".

**Paso 2:** Complete el formulario:

**Información Básica:**
- Nombre del producto (obligatorio)
- Categoría (obligatorio)
- Código de barras (opcional, único)
- Descripción (opcional)

**Información de Precios:**
- Precio de compra (obligatorio)
- Precio de venta (obligatorio)

**Información de Stock:**
- Stock inicial (obligatorio)
- Stock mínimo (por defecto 10)

**Imagen:**
- Cargar imagen del producto (opcional)

**Paso 3:** Haga clic en "Guardar Producto".

**Resultado:** El producto será agregado al inventario.

**Validaciones:**
- El código de barras no debe estar duplicado
- Los precios deben ser mayores a 0
- El stock debe ser un número positivo

### 6.3 Editar Producto (Solo Administrador)

**Paso 1:** En la lista de productos, haga clic en "Editar".

**Paso 2:** Modifique los campos necesarios.

**Paso 3:** Haga clic en "Actualizar Producto".

**Resultado:** Los cambios serán guardados.

**Nota:** No puede modificar el código de barras si ya está en uso.

### 6.4 Gestión de Categorías

**Ver Categorías:**

**Paso 1:** En la página de inventario, haga clic en "Categorías".

**Paso 2:** Se mostrará la lista de categorías con:
- Nombre
- Descripción
- Número de productos en la categoría

**Crear Nueva Categoría:**

**Paso 1:** Haga clic en "Nueva Categoría".

**Paso 2:** Complete:
- Nombre de la categoría (obligatorio)
- Descripción (opcional)

**Paso 3:** Haga clic en "Guardar".

**Crear Categoría Rápida (desde formulario de producto):**

**Paso 1:** En el formulario de producto, junto al campo categoría, haga clic en "+".

**Paso 2:** Ingrese el nombre de la nueva categoría.

**Paso 3:** La categoría será creada y seleccionada automáticamente.

### 6.5 Alertas de Stock

El sistema muestra alertas automáticas cuando:
- Un producto tiene stock inferior al stock mínimo configurado
- Un producto está agotado (stock = 0)

**Ver productos con stock bajo:**

**Paso 1:** En el dashboard o en inventario, busque la sección "Alertas".

**Paso 2:** Se mostrarán los productos que requieren reabastecimiento.

---

## 7. PUNTO DE VENTA

### 7.1 Acceder al Punto de Venta

**Paso 1:** Haga clic en "Ventas" en el menú principal.

**Paso 2:** Seleccione "Nueva Venta" o "Punto de Venta".

**Resultado:** Se abrirá la interfaz del punto de venta.

### 7.2 Realizar una Venta

**Paso 1: Búsqueda de Productos**

Existen dos métodos para agregar productos:

**Método 1: Búsqueda por Nombre o Código**
- Use el campo de búsqueda en la parte superior
- Escriba el nombre o código del producto
- Seleccione el producto de la lista desplegable
- El producto se agregará a la venta

**Método 2: Explorar por Categorías**
- Seleccione una categoría del menú de categorías
- Se mostrarán los productos de esa categoría
- Haga clic en el producto deseado para agregarlo

**Paso 2: Ajustar Cantidades**

- Cada producto agregado aparece en la lista de venta
- Use los botones "+" y "-" para ajustar cantidades
- O ingrese la cantidad directamente en el campo
- Para eliminar un producto, haga clic en el ícono de eliminar

**Paso 3: Aplicar Descuentos (Opcional)**

**Descuento por Producto:**
- Haga clic en el campo de descuento del producto
- Ingrese el porcentaje o monto de descuento
- El subtotal se actualizará automáticamente

**Descuento General:**
- Use el campo "Descuento Total" en el resumen
- Ingrese el descuento a aplicar sobre el total

**Paso 4: Seleccionar Cliente**

**Opción 1: Cliente Registrado**
- En el campo "Cliente", comience a escribir el nombre
- Seleccione el cliente de la lista desplegable
- Los datos del cliente se mostrarán

**Opción 2: Cliente Casual**
- Deje seleccionado "Cliente Casual" (por defecto)
- Use esta opción para ventas rápidas sin registro

**Paso 5: Revisar Totales**

El resumen de venta muestra:
- Subtotal (suma de productos)
- IVA (19% del subtotal)
- Descuento (si aplica)
- Total a pagar

**Paso 6: Seleccionar Método de Pago**

Métodos disponibles:
- Efectivo
- Tarjeta
- Transferencia
- Mixto (efectivo + otro método)

**Para pago mixto:**
- Seleccione "Mixto"
- Ingrese el monto en efectivo
- Ingrese el monto en el otro método
- El sistema validará que sumen el total

**Paso 7: Procesar Venta**

**Paso final:** Haga clic en el botón "Procesar Venta".

**Validaciones automáticas:**
- Verifica que haya al menos un producto
- Valida stock disponible de cada producto
- Verifica método de pago seleccionado
- En pago mixto, valida que los montos sumen el total

**Resultado:**
- La venta se registra en el sistema
- El stock se actualiza automáticamente
- Los datos del cliente se actualizan
- Se muestra un mensaje de confirmación
- Se ofrece opción de generar factura

### 7.3 Generar Factura

**Paso 1:** Después de procesar la venta, haga clic en "Generar Factura".

**Paso 2:** Se abrirá la factura en una nueva ventana.

**Contenido de la factura:**
- Número de venta
- Fecha y hora
- Datos del cliente
- Detalle de productos (nombre, cantidad, precio, subtotal)
- Subtotal
- IVA
- Descuentos
- Total
- Método de pago
- Nombre del vendedor

**Paso 3:** Use las opciones del navegador para:
- Imprimir la factura
- Guardar como PDF
- Enviar por correo

### 7.4 Cancelar Venta en Proceso

Si necesita cancelar una venta antes de procesarla:

**Paso 1:** Haga clic en "Cancelar" o "Limpiar".

**Paso 2:** Confirme la acción.

**Resultado:** Todos los productos serán eliminados y la venta se reiniciará.

---

## 8. HISTORIAL DE VENTAS

### 8.1 Ver Historial de Ventas

**Paso 1:** Haga clic en "Ventas" en el menú principal.

**Paso 2:** Seleccione "Historial" o "Ver Ventas".

**Información mostrada:**
- Número de venta
- Fecha y hora
- Cliente
- Total de la venta
- Método de pago
- Estado (Completada, Cancelada)
- Vendedor que realizó la venta

**Acciones disponibles:**
- Ver detalle de venta
- Generar factura
- Cancelar venta (solo administrador)

### 8.2 Filtrar Ventas

**Filtros disponibles:**

**Por Fecha:**
- Seleccione fecha de inicio
- Seleccione fecha de fin
- Haga clic en "Filtrar"

**Por Cliente:**
- Seleccione cliente del listado
- Se mostrarán solo sus ventas

**Por Método de Pago:**
- Seleccione método (efectivo, tarjeta, etc.)
- Se mostrarán ventas con ese método

**Por Estado:**
- Completadas
- Canceladas
- Pendientes

**Por Vendedor (solo administrador):**
- Seleccione trabajador
- Se mostrarán sus ventas

### 8.3 Ver Detalle de Venta

**Paso 1:** En el historial, haga clic en el número de venta o en "Ver Detalle".

**Información completa:**
- Datos del cliente
- Fecha y hora exacta
- Vendedor
- Lista completa de productos con:
  - Nombre del producto
  - Cantidad
  - Precio unitario
  - Subtotal por producto
- Subtotal general
- IVA aplicado
- Descuentos
- Total final
- Método de pago
- Estado de la venta
- Notas adicionales

**Acciones:**
- Generar factura
- Volver al historial

### 8.4 Cancelar Venta (Solo Administrador)

**Importante:** Solo los administradores pueden cancelar ventas.

**Paso 1:** En el detalle de la venta, haga clic en "Cancelar Venta".

**Paso 2:** Aparecerá un mensaje de confirmación explicando que:
- La venta se marcará como cancelada
- El stock de los productos será restaurado
- Esta acción no se puede deshacer

**Paso 3:** Confirme la acción.

**Resultado:**
- El estado de la venta cambia a "Cancelada"
- El stock de cada producto se incrementa según las cantidades vendidas
- Se muestra un mensaje de confirmación

**Nota:** Las ventas canceladas permanecen en el historial para fines de auditoría.

---

## 9. REPORTES Y ESTADÍSTICAS

**Acceso:** Solo disponible para Administradores

### 9.1 Dashboard de Reportes

**Paso 1:** Haga clic en "Reportes" en el menú principal.

**Paso 2:** Se mostrará el dashboard de reportes con:
- Total de ventas del mes
- Cantidad de ventas realizadas
- Producto más vendido
- Cliente con más compras

### 9.2 Reporte de Ventas

**Paso 1:** En Reportes, seleccione "Reporte de Ventas".

**Paso 2:** Configure los filtros:
- Rango de fechas (inicio y fin)
- Método de pago (opcional)
- Cliente específico (opcional)

**Paso 3:** Haga clic en "Generar Reporte".

**Información del reporte:**
- Total de ventas en el período
- Cantidad de transacciones
- Promedio de venta
- Desglose por método de pago
- Lista detallada de ventas

**Exportar:**
- Haga clic en "Exportar a Excel"
- El archivo se descargará automáticamente

### 9.3 Reporte de Productos

**Paso 1:** Seleccione "Reporte de Productos".

**Secciones del reporte:**

**Productos Más Vendidos:**
- Top 20 productos por cantidad
- Ingresos generados por cada producto
- Categoría del producto

**Productos sin Ventas:**
- Lista de productos que no han tenido ventas
- Útil para identificar productos de baja rotación

**Productos con Stock Bajo:**
- Productos por debajo del stock mínimo
- Requieren reabastecimiento urgente

**Ventas por Categoría:**
- Total de ventas agrupadas por categoría
- Unidades vendidas por categoría
- Ingresos por categoría

### 9.4 Reporte de Clientes

**Paso 1:** Seleccione "Reporte de Clientes".

**Información del reporte:**

**Top Clientes:**
- Los 20 mejores clientes por volumen de compras
- Total gastado por cada cliente
- Número de compras realizadas
- Promedio de compra

**Clientes Nuevos:**
- Clientes registrados en el mes actual
- Tendencia de crecimiento

**Estadísticas Generales:**
- Total de clientes activos
- Total de clientes inactivos
- Promedio de compras por cliente

### 9.5 Gráficos Estadísticos

**Gráfico de Ventas Mensuales:**
- Muestra ventas de los últimos 12 meses
- Permite identificar tendencias y estacionalidad

**Gráfico de Productos Top:**
- Top 10 productos más vendidos
- Visualización en gráfico de barras

**Gráfico de Ventas por Categoría:**
- Distribución de ventas por categoría
- Visualización en gráfico circular

**Interacción con gráficos:**
- Pase el cursor sobre barras/sectores para ver valores exactos
- Los gráficos se actualizan automáticamente con nuevas ventas

---

## 10. GESTIÓN DE TRABAJADORES (Solo Administrador)

### 10.1 Ver Lista de Trabajadores

**Paso 1:** Haga clic en "Trabajadores" en el menú principal.

**Información mostrada:**
- Nombre completo
- Usuario
- Rol (Administrador/Trabajador)
- Teléfono
- Estado (Activo/Inactivo)
- Fecha de creación

### 10.2 Crear Nuevo Trabajador

**Paso 1:** Haga clic en "Crear Trabajador".

**Paso 2:** Complete el formulario:

**Información de Usuario:**
- Nombre de usuario (único, sin espacios)
- Contraseña (mínimo 8 caracteres)
- Confirmar contraseña

**Información Personal:**
- Nombre
- Apellido
- Teléfono
- Dirección (opcional)

**Rol:**
- Administrador: Acceso completo al sistema
- Trabajador: Acceso limitado a ventas y consultas

**Paso 3:** Haga clic en "Guardar Trabajador".

**Resultado:** El trabajador será creado y podrá acceder al sistema con sus credenciales.

### 10.3 Editar Trabajador

**Paso 1:** En la lista de trabajadores, haga clic en "Editar".

**Paso 2:** Modifique los datos necesarios.

**Nota:** No puede cambiar el nombre de usuario una vez creado.

**Paso 3:** Haga clic en "Actualizar".

### 10.4 Desactivar/Activar Trabajador

**Para desactivar:**

**Paso 1:** Haga clic en el botón "Desactivar" del trabajador.

**Paso 2:** Confirme la acción.

**Resultado:**
- El trabajador no podrá iniciar sesión
- Sus datos permanecen en el sistema
- Sus ventas anteriores se mantienen

**Para reactivar:**

**Paso 1:** Haga clic en "Activar".

**Resultado:** El trabajador puede volver a acceder al sistema.

---

## 11. PERFIL DE USUARIO

### 11.1 Ver Mi Perfil

**Paso 1:** Haga clic en su nombre de usuario en la esquina superior derecha.

**Paso 2:** Seleccione "Mi Perfil".

**Información mostrada:**
- Nombre completo
- Nombre de usuario
- Correo electrónico
- Teléfono
- Dirección
- Rol en el sistema
- Fecha de registro

### 11.2 Editar Mi Perfil

**Paso 1:** En Mi Perfil, haga clic en "Editar Perfil".

**Paso 2:** Modifique los datos que desee cambiar:
- Nombre
- Apellido
- Teléfono
- Dirección

**Nota:** No puede cambiar su nombre de usuario ni rol.

**Paso 3:** Haga clic en "Guardar Cambios".

### 11.3 Cambiar Contraseña

**Paso 1:** En el menú de usuario, seleccione "Cambiar Contraseña".

**Paso 2:** Complete el formulario:
- Contraseña actual
- Nueva contraseña (mínimo 8 caracteres)
- Confirmar nueva contraseña

**Paso 3:** Haga clic en "Cambiar Contraseña".

**Validaciones:**
- La contraseña actual debe ser correcta
- Las contraseñas nuevas deben coincidir
- La nueva contraseña debe cumplir los requisitos mínimos

**Resultado:** Su contraseña será actualizada y deberá usar la nueva en el próximo inicio de sesión.

---

## 12. PREGUNTAS FRECUENTES

### 12.1 Ventas

**P: ¿Qué hago si un producto no aparece en la búsqueda?**
R: Verifique que el producto esté activo en el inventario. Si no existe, un administrador debe crearlo primero.

**P: ¿Puedo modificar una venta después de procesarla?**
R: No, las ventas no pueden modificarse una vez procesadas. Solo un administrador puede cancelarla y crear una nueva.

**P: ¿Qué pasa si proceso una venta sin stock suficiente?**
R: El sistema valida automáticamente el stock antes de procesar. Si no hay suficiente stock, mostrará un error y no permitirá completar la venta.

**P: ¿Debo crear un cliente para cada venta?**
R: No es obligatorio. Puede usar "Cliente Casual" para ventas rápidas. Sin embargo, registrar clientes permite llevar un mejor control y ofrecer mejor servicio.

### 12.2 Clientes

**P: ¿Qué hago si intento registrar un cliente y dice que la cédula ya existe?**
R: Significa que ya hay un cliente con esa cédula. Use la búsqueda para encontrarlo. Si está inactivo, un administrador puede reactivarlo.

**P: ¿Puedo eliminar un cliente?**
R: No se eliminan clientes, solo se desactivan. Esto mantiene el historial de ventas intacto.

### 12.3 Inventario

**P: ¿Cómo se actualiza el stock automáticamente?**
R: Cada vez que se procesa una venta, el sistema resta automáticamente las cantidades vendidas. Si se cancela una venta, el stock se restaura.

**P: ¿Qué es el stock mínimo?**
R: Es la cantidad mínima que debería tener siempre. Cuando el stock baja de este nivel, el sistema genera una alerta.

**P: ¿Puedo tener productos sin código de barras?**
R: Sí, el código de barras es opcional. Sin embargo, facilita la búsqueda en el punto de venta.

### 12.4 Reportes

**P: ¿Cada cuánto se actualizan los reportes?**
R: Los reportes se generan en tiempo real cada vez que los solicita.

**P: ¿Puedo ver reportes de meses anteriores?**
R: Sí, use los filtros de fecha para seleccionar el rango que desee consultar.

---

## 13. SOLUCIÓN DE PROBLEMAS

### 13.1 No Puedo Iniciar Sesión

**Problema:** El sistema muestra "Usuario o contraseña incorrectos"

**Soluciones:**
1. Verifique que está escribiendo correctamente el usuario y contraseña
2. Asegúrese de que no tiene activado el bloqueo de mayúsculas
3. Si olvidó su contraseña, contacte al administrador
4. Verifique que su cuenta esté activa

### 13.2 La Página No Carga o Carga Lentamente

**Soluciones:**
1. Verifique su conexión a internet
2. Actualice la página (F5 o Ctrl+R)
3. Cierre pestañas innecesarias del navegador
4. Limpie el caché del navegador
5. Intente con otro navegador

### 13.3 Error al Procesar Venta

**Problema:** "Error al procesar la venta"

**Soluciones:**
1. Verifique que hay stock suficiente de todos los productos
2. Asegúrese de haber seleccionado un método de pago
3. En pago mixto, verifique que los montos sumen el total
4. Verifique su conexión a internet
5. Si persiste, contacte al administrador

### 13.4 No Encuentro un Producto

**Soluciones:**
1. Verifique que está escribiendo correctamente el nombre
2. Busque por código de barras si lo tiene
3. Explore por categorías
4. El producto puede estar inactivo, consulte con administrador
5. El producto puede no estar creado aún

### 13.5 Los Totales No Cuadran

**Problema:** Los totales de la venta parecen incorrectos

**Verificaciones:**
1. Revise que las cantidades de productos sean correctas
2. Verifique los descuentos aplicados
3. Recuerde que el IVA (19%) se calcula automáticamente
4. El total es: Subtotal + IVA - Descuentos

### 13.6 No Puedo Imprimir la Factura

**Soluciones:**
1. Verifique que su navegador permite ventanas emergentes del sitio
2. Asegúrese de que la impresora está conectada y encendida
3. Use la opción "Guardar como PDF" si la impresora falla
4. Intente abrir la factura en otro navegador

### 13.7 Errores de Permisos

**Problema:** "No tienes permisos para acceder a esta sección"

**Explicación:** Su rol de usuario no permite acceder a esa funcionalidad.

**Soluciones:**
1. Verifique que está en la sección correcta para su rol
2. Si necesita acceso, contacte al administrador
3. Algunas funciones son solo para administradores

---

## 14. CONSEJOS Y MEJORES PRÁCTICAS

### 14.1 Para Eficiencia en Ventas

- Aprenda los atajos de teclado del navegador
- Use la búsqueda por código de barras cuando sea posible
- Mantenga abierta solo la pestaña del sistema
- Registre clientes frecuentes para agilizar ventas futuras

### 14.2 Para Mejor Control de Inventario

- Revise diariamente los productos con stock bajo
- Mantenga actualizados los precios
- Use categorías descriptivas para facilitar búsquedas
- Agregue imágenes a los productos

### 14.3 Para Gestión de Clientes

- Valide los datos del cliente al momento de registro
- Incentive el registro de clientes ofreciendo beneficios
- Use las estadísticas para identificar clientes importantes
- Mantenga actualizados teléfonos y correos

### 14.4 Seguridad

- No comparta su contraseña con nadie
- Cierre sesión al terminar su turno
- No deje la sesión abierta en computadoras públicas
- Cambie su contraseña periódicamente

---

## 15. SOPORTE TÉCNICO

Para soporte técnico o reportar problemas:

- Contacte al administrador del sistema
- Describa el problema con el mayor detalle posible
- Indique en qué sección del sistema ocurre
- Si es posible, tome capturas de pantalla del error

---

## 16. GLOSARIO DE TÉRMINOS

- **Dashboard:** Panel principal con métricas e información resumida
- **Stock:** Cantidad disponible de un producto
- **IVA:** Impuesto al Valor Agregado (19%)
- **Cliente Casual:** Cliente genérico para ventas sin registro específico
- **SKU:** Código único de producto
- **Método de pago mixto:** Combinación de efectivo y otro método
- **Stock mínimo:** Cantidad mínima recomendada en inventario
- **Venta cancelada:** Venta anulada, con stock restaurado

---

## NOTAS FINALES

Este manual será actualizado conforme se agreguen nuevas funcionalidades al sistema. Para versiones actualizadas, consulte con su administrador.

**Desarrollado por:** Marco Antonio Saavedra y Emanuel
**Versión del Manual:** 1.0
**Fecha:** Noviembre 2024

---

FIN DEL MANUAL DE USUARIO
