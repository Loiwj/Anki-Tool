# Script dong goi AnkiTool thanh file phan phoi
param(
    [string]$Version = "1.0"
)

$PackageName = "AnkiTool-v$Version"
$DistPath = "dist"
$PackagePath = "$PackageName.zip"

Write-Host "Dang dong goi AnkiTool v$Version..." -ForegroundColor Green

# Kiem tra thu muc dist co ton tai
if (-not (Test-Path $DistPath)) {
    Write-Host "Loi: Khong tim thay thu muc dist. Vui long build ung dung truoc." -ForegroundColor Red
    exit 1
}

# Xoa file zip cu neu co
if (Test-Path $PackagePath) {
    Remove-Item $PackagePath -Force
    Write-Host "Da xoa file zip cu" -ForegroundColor Yellow
}

# Tao file zip
try {
    Compress-Archive -Path "$DistPath\*" -DestinationPath $PackagePath -Force
    Write-Host ""
    Write-Host "=======================================" -ForegroundColor Green
    Write-Host "DONG GOI THANH CONG!" -ForegroundColor Green
    Write-Host "=======================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "File da tao: $PackagePath" -ForegroundColor Cyan
    Write-Host "Kich thuoc: $([math]::Round((Get-Item $PackagePath).Length / 1MB, 2)) MB" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Noi dung package:" -ForegroundColor Yellow
    Get-ChildItem $DistPath | ForEach-Object {
        if ($_.PSIsContainer) {
            Write-Host "  📁 $($_.Name)/" -ForegroundColor Blue
        } else {
            Write-Host "  📄 $($_.Name)" -ForegroundColor White
        }
    }
    Write-Host ""
    Write-Host "Package san sang de phan phoi!" -ForegroundColor Green
} catch {
    Write-Host "Loi khi tao file zip: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

Read-Host "Press Enter to continue"
