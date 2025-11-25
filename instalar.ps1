# ========================================
# SCRIPT DE INSTALACIÓN AUTOMÁTICA
# Sistema POS - Versión Corregida
# ========================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "SISTEMA POS - INSTALACIÓN AUTOMÁTICA" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar ubicación
$ruta = Get-Location
Write-Host "📁 Ruta actual: $ruta" -ForegroundColor Yellow
Write-Host ""

$confirmar = Read-Host "¿Estás en el directorio raíz del proyecto? (S/N)"
if ($confirmar -ne "S" -and $confirmar -ne "s") {
    Write-Host "❌ Por favor, navega al directorio del proyecto primero" -ForegroundColor Red
    exit
}

# PASO 1: Crear respaldo
Write-Host ""
Write-Host "📦 PASO 1: Creando respaldo..." -ForegroundColor Green
$fecha = Get-Date -Format "yyyyMMdd_HHmmss"
$nombreBackup = "backup_$fecha"

if (Test-Path "../$nombreBackup") {
    Write-Host "⚠️ El respaldo ya existe" -ForegroundColor Yellow
} else {
    Copy-Item -Path . -Destination "../$nombreBackup" -Recurse -Force
    Write-Host "✅ Respaldo creado: ../$nombreBackup" -ForegroundColor Green
}

# PASO 2: Eliminar archivos innecesarios
Write-Host ""
Write-Host "🗑️ PASO 2: Eliminando archivos innecesarios..." -ForegroundColor Green

$archivos = @(
    "corregir_todas_urls.py",
    "corregir_todo.py",
    "corregir_urls_completo.py",
    "corregir_visualizacion_productos.py",
    "crear_clientes_prueba.py",
    "crear_datos_completos.py",
    "crear_datos_prueba.py",
    "crear_template_ventas.py",
    "diagnostico_completo.py",
    "verificar_archivos.py",
    "templates\base copy.html",
    "ventas\views copy.py"
)

$eliminados = 0
foreach ($archivo in $archivos) {
    if (Test-Path $archivo) {
        Remove-Item $archivo -Force
        Write-Host "  ✓ Eliminado: $archivo" -ForegroundColor Gray
        $eliminados++
    }
}

# Eliminar carpeta dashboard
if (Test-Path "templates\dashboard") {
    Remove-Item -Path "templates\dashboard" -Recurse -Force
    Write-Host "  ✓ Eliminada carpeta: templates\dashboard" -ForegroundColor Gray
    $eliminados++
}

Write-Host "✅ $eliminados archivos/carpetas eliminados" -ForegroundColor Green

# PASO 3: Información de archivos a copiar
Write-Host ""
Write-Host "📋 PASO 3: Archivos a actualizar manualmente:" -ForegroundColor Green
Write-Host ""
Write-Host "Copia estos archivos desde la carpeta CORREGIDO:" -ForegroundColor Yellow
Write-Host "  1. reportes/urls.py" -ForegroundColor White
Write-Host "  2. reportes/views.py" -ForegroundColor White
Write-Host "  3. autenticacion/views.py" -ForegroundColor White
Write-Host "  4. ventas/views.py" -ForegroundColor White
Write-Host "  5. templates/base.html" -ForegroundColor White
Write-Host "  6. templates/ventas/punto_venta.html" -ForegroundColor White
Write-Host "  7. tablero/templates/tablero/dashboard_admin.html" -ForegroundColor White
Write-Host "  8. tablero/templates/tablero/dashboard_trabajador.html" -ForegroundColor White
Write-Host ""

$continuar = Read-Host "¿Has copiado todos los archivos? (S/N)"
if ($continuar -ne "S" -and $continuar -ne "s") {
    Write-Host "⚠️ Por favor, copia los archivos antes de continuar" -ForegroundColor Yellow
    exit
}

# PASO 4: Verificar requirements
Write-Host ""
Write-Host "📦 PASO 4: Verificando dependencias..." -ForegroundColor Green

if (Test-Path ".venv\Scripts\activate") {
    Write-Host "✅ Entorno virtual encontrado" -ForegroundColor Green
    
    $instalar = Read-Host "¿Instalar/actualizar dependencias? (S/N)"
    if ($instalar -eq "S" -or $instalar -eq "s") {
        & .venv\Scripts\pip.exe install -r requirements.txt
        Write-Host "✅ Dependencias instaladas" -ForegroundColor Green
    }
} else {
    Write-Host "⚠️ No se encontró entorno virtual" -ForegroundColor Yellow
    Write-Host "Ejecuta: python -m venv .venv" -ForegroundColor White
}

# PASO 5: Verificar trabajador admin
Write-Host ""
Write-Host "👤 PASO 5: Verificación de trabajador admin..." -ForegroundColor Green
Write-Host "Ejecutando verificación..." -ForegroundColor Yellow

$scriptPython = @"
from django.contrib.auth.models import User
from trabajadores.models import Trabajador

try:
    user = User.objects.get(username='admin1')
    print(f'Usuario encontrado: {user.username}')
    
    try:
        trabajador = user.trabajador
        print(f'✅ Trabajador existe: {trabajador.rol}')
    except Exception:
        print('Creando trabajador admin...')
        Trabajador.objects.create(
            usuario=user,
            rol='admin',
            nombre='Admin',
            apellido='Sistema',
            activo=True
        )
        print('✅ Trabajador admin creado')
except Exception as e:
    print(f'Error: {e}')
"@

# IMPORTANTE: canalizar el bloque al intérprete de Python
$scriptPython | & .venv\Scripts\python.exe manage.py shell

# PASO 6: Instrucciones finales
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "✅ INSTALACIÓN COMPLETADA" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "🚀 Próximos pasos:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Iniciar servidor:" -ForegroundColor White
Write-Host "   python manage.py runserver" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Abrir navegador:" -ForegroundColor White
Write-Host "   http://localhost:8000" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Credenciales de prueba:" -ForegroundColor White
Write-Host "   Usuario: admin1" -ForegroundColor Gray
Write-Host "   Contraseña: admin123" -ForegroundColor Gray
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$iniciar = Read-Host "¿Iniciar servidor ahora? (S/N)"
if ($iniciar -eq "S" -or $iniciar -eq "s") {
    Write-Host ""
    Write-Host "🚀 Iniciando servidor..." -ForegroundColor Green
    Write-Host "Presiona Ctrl+C para detener" -ForegroundColor Yellow
    Write-Host ""
    & .venv\Scripts\python.exe manage.py runserver
}

Write-Host ""
Write-Host "¡Gracias por usar el Sistema POS! 🎉" -ForegroundColor Cyan
