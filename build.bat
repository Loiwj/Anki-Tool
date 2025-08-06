@echo off
echo Building AnkiTool application...
echo.

REM Clean previous build
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

REM Build the application
pyinstaller ankitool.spec

REM Check if build was successful
if exist "dist\AnkiTool.exe" (
    echo.
    echo ========================================
    echo BUILD SUCCESSFUL!
    echo ========================================
    echo.
    echo Executable file created: dist\AnkiTool.exe
    echo You can run the application by double-clicking AnkiTool.exe
    echo.
    echo Note: Make sure to create a .env file with your GEMINI_API_KEYS
    echo in the same folder as AnkiTool.exe before running it.
    echo.
) else (
    echo.
    echo ========================================
    echo BUILD FAILED!
    echo ========================================
    echo Please check the error messages above.
)

pause
