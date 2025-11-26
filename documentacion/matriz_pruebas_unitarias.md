# MATRIZ DE PRUEBAS UNITARIAS - SISTEMA POS

**Desarrollado por:** Marco Antonio Saavedra y Emanuel

---

## 1. INTRODUCCIÓN A PRUEBAS UNITARIAS

Las pruebas unitarias son componentes fundamentales en el desarrollo de software que verifican el correcto funcionamiento de unidades individuales de código. En el contexto del Sistema POS, cada módulo, función y método debe ser probado de manera aislada para garantizar su comportamiento esperado.

### Beneficios de las Pruebas Unitarias:

- Detección temprana de errores
- Facilita refactorización segura
- Documenta el comportamiento esperado
- Reduce costos de mantenimiento
- Mejora la calidad del código

---

## 2. MARCO DE PRUEBAS

### 2.1 Herramientas Utilizadas

| Herramienta | Propósito |
|---|---|
| Django TestCase | Framework de pruebas de Django |
| Python unittest | Biblioteca estándar de pruebas |
| Django Client | Simulación de requests HTTP |
| Factory Boy | Generación de datos de prueba |

### 2.2 Convenciones de Pruebas

- Archivos de prueba: `tests.py` en cada módulo
- Nomenclatura: `test_nombre_descriptivo()`
- Estructura: Arrange-Act-Assert
- Cobertura mínima: 80% del código

---

## 3. MÓDULO: AUTENTICACIÓN

### 3.1 Pruebas de Autenticación

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| AUTH-01 | test_login_exitoso | Login con credenciales válidas | username: admin, password: admin123 | Redirección a dashboard, sesión creada | Pendiente |
| AUTH-02 | test_login_credenciales_invalidas | Login con contraseña incorrecta | username: admin, password: wrong | Mensaje de error, sin sesión | Pendiente |
| AUTH-03 | test_login_usuario_inexistente | Login con usuario que no existe | username: noexiste, password: test | Mensaje de error, sin sesión | Pendiente |
| AUTH-04 | test_logout | Cerrar sesión correctamente | Usuario autenticado | Sesión eliminada, redirección a login | Pendiente |
| AUTH-05 | test_cambio_contrasena_exitoso | Cambiar contraseña con datos válidos | old: pass123, new: newpass123 | Contraseña actualizada, mensaje éxito | Pendiente |
| AUTH-06 | test_cambio_contrasena_incorrecta | Cambiar contraseña con anterior incorrecta | old: wrong, new: newpass | Error, contraseña no cambia | Pendiente |
| AUTH-07 | test_setup_primer_admin | Crear primer administrador | datos completos | Admin creado, redirección login | Pendiente |
| AUTH-08 | test_redireccion_segun_rol_admin | Login admin redirige correctamente | rol: admin | Redirección dashboard_admin | Pendiente |
| AUTH-09 | test_redireccion_segun_rol_trabajador | Login trabajador redirige correctamente | rol: trabajador | Redirección dashboard_trabajador | Pendiente |

### 3.2 Pruebas de Autorización

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| AUTH-10 | test_acceso_sin_autenticacion | Acceder vista protegida sin login | No autenticado | Redirección a login | Pendiente |
| AUTH-11 | test_trabajador_acceso_admin | Trabajador intenta acceder función admin | rol: trabajador | Mensaje error permisos, acceso denegado | Pendiente |
| AUTH-12 | test_admin_acceso_todas_vistas | Admin puede acceder todas las vistas | rol: admin | Acceso permitido a todas | Pendiente |

---

## 4. MÓDULO: TRABAJADORES

### 4.1 Pruebas de Modelo Trabajador

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| TRAB-01 | test_crear_trabajador | Crear trabajador válido | datos completos | Trabajador creado en BD | Pendiente |
| TRAB-02 | test_trabajador_str | Método __str__ del modelo | trabajador existente | Retorna nombre completo | Pendiente |
| TRAB-03 | test_trabajador_activo_default | Campo activo por defecto | nuevo trabajador | activo=True | Pendiente |
| TRAB-04 | test_relacion_usuario | Relación OneToOne con User | trabajador con user | Relación correcta | Pendiente |

