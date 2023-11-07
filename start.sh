#!/bin/bash

# Dá permissão de execução ao script start.sh
chmod +x start.sh

# Detecta o sistema operacional
case "$(uname -s)" in
  Linux*)
    # Comando para Linux
    python3 __main.py
    ;;
  Darwin*)
    # Comando para macOS
    python3 __main.py
    ;;
  CYGWIN*|MINGW32*|MSYS*|MINGW*)
    # Comando para Windows (Git Bash ou MSYS2)
    python __main.py
    ;;
  *)
    echo "Sistema operacional não suportado"
    exit 1
    ;;
esac
