@echo off
title MobCap System - Gerador de APK
echo ==========================================
echo    MOBCAP: INICIANDO GERACAO DE APK
echo ==========================================
echo.
echo [1/3] Entrando na pasta frontend...
cd frontend

echo [2/3] Verificando login no Expo EAS...
call npx eas-cli whoami
if %errorlevel% neq 0 (
    echo.
    echo ERRO: Voce nao esta logado no Expo EAS.
    echo Por favor, execute 'npx eas-cli login' antes do build.
    pause
    exit /b
)

echo.
echo [3/3] Iniciando Build do APK (Perfil Preview)...
echo Isso vai gerar um novo APK nos servidores da Expo.
echo O processo geralmente leva de 5 a 10 minutos.
echo Ao finalizar, você receberá um QR Code e um link para download.
echo.
call npx eas-cli build --platform android --profile preview

echo.
echo ==========================================
echo    PROCESSO DE BUILD FINALIZADO!
echo ==========================================
pause
