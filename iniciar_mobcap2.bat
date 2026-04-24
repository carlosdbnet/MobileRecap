@echo off
setlocal enabledelayedexpansion
set BASE_DIR=%~dp0

:menu
cls
echo ========================================
echo     Mobcap - Sistema de Coleta
echo ========================================
echo.
echo  [1] Iniciar Backend (FastAPI)
echo  [2] Iniciar Frontend (Expo)
echo  [3] Iniciar Ambos
echo  [0] Sair
echo.
set /p opcao="Escolha uma opcao: "

if "%opcao%"=="1" goto backend
if "%opcao%"=="2" goto frontend
if "%opcao%"=="3" goto ambos
if "%opcao%"=="0" exit
goto menu

:backend
cls
echo ========================================
echo     Iniciando Backend FastAPI...
echo ========================================
cd /d %BASE_DIR%backend
if errorlevel 1 (
    echo ERRO: Pasta backend nao encontrada
    pause
    goto menu
)
echo [1/2] Obtendo IP Local para configuracao...
for /f "tokens=*" %%i in ('python ..\get_ip.py') do set LOCAL_IP=%%i
echo SEU IP LOCAL E: %LOCAL_IP%
echo.
echo [1/2] Iniciando Backend na porta 8082...
start "Mobcap Backend" cmd /k "cd /d %BASE_DIR%backend && venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8082"
goto menu

:frontend
cls
echo ========================================
echo     Iniciando Frontend Expo...
echo ========================================
echo Use o Expo Go no celular e escaneie o QR Code
start "Mobcap Frontend" cmd /k "cd /d %BASE_DIR%frontend && npx expo start"
goto menu

:ambos
cls
echo ========================================
echo     Iniciando Backend e Frontend...
echo ========================================
echo [1/2] Obtendo IP Local para configuracao...
for /f "tokens=*" %%i in ('python get_ip.py') do set LOCAL_IP=%%i
echo SEU IP LOCAL E: %LOCAL_IP%
echo.
echo [1/2] Iniciando Backend na porta 8082...
start "Mobcap Backend" cmd /k "cd /d %BASE_DIR%backend && venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8082"

timeout /t 5 /nobreak >nul
echo Use o Expo Go no celular e escaneie o QR Code
start "Mobcap Frontend" cmd /k "cd /d %BASE_DIR%frontend && npx expo start"
pause
goto menu