### 4.2 Pruebas de Vistas Trabajadores

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| TRAB-05 | test_crear_trabajador_admin | Admin crea trabajador | datos válidos, rol admin | Trabajador creado, mensaje éxito | Pendiente |
| TRAB-06 | test_crear_trabajador_sin_permisos | Trabajador intenta crear otro | datos válidos, rol trabajador | Acceso denegado | Pendiente |
| TRAB-07 | test_editar_trabajador | Editar datos de trabajador | datos modificados | Trabajador actualizado | Pendiente |
| TRAB-08 | test_listar_trabajadores | Ver lista de trabajadores | request autenticado | Lista mostrada correctamente | Pendiente |
| TRAB-09 | test_toggle_estado_trabajador | Activar/desactivar trabajador | trabajador_id | Estado cambiado correctamente | Pendiente |
| TRAB-10 | test_buscar_trabajador | Búsqueda por nombre | query: "Juan" | Trabajadores encontrados | Pendiente |

---

## 5. MÓDULO: CLIENTES

### 5.1 Pruebas de Modelo Cliente

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| CLI-01 | test_crear_cliente | Crear cliente válido | datos completos | Cliente creado en BD | Pendiente |
| CLI-02 | test_cedula_unica | Validar unicidad de cédula | cédula duplicada | Error de validación | Pendiente |
| CLI-03 | test_correo_unico | Validar unicidad de correo | correo duplicado | Error de validación | Pendiente |
| CLI-04 | test_actualizar_total_compras | Método actualizar_total_compras() | cliente con ventas | total_compras actualizado | Pendiente |
| CLI-05 | test_get_numero_compras | Método get_numero_compras() | cliente con 5 ventas | Retorna 5 | Pendiente |
| CLI-06 | test_cliente_frecuente | Método es_cliente_frecuente() | cliente con 10+ ventas | Retorna True | Pendiente |
| CLI-07 | test_promedio_compra | Método get_promedio_compra() | cliente con ventas | Promedio calculado correctamente | Pendiente |
| CLI-08 | test_validacion_telefono | Validar formato teléfono | teléfono inválido | Error de validación | Pendiente |

### 5.2 Pruebas de Vistas Clientes

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| CLI-09 | test_crear_cliente_exitoso | Crear cliente con datos válidos | datos completos | Cliente creado, mensaje éxito | Pendiente |
| CLI-10 | test_crear_cliente_cedula_duplicada | Crear con cédula existente | cédula duplicada | Error, cliente no creado | Pendiente |
| CLI-11 | test_editar_cliente | Editar datos de cliente | datos modificados | Cliente actualizado | Pendiente |
| CLI-12 | test_listar_clientes | Ver lista de clientes | request autenticado | Lista mostrada | Pendiente |
| CLI-13 | test_buscar_cliente_ajax | Búsqueda AJAX por nombre | query: "María" | JSON con resultados | Pendiente |
| CLI-14 | test_estadisticas_clientes | Ver estadísticas de clientes | request admin | Estadísticas calculadas | Pendiente |
| CLI-15 | test_toggle_estado_cliente | Activar/desactivar cliente | cliente_id | Estado cambiado | Pendiente |

---

## 6. MÓDULO: INVENTARIO

### 6.1 Pruebas de Modelo Categoria

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| INV-01 | test_crear_categoria | Crear categoría válida | nombre, descripción | Categoría creada | Pendiente |
| INV-02 | test_categoria_str | Método __str__ | categoría existente | Retorna nombre | Pendiente |

### 6.2 Pruebas de Modelo Producto

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| INV-03 | test_crear_producto | Crear producto válido | datos completos | Producto creado | Pendiente |
| INV-04 | test_codigo_barras_unico | Validar unicidad código barras | código duplicado | Error de validación | Pendiente |
| INV-05 | test_stock_minimo_default | Valor default stock_minimo | nuevo producto | stock_minimo=10 | Pendiente |
| INV-06 | test_relacion_categoria | ForeignKey a Categoria | producto con categoría | Relación correcta | Pendiente |
| INV-07 | test_precio_positivo | Validar precio mayor a 0 | precio=-10 | Error de validación | Pendiente |

