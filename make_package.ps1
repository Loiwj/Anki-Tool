param([string]$Version = "1.0")

$PackageName = "AnkiTool-v$Version"
$PackagePath = "$PackageName.zip"

Write-Host "Creating package: $PackageName" -ForegroundColor Green

if (Test-Path $PackagePath) {
    Remove-Item $PackagePath -Force
}

Compress-Archive -Path "dist\*" -DestinationPath $PackagePath -Force

Write-Host "Package created: $PackagePath" -ForegroundColor Green
Write-Host "Size: $([math]::Round((Get-Item $PackagePath).Length / 1MB, 2)) MB" -ForegroundColor Cyan

Read-Host "Press Enter to continue"
