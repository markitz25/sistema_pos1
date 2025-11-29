# API de Clientes

Todas las rutas requieren sesión iniciada. La búsqueda está disponible para administradores y trabajadores.

## Búsqueda rápida de clientes (AJAX)
- **GET** `/clientes/buscar-ajax/`
- **Query params**:
  - `q` (obligatorio): texto a buscar en nombre, cédula o teléfono. En UI se espera al menos 2 caracteres.
- **Respuesta 200 (ejemplo)**
```json
{
  "clientes": [
    {
      "id": 5,
      "nombre": "Ana Pérez",
      "cedula": "12345678",
      "telefono": "3001234567",
      "correo": "ana@example.com"
    }
  ]
}
```
- **Notas**:
  - Solo devuelve clientes activos.
  - Si `q` es muy corto, puede devolver lista vacía.
  - Si no hay sesión, redirige a `/login/` (302).

## Rutas HTML relacionadas (para contexto, no JSON)
- Estadísticas de clientes: `/clientes/estadisticas/`

