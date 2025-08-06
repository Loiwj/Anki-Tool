# Build script for AnkiTool using cx_Freeze
Write-Host "Building AnkiTool application with cx_Freeze..." -ForegroundColor Green
Write-Host ""

# Clean previous build
if (Test-Path "build") {
    Remove-Item -Recurse -Force "build"
}
if (Test-Path "dist") {
    Remove-Item -Recurse -Force "dist"
}

# Build the application
Write-Host "Running cx_Freeze..." -ForegroundColor Yellow
python setup.py build

# Check if build was successful
if (Test-Path "build\exe.win-amd64-3.10\AnkiTool.exe") {
    Write-Host ""
    Write-Host "=======================================" -ForegroundColor Green
    Write-Host "BUILD SUCCESSFUL!" -ForegroundColor Green
    Write-Host "=======================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Executable file created: build\exe.win-amd64-3.10\AnkiTool.exe" -ForegroundColor Cyan
    Write-Host "You can run the application by double-clicking AnkiTool.exe" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Note: Make sure to create a .env file with your GEMINI_API_KEYS" -ForegroundColor Yellow
    Write-Host "in the same folder as AnkiTool.exe before running it." -ForegroundColor Yellow
    Write-Host ""
    
    # Copy the built folder to a more accessible location
    Write-Host "Copying build to 'dist' folder for easier access..." -ForegroundColor Yellow
    Copy-Item -Recurse "build\exe.win-amd64-3.10" "dist"
    Write-Host "Application available at: dist\AnkiTool.exe" -ForegroundColor Cyan
} else {
    Write-Host ""
    Write-Host "=======================================" -ForegroundColor Red
    Write-Host "BUILD FAILED!" -ForegroundColor Red
    Write-Host "=======================================" -ForegroundColor Red
    Write-Host "Please check the error messages above." -ForegroundColor Red
}

Read-Host "Press Enter to continue"
