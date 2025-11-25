# Script para reemplazar 'tablero:inicio' por 'tablero:inicio' en todos los archivos

Write-Host "🔍 Buscando archivos con 'tablero:inicio'..." -ForegroundColor Yellow

# Obtener todos los archivos Python y HTML
$archivos = Get-ChildItem -Path . -Include *.py,*.html -Recurse -File | Where-Object { 
    $_.FullName -notlike "*\venv\*" -and 
    $_.FullName -notlike "*\migrations\*" 
}

$contador = 0

foreach ($archivo in $archivos) {
    $contenido = Get-Content $archivo.FullName -Raw -Encoding UTF8
    
    if ($contenido -match "tablero:inicio") {
        Write-Host "📝 Corrigiendo: $($archivo.FullName)" -ForegroundColor Cyan
        
        # Reemplazar 'tablero:inicio' por 'tablero:inicio'
        $nuevoContenido = $contenido -replace "tablero:inicio", "tablero:inicio"
        
        # Guardar el archivo
        Set-Content -Path $archivo.FullName -Value $nuevoContenido -Encoding UTF8 -NoNewline
        
        $contador++
    }
}

Write-Host "`n✅ Se corrigieron $contador archivos" -ForegroundColor Green
Write-Host "🚀 Ahora reinicia el servidor con: python manage.py runserver" -ForegroundColor Yellow
