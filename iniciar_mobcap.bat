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
echo  [2] Iniciar Frontend (Expo - LAN)
echo  [3] Iniciar Frontend (Expo - TUNNEL) ^<-- Recomendado se o QR Code falhar
echo  [4] Iniciar Ambos (LAN)
echo  [5] Iniciar Ambos (TUNNEL)
echo  [0] Sair
echo.
set /p opcao="Escolha uma opcao: "

if "%opcao%"=="1" goto backend
if "%opcao%"=="2" goto frontend_lan
if "%opcao%"=="3" goto frontend_tunnel
if "%opcao%"=="4" goto ambos_lan
if "%opcao%"=="5" goto ambos_tunnel
if "%opcao%"=="0" exit
goto menu

:backend
cls
echo ========================================
echo     Iniciando Backend FastAPI...
echo ========================================
echo [1/2] Obtendo IP Local...
for /f "tokens=*" %%i in ('python get_ip.py') do set LOCAL_IP=%%i
echo SEU IP LOCAL E: %LOCAL_IP%
echo.
echo [2/2] Iniciando Backend na porta 8082...
start "Mobcap Backend" cmd /k "cd /d %BASE_DIR%backend && venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8082"
goto menu

:frontend_lan
cls
echo ========================================
echo     Iniciando Frontend Expo (LAN)...
echo ========================================
echo Forcando IP: 192.168.15.98
set EXPO_PACKAGER_PROXY_URL=
set REACT_NATIVE_PACKAGER_HOSTNAME=192.168.15.98
echo Use o Expo Go no celular e escaneie o QR Code
start "Mobcap Frontend" cmd /k "cd /d %BASE_DIR%frontend && npx expo start"
goto menu

:frontend_tunnel
cls
echo ========================================
echo     Iniciando Frontend Expo (TUNNEL)...
echo ========================================
echo AGUARDE: Criando túnel seguro...
echo Se for a primeira vez, pode ser solicitado instalar @expo/ngrok.
start "Mobcap Frontend" cmd /k "cd /d %BASE_DIR%frontend && npx expo start --tunnel"
goto menu

:ambos_lan
cls
echo ========================================
echo     Iniciando Backend e Frontend (LAN)...
echo ========================================
for /f "tokens=*" %%i in ('python get_ip.py') do set LOCAL_IP=%%i
echo SEU IP LOCAL E: %LOCAL_IP%
set REACT_NATIVE_PACKAGER_HOSTNAME=192.168.15.98
echo.
echo [1/2] Iniciando Backend na porta 8082...
start "Mobcap Backend" cmd /k "cd /d %BASE_DIR%backend && venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8082"

:wait_backend_lan
echo Aguardando Backend iniciar na porta 8082...
timeout /t 2 /nobreak >nul
netstat -ano | findstr LISTENING | findstr :8082 >nul
if errorlevel 1 goto wait_backend_lan

echo.
echo [2/2] Backend detectado! Iniciando Frontend Expo...
start "Mobcap Frontend" cmd /k "cd /d %BASE_DIR%frontend && npx expo start"
goto menu

:ambos_tunnel
cls
echo ========================================
echo     Iniciando Backend e Frontend (TUNNEL)...
echo ========================================
for /f "tokens=*" %%i in ('python get_ip.py') do set LOCAL_IP=%%i
echo SEU IP LOCAL E: %LOCAL_IP%
echo.
echo [1/2] Iniciando Backend na porta 8082...
start "Mobcap Backend" cmd /k "cd /d %BASE_DIR%backend && venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8082"

:wait_backend_tunnel
echo Aguardando Backend iniciar na porta 8082...
timeout /t 2 /nobreak >nul
netstat -ano | findstr LISTENING | findstr :8082 >nul
if errorlevel 1 goto wait_backend_tunnel

echo.
echo [2/2] Backend detectado! Iniciando Frontend Expo (TUNNEL)...
start "Mobcap Frontend" cmd /k "cd /d %BASE_DIR%frontend && npx expo start --tunnel"
goto menu