### 6.3 Pruebas de Vistas Inventario

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| INV-08 | test_agregar_producto_admin | Admin crea producto | datos válidos | Producto creado | Pendiente |
| INV-09 | test_agregar_producto_sin_permisos | Trabajador intenta crear | datos válidos | Acceso denegado | Pendiente |
| INV-10 | test_editar_producto | Editar datos de producto | datos modificados | Producto actualizado | Pendiente |
| INV-11 | test_lista_productos | Ver lista de productos | request autenticado | Lista mostrada | Pendiente |
| INV-12 | test_buscar_producto_ajax | Búsqueda AJAX | query: "arroz" | JSON con productos | Pendiente |
| INV-13 | test_crear_categoria_ajax | Crear categoría rápida | nombre categoría | JSON con nueva categoría | Pendiente |
| INV-14 | test_filtrar_por_categoria | Filtrar productos | categoria_id | Productos filtrados | Pendiente |

---

## 7. MÓDULO: VENTAS

### 7.1 Pruebas de Modelo Venta

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| VTA-01 | test_crear_venta | Crear venta válida | datos completos | Venta creada | Pendiente |
| VTA-02 | test_calcular_totales | Método calcular_totales() | venta con productos | Totales correctos | Pendiente |
| VTA-03 | test_get_numero_productos | Método get_numero_productos() | venta con 3 productos | Retorna 3 | Pendiente |
| VTA-04 | test_cancelar_venta | Método cancelar_venta() | venta completada | Estado=cancelada, stock restaurado | Pendiente |
| VTA-05 | test_calculo_iva | Cálculo IVA 19% | subtotal=100 | impuesto=19 | Pendiente |
| VTA-06 | test_aplicar_descuento | Aplicar descuento | total=100, desc=10 | total_final=90 | Pendiente |

### 7.2 Pruebas de Modelo DetalleVenta

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| VTA-07 | test_crear_detalle | Crear detalle de venta | venta, producto, cantidad | Detalle creado | Pendiente |
| VTA-08 | test_calculo_subtotal_auto | Subtotal calculado en save() | cantidad=5, precio=10 | subtotal=50 | Pendiente |
| VTA-09 | test_actualizar_inventario | Actualización de stock | producto con stock=100, venta=10 | stock=90 | Pendiente |

### 7.3 Pruebas de Vistas Ventas

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| VTA-10 | test_punto_venta_view | Acceder punto de venta | request autenticado | Vista mostrada | Pendiente |
| VTA-11 | test_procesar_venta_exitosa | Procesar venta completa | productos, cliente, pago | Venta creada, stock actualizado | Pendiente |
| VTA-12 | test_venta_sin_stock | Intentar venta sin stock | producto con stock=0 | Error, venta no procesada | Pendiente |
| VTA-13 | test_venta_cliente_casual | Venta sin cliente específico | cliente_id=1 (casual) | Venta con cliente casual | Pendiente |
| VTA-14 | test_cancelar_venta_admin | Admin cancela venta | venta_id, rol admin | Venta cancelada | Pendiente |
| VTA-15 | test_cancelar_venta_sin_permisos | Trabajador intenta cancelar | venta_id, rol trabajador | Acceso denegado | Pendiente |
| VTA-16 | test_listar_ventas_admin | Admin ve todas las ventas | request admin | Todas las ventas | Pendiente |
| VTA-17 | test_listar_ventas_trabajador | Trabajador ve solo sus ventas | request trabajador | Solo ventas propias | Pendiente |
| VTA-18 | test_generar_factura | Generar factura PDF/HTML | venta_id | Factura generada | Pendiente |
| VTA-19 | test_metodos_pago | Probar métodos de pago | efectivo, tarjeta, etc | Guardado correctamente | Pendiente |
| VTA-20 | test_pago_mixto | Venta con pago mixto | efectivo + tarjeta | Registrado correctamente | Pendiente |

---

## 8. MÓDULO: TABLERO

### 8.1 Pruebas de Vistas Dashboard

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| DASH-01 | test_dashboard_admin | Dashboard para admin | request admin | Dashboard completo | Pendiente |
| DASH-02 | test_dashboard_trabajador | Dashboard para trabajador | request trabajador | Dashboard limitado | Pendiente |
| DASH-03 | test_dashboard_redirect | Redirección automática | request autenticado | Redirige según rol | Pendiente |
| DASH-04 | test_metricas_ventas | Calcular métricas de ventas | request con datos | Métricas correctas | Pendiente |
| DASH-05 | test_alertas_stock_bajo | Mostrar alertas stock bajo | productos con stock<10 | Alertas mostradas | Pendiente |

