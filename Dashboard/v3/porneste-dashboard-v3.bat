@echo off
setlocal

set "DASHBOARD_DIR=%~dp0"
set "PORT=8766"

cd /d "%DASHBOARD_DIR%"

where python >nul 2>nul
if errorlevel 1 (
  echo Python nu a fost gasit in PATH.
  echo Instaleaza Python sau porneste manual cu runtime-ul folosit de Codex.
  pause
  exit /b 1
)

python -c "import yaml" >nul 2>nul
if errorlevel 1 (
  echo Lipseste PyYAML. Rulez instalarea dependintelor din requirements.txt...
  python -m pip install -r requirements.txt
  if errorlevel 1 (
    echo Nu am putut instala dependintele.
    pause
    exit /b 1
  )
)

start "" "http://127.0.0.1:%PORT%"
python server.py --host 127.0.0.1 --port %PORT%

pause
