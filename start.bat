@echo off
setlocal

:: Detecta o sistema operacional
:: Use o comando "ver" para verificar a versão do Windows
:: "Windows_NT" indica que o sistema é Windows
if "%OS%" == "Windows_NT" (
    python __main.py
) else (
    echo "Sistema operacional não suportado"
    exit /b 1
)

endlocal