### 8.2 Pruebas de APIs

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| DASH-06 | test_api_ventas_por_mes | API ventas mensuales | request autenticado | JSON con datos 12 meses | Pendiente |
| DASH-07 | test_api_productos_top | API productos más vendidos | request autenticado | JSON top 10 productos | Pendiente |
| DASH-08 | test_api_ventas_categoria | API ventas por categoría | request autenticado | JSON ventas por categoría | Pendiente |

---

## 9. MÓDULO: REPORTES

### 9.1 Pruebas de Reportes

| ID | Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| REP-01 | test_reporte_ventas | Generar reporte de ventas | fechas, filtros | Reporte generado | Pendiente |
| REP-02 | test_reporte_productos | Reporte productos vendidos | request admin | Reporte con datos | Pendiente |
| REP-03 | test_reporte_clientes | Reporte top clientes | request admin | Top clientes listados | Pendiente |
| REP-04 | test_exportar_excel | Exportar ventas a Excel | request admin | Archivo Excel descargado | Pendiente |
| REP-05 | test_filtros_fecha_reporte | Filtrar por rango fechas | fecha_inicio, fecha_fin | Datos filtrados | Pendiente |
| REP-06 | test_filtros_metodo_pago | Filtrar por método pago | metodo=efectivo | Ventas filtradas | Pendiente |
| REP-07 | test_reporte_sin_permisos | Trabajador accede reportes | request trabajador | Acceso denegado | Pendiente |

---

## 10. PRUEBAS DE INTEGRACIÓN

### 10.1 Flujos Completos

| ID | Caso de Prueba | Descripción | Pasos | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| INT-01 | test_flujo_venta_completo | Proceso completo de venta | Login → buscar producto → agregar → seleccionar cliente → procesar | Venta registrada, stock actualizado, cliente actualizado | Pendiente |
| INT-02 | test_flujo_cancelacion_venta | Cancelar venta y verificar | Crear venta → cancelar → verificar stock | Stock restaurado correctamente | Pendiente |
| INT-03 | test_flujo_crear_trabajador | Admin crea y gestiona trabajador | Login admin → crear trabajador → editar → desactivar | Trabajador gestionado correctamente | Pendiente |
| INT-04 | test_flujo_gestion_inventario | Gestión completa inventario | Crear categoría → crear producto → editar → buscar | Inventario gestionado | Pendiente |

---

## 11. MÉTRICAS DE COBERTURA

### 11.1 Objetivos de Cobertura

| Módulo | Objetivo Cobertura | Cobertura Actual | Estado |
|---|---|---|---|
| autenticacion | 85% | Pendiente medición | En desarrollo |
| trabajadores | 80% | Pendiente medición | En desarrollo |
| clientes | 80% | Pendiente medición | En desarrollo |
| inventario | 80% | Pendiente medición | En desarrollo |
| ventas | 90% | Pendiente medición | En desarrollo |
| tablero | 75% | Pendiente medición | En desarrollo |
| reportes | 75% | Pendiente medición | En desarrollo |
| **TOTAL SISTEMA** | **80%** | **Pendiente** | **En desarrollo** |

### 11.2 Cómo Medir Cobertura

Comando para medir cobertura:
```bash
coverage run --source='.' manage.py test
coverage report
coverage html
```

---

## 12. IMPLEMENTACIÓN DE PRUEBAS

### 12.1 Estructura de Archivo de Pruebas

```python
# tests.py en cada módulo

from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import NombreModelo

class NombreModeloTestCase(TestCase):
    def setUp(self):
        # Configuración inicial
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_nombre_descriptivo(self):
        # Arrange: Preparar datos
        dato = "valor"

        # Act: Ejecutar acción
        resultado = funcion_a_probar(dato)

        # Assert: Verificar resultado
        self.assertEqual(resultado, valor_esperado)

    def tearDown(self):
        # Limpieza después de pruebas
        pass
```

