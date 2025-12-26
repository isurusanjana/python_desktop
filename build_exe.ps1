# PowerShell script to build a single-file Windows executable with PyInstaller
# Run: .\build_exe.ps1 from repository root (unblock the file if needed)
param()

$python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
    $python = "python"
}

Write-Host "Installing/upgrading PyInstaller..."
& $python -m pip install --upgrade pyinstaller | Out-Null

# Optional icon path (relative to project root). Create assets\app.ico to include an icon.
$icon = Join-Path $PSScriptRoot "assets\app.ico"

# Use main.py by default
$entrypoint = "main.py"

if (Test-Path $icon) {
    Write-Host "Found icon at $icon — building with icon"
    pyinstaller --onefile --windowed --noconfirm --clean --name "PythonDesktopApp" --icon "$icon" $entrypoint
} else {
    Write-Host "No icon found at $icon — building without icon"
    pyinstaller --onefile --windowed --noconfirm --clean --name "PythonDesktopApp" $entrypoint
}

Write-Host "Build finished. See the dist\\ directory." -ForegroundColor Green
Pause
