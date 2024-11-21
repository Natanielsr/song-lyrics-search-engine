@echo off
REM Script para abrir o Visual Studio Code no diretório atual

set vscode="D:\Program Files\Microsoft VS Code\Code.exe"

if not exist %vscode% (
    echo Visual Studio Code nao foi encontrado no local padrao.
    pause
    exit /b
)

echo Abrindo o projeto no Visual Studio Code...
%vscode% .
exit