### 12.2 Ejemplo: Prueba de Modelo Cliente

```python
# clientes/tests.py

from django.test import TestCase
from .models import Cliente

class ClienteModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Juan Pérez",
            cedula="1234567890",
            correo="juan@example.com",
            telefono="3001234567",
            direccion="Calle 123"
        )

    def test_crear_cliente(self):
        self.assertEqual(self.cliente.nombre, "Juan Pérez")
        self.assertEqual(self.cliente.cedula, "1234567890")
        self.assertTrue(self.cliente.activo)

    def test_cedula_unica(self):
        with self.assertRaises(Exception):
            Cliente.objects.create(
                nombre="María López",
                cedula="1234567890",  # Duplicada
                correo="maria@example.com",
                telefono="3009876543",
                direccion="Calle 456"
            )

    def test_str_method(self):
        self.assertEqual(str(self.cliente), "Juan Pérez")
```

### 12.3 Ejemplo: Prueba de Vista

```python
# ventas/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from trabajadores.models import Trabajador

class PuntoVentaViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='vendedor',
            password='test123'
        )
        self.trabajador = Trabajador.objects.create(
            usuario=self.user,
            rol='trabajador',
            nombre='Test',
            apellido='Vendedor'
        )
        self.client.login(username='vendedor', password='test123')

    def test_punto_venta_accesible(self):
        response = self.client.get(reverse('ventas:punto_venta'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ventas/punto_venta.html')

    def test_punto_venta_sin_auth(self):
        self.client.logout()
        response = self.client.get(reverse('ventas:punto_venta'))
        self.assertEqual(response.status_code, 302)  # Redirect a login
```

---

## 13. EJECUCIÓN DE PRUEBAS

### 13.1 Comandos para Ejecutar Pruebas

```bash
# Ejecutar todas las pruebas
python manage.py test

# Ejecutar pruebas de un módulo específico
python manage.py test clientes

# Ejecutar prueba específica
python manage.py test clientes.tests.ClienteModelTest.test_crear_cliente

# Ejecutar con verbosidad
python manage.py test --verbosity=2

# Mantener base de datos después de pruebas
python manage.py test --keepdb
```

### 13.2 Configuración para Pruebas

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # BD en memoria para pruebas
    }
}

# Configuración específica para pruebas
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
```

---

## 14. REFERENCIAS

- Testing in Django: https://docs.djangoproject.com/en/4.2/topics/testing/
- Unit Testing Best Practices: https://www.ibm.com/think/insights/unit-testing-best-practices
- TestGen-LLM: https://www.freecodecamp.org/news/automated-unit-testing-with-testgen-llm-and-cover-agent/
- Software Testing Guide: https://www.testingit.com.mx/blog/pruebas-unitarias-de-software
- Microsoft Testing Guide: https://learn.microsoft.com/es-es/visualstudio/test/unit-test-basics
- AWS Unit Testing: https://aws.amazon.com/es/what-is/unit-testing/
- BrowserStack Guide: https://www.browserstack.com/guide/unit-testing-a-detailed-guide
- Softtek Testing Blog: https://blog.softtek.com/es/testing-unitario

---

## 15. CRONOGRAMA DE IMPLEMENTACIÓN

| Fase | Módulo | Duración Estimada | Responsable |
|---|---|---|---|
| Fase 1 | autenticacion | 2 días | Equipo desarrollo |
| Fase 2 | clientes | 2 días | Equipo desarrollo |
| Fase 3 | inventario | 2 días | Equipo desarrollo |
| Fase 4 | ventas | 3 días | Equipo desarrollo |
| Fase 5 | trabajadores | 2 días | Equipo desarrollo |
| Fase 6 | tablero | 2 días | Equipo desarrollo |
| Fase 7 | reportes | 2 días | Equipo desarrollo |
| Fase 8 | Integración | 3 días | Equipo desarrollo |
| **TOTAL** | | **18 días** | |

---

**Elaborado por:** Marco Antonio Saavedra y Emanuel
**Fecha:** Noviembre 2024

**Notas:**
- Todas las pruebas están pendientes de implementación
- Se recomienda implementación incremental por módulo
- Mantener cobertura mínima del 80% en código crítico
- Ejecutar pruebas antes de cada commit en producción
