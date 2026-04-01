@echo off
title MobCap System - Backend & Frontend
echo ==========================================
echo    INICIANDO SISTEMA MOBCAP (FastAPI + Expo)
echo ==========================================

:: Iniciando o Backend em uma nova janela
echo [1/2] Iniciando Backend na porta 8000...
start "MobCap Backend" cmd /k "cd backend && python -m uvicorn main:app --host 0.0.0.0 --port 8000"

:: Iniciando o Frontend em uma nova janela
echo [2/2] Iniciando Frontend Expo...
start "MobCap Frontend" cmd /k "cd frontend && npx expo start"

echo.
echo ==========================================
echo    SISTEMA INICIADO COM SUCESSO!
echo    Verifique as janelas abertas para os logs.
echo ==========================================
pause
