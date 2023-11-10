import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": [],
    "includes": [],
    "zip_include_packages": ["encodings", "PySide6"],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="MecChat Voice Assistent",
    version="1.0",
    description="MecChat Voice Assistente Virtual Especializado. MecChat foi desenvolvido pela equipe de desenvolvedores da empresa Mecânica Total Brasil, utilizando tecnologia várias tecnologias para fornecer soluções, orientações e sugestões claras e objetivas para resolução de problemas mecânicos. Este ADD-ON adiciona a funcionalidade de assistente de voz a plataforma principal que é uma ferramenta poderosa para suporte técnico e assistência na área mecânica.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)

# cxfreeze -c main.py --target-dir dist --target-name MecChat-Voice-Assistent 