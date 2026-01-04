@echo off
REM Build Windows single-file executable using PyInstaller
REM Usage: run this from project root (double-click or from PowerShell/CMD)
SET SCRIPT_DIR=%~dp0
SET PYTHON=%SCRIPT_DIR%\.venv\Scripts\python.exe
IF NOT EXIST "%PYTHON%" (
	SET PYTHON=python
)

REM Optional icon path (relative to project root). Create assets\app.ico to include an icon.
SET ICON=%SCRIPT_DIR%assets\app.ico
echo Installing/ensuring PyInstaller is available...
%PYTHON% -m pip install --upgrade pyinstaller >nul

REM Choose entrypoint (main.py by default)
SET ENTRYPOINT=main.py
REM Build command (will include icon if file exists)
IF EXIST "%ICON%" (
	echo Found icon at %ICON% — building with icon
	pyinstaller --onefile --windowed --noconfirm --clean --name "PythonDesktopApp" --icon "%ICON%" %ENTRYPOINT%
) ELSE (
	echo No icon found at %ICON% — building without icon
	pyinstaller --onefile --windowed --noconfirm --clean --name "PythonDesktopApp" %ENTRYPOINT%
)
echo Build finished. See the dist\ directory.
pause
@echo off
REM Build Windows single-file executable using PyInstaller
REM Usage: run this from project root (double-click or from PowerShell/CMD)












pause
necho Build finished. See the dist\ directory.pyinstaller --onefile --windowed --noconfirm --clean --name "PythonDesktopApp" main.pyREM Build using `main.py` as entrypoint. Change to `first-desktop.py` if you prefer.%PYTHON% -m pip install --upgrade pyinstaller)    SET PYTHON=pythonIF NOT EXIST %PYTHON% (nSET PYTHON=%~dp0\.venv\Scripts\python.exe