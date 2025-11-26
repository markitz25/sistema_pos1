# 04. PRUEBAS UNITARIAS

Esta carpeta contiene el plan completo de pruebas unitarias del Sistema POS.

## Archivo Incluido

### matriz_pruebas_unitarias.md
Plan exhaustivo de pruebas que incluye:

#### 1. Introducción a Pruebas Unitarias
- Concepto y beneficios
- Marco de pruebas (Django TestCase, unittest, etc.)
- Herramientas utilizadas

#### 2. Pruebas por Módulo

**Módulo Autenticación (12 casos de prueba)**
- Pruebas de autenticación (AUTH-01 a AUTH-09)
- Pruebas de autorización (AUTH-10 a AUTH-12)

**Módulo Trabajadores (10 casos de prueba)**
- Pruebas de modelo (TRAB-01 a TRAB-04)
- Pruebas de vistas (TRAB-05 a TRAB-10)

**Módulo Clientes (15 casos de prueba)**
- Pruebas de modelo (CLI-01 a CLI-08)
- Pruebas de vistas (CLI-09 a CLI-15)

**Módulo Inventario (14 casos de prueba)**
- Pruebas de categoría (INV-01 a INV-02)
- Pruebas de producto (INV-03 a INV-07)
- Pruebas de vistas (INV-08 a INV-14)

**Módulo Ventas (20 casos de prueba)**
- Pruebas de modelo Venta (VTA-01 a VTA-06)
- Pruebas de DetalleVenta (VTA-07 a VTA-09)
- Pruebas de vistas (VTA-10 a VTA-20)

**Módulo Tablero (8 casos de prueba)**
- Pruebas de dashboard (DASH-01 a DASH-05)
- Pruebas de APIs (DASH-06 a DASH-08)

**Módulo Reportes (7 casos de prueba)**
- Pruebas de reportes (REP-01 a REP-07)

**Pruebas de Integración (4 casos de prueba)**
- Flujos completos end-to-end (INT-01 a INT-04)

**Total: 100+ casos de prueba definidos**

#### 3. Métricas de Cobertura
- Objetivos de cobertura por módulo
- Cómo medir cobertura con coverage.py
- Comandos de ejecución

#### 4. Implementación
- Estructura de archivos de prueba
- Ejemplos de código de pruebas
- Convenciones y mejores prácticas

#### 5. Ejecución de Pruebas
- Comandos para ejecutar pruebas
- Configuración para pruebas
- Tips de ejecución

#### 6. Referencias
Incluye enlaces a:
- Testing in Django (documentación oficial)
- IBM Unit Testing Best Practices
- Microsoft Testing Guide
- AWS Unit Testing
- BrowserStack Guide
- TestGen-LLM y otras herramientas

#### 7. Cronograma de Implementación
Plan de 18 días para implementar todas las pruebas

## Estado Actual
- Casos de prueba: Definidos (pendientes de implementación)
- Cobertura objetivo: 80% del código
- Estado: En desarrollo

## Desarrollado por
Marco Antonio Saavedra y Emanuel
Noviembre 2024
