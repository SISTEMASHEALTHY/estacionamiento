import os
import sys
from cx_Freeze import setup, Executable
import pywin32_system32

# Carpeta de PyWin32 con las DLLs
include_files = [os.path.join(pywin32_system32.__path__[0], 'win32print.pyd')]

setup(
    name="MiApp",
    version="1.0",
    description="Mi aplicación Python",
    options={"build_exe": {"include_files": include_files}},
    executables=[Executable("main.py", base="Win32GUI")]
)