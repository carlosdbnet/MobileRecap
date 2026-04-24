@echo off
title MobCap System - Backend & Frontend
set BASE_DIR=%~dp0
echo ==========================================
echo    INICIANDO SISTEMA MOBCAP (FastAPI + Expo)
echo    Diretorio: %BASE_DIR%
echo ==========================================

:: Iniciando o Backend
echo [1/2] Iniciando Backend na porta 8082 (Venv)...
start "MobCap Backend" cmd /k "cd /d %BASE_DIR%backend && ..\.venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8082"

:: Iniciando o Frontend Expo
echo [2/2] Iniciando Frontend Expo...
start "MobCap Frontend" cmd /k "cd /d %BASE_DIR%frontend && npx expo start"

echo.
echo ==========================================
echo    SISTEMA INICIADO COM SUCESSO!
echo    Use o Expo Go para escanear o QR Code.
echo ==========================================
pause
