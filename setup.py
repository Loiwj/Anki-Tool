import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine-tuning
build_exe_options = {
    "packages": [
        "tkinter", 
        "ttkthemes", 
        "requests", 
        "google.generativeai",
        "dotenv",
        "os",
        "json",
        "threading",
        "queue",
        "time",
        "webbrowser",
        "urllib.parse"
    ],
    "include_files": [
        ("assets/", "assets/"),  # Include assets folder
    ],
    "excludes": [
        "unittest",
        "email",
        "http",
        "xmlrpc",
        "pdb",
        "difflib",
        "inspect",
        "calendar",
        "doctest"
    ]
}

# GUI applications require a different base on Windows (the default is for console applications).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="AnkiTool",
    version="1.0",
    description="Anki Learning Tool with AI Support",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "main.py", 
            base=base, 
            target_name="AnkiTool.exe",
            icon="assets/icon.ico"
        )
    ]
)
