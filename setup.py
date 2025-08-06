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
        "urllib.parse",
        "urllib3",
        "http.client",
        "http",
        "ssl",
        "socket",
        "calendar",
        "email",
        "inspect",
        "httplib2"
    ],
    "include_files": [
        ("assets/", "assets/"),  # Include assets folder
        ("gui/", "gui/"),       # Include GUI modules
        ("services/", "services/")  # Include services modules
    ],
    "excludes": [
        "unittest",
        "xmlrpc",
        "pdb",
        "difflib",
        "doctest",
        "test"
    ]
}

# GUI applications require a different base on Windows (the default is for console applications).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="AnkiTool",
    version="1.1.0",
    description="Multi-language Anki Learning Tool with AI Support",
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
