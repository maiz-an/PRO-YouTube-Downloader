@echo off
chcp 65001 >nul
title PRO YouTube Downloader - Setup Assistant
color 07

:: Set working directory to script location
cd /d "%~dp0"

echo.
echo ════════════════════════════════════════════════════════════════
echo                    PRO YouTube Downloader
echo                  Setup Assistant
echo ════════════════════════════════════════════════════════════════
echo.

:INITIAL_SETUP
set PYTHON_EXE=python
set PIP_EXE=pip
set INSTALL_SUCCESS=0
set SCRIPT_PATH=Source\Downloader.py
set REFRESH_ENV_PATH=Source\refresh_env.bat

:: Dynamic path detection and validation
echo 🔍 Scanning for required files...

:: Initialize variables properly
set "SOURCE_FOLDER_EXISTS=0"
set "DOWNLOADER_EXISTS=0"
set "REFRESH_ENV_EXISTS=0"

:: Check file existence without using parentheses in condition
if exist "Source\" (
    set "SOURCE_FOLDER_EXISTS=1"
)
if exist "%SCRIPT_PATH%" (
    set "DOWNLOADER_EXISTS=1"
)
if exist "%REFRESH_ENV_PATH%" (
    set "REFRESH_ENV_EXISTS=1"
)

:: If Source folder doesn't exist, check if we're already in Source folder
if "%SOURCE_FOLDER_EXISTS%"=="0" (
    if exist "Downloader.py" (
        echo ℹ️  Found Downloader.py in current directory
        set "SCRIPT_PATH=Downloader.py"
        set "REFRESH_ENV_PATH=refresh_env.bat"
        if exist "%REFRESH_ENV_PATH%" (
            set "REFRESH_ENV_EXISTS=1"
        )
        set "DOWNLOADER_EXISTS=1"
    )
)

:: Check if Python script exists with dynamic path handling
if not exist "%SCRIPT_PATH%" (
    echo ❌ Error: Downloader.py not found!
    echo.
    echo 📁 Current location: %CD%
    echo 🔍 Searching for Downloader.py...
    dir /s /b Downloader.py 2>nul
    if errorlevel 1 (
        echo ❗ Could not find Downloader.py in any subdirectory
    )
    echo.
    echo 🔧 Setup Assistant: Let me help you fix this!
    echo.
    echo Possible solutions:
    echo 1. Ensure the folder structure is:
    echo    Mainfolder/
    echo    ├── Run.bat
    echo    └── Source/
    echo        ├── Downloader.py
    echo        └── refresh_env.bat
    echo.
    echo 2. Or Downloader.py should be in the same folder as Run.bat
    echo.
    choice /C YN /M "Would you like to create the required folder structure automatically"
    if %errorlevel% equ 1 (
        echo.
        echo 🛠️  Creating folder structure...
        if not exist "Source" mkdir Source
        echo 📝 Please make sure to:
        echo    - Place Downloader.py in the 'Source' folder
        echo    - Place refresh_env.bat in the 'Source' folder
        echo    - Then run this script again
        echo.
        echo 📁 Created folder: %CD%\Source
        echo.
        pause
        explorer "%~dp0"
        exit /b 1
    ) else (
        echo.
        echo 💡 Manual setup required.
        echo Please ensure Downloader.py is in the correct location.
        pause
        exit /b 1
    )
)

:: Check if refresh_env.bat exists
if not exist "%REFRESH_ENV_PATH%" (
    echo ⚠️  Warning: refresh_env.bat not found at %REFRESH_ENV_PATH%
    echo Creating a basic refresh_env.bat file...
    (
        echo @echo off
        echo echo Refreshing environment variables...
        echo for /f "skip=2 tokens=3*" %%a in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PATH' 2^>nul'^) do set "SYSTEMPATH=%%a %%b"
        echo for /f "skip=2 tokens=3*" %%a in ('reg query "HKCU\Environment" /v PATH' 2^>nul'^) do set "USERPATH=%%a %%b"
        echo set "PATH=%%SYSTEMPATH%%;%%USERPATH%%"
        echo echo Environment refreshed!
    ) > "%REFRESH_ENV_PATH%"
    echo ✅ Created %REFRESH_ENV_PATH%
)

echo ✅ Found required files:
echo    - Downloader.py: %SCRIPT_PATH%
echo    - refresh_env.bat: %REFRESH_ENV_PATH%
echo.

:: Enhanced dependency checking
echo 🔧 Performing comprehensive system check...

:: Check if Python is installed
echo [1/4] 🔍 Checking Python installation...
%PYTHON_EXE% --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found or not in PATH
    echo.
    echo 🔧 Setup Assistant: I need to help you install Python first!
    echo.
    choice /C YN /M "Would you like me to download and install Python 3.11 automatically"
    if %errorlevel% equ 2 (
        echo.
        echo ❗ Python is required to run this application.
        echo Please install Python manually from https://python.org
        echo and make sure to check 'Add Python to PATH' during installation.
        pause
        exit /b 1
    )
    
    echo.
    echo 📥 Downloading Python installer...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe' -OutFile 'python_installer.exe'" 2>nul
    
    if exist "python_installer.exe" (
        echo 🚀 Installing Python... This may take a few minutes.
        echo 📝 Please check 'Add Python to PATH' in the installer!
        echo.
        start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
        del python_installer.exe 2>nul
        echo.
        echo ✅ Python installation completed!
        echo 🔄 Refreshing environment variables...
        call "%REFRESH_ENV_PATH%"
        timeout /t 3 >nul
    ) else (
        echo ❌ Failed to download Python installer.
        echo Please install Python manually from https://python.org
        pause
        exit /b 1
    )
    
    :: Verify Python installation after install
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo ❗ Python installed but not detected in PATH.
        echo Please restart your computer or add Python to PATH manually.
        pause
        exit /b 1
    )
    set PYTHON_EXE=python
)

for /f "tokens=*" %%i in ('%PYTHON_EXE% --version 2^>nul') do set PYTHON_VERSION=%%i
echo ✅ Python detected: %PYTHON_VERSION%
echo.

:: Check and upgrade pip
echo [2/4] 🔧 Checking pip package manager...
%PYTHON_EXE% -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Pip not available, installing...
    %PYTHON_EXE% -m ensurepip --default-pip
    %PYTHON_EXE% -m pip install --upgrade pip
) else (
    echo 📦 Upgrading pip to latest version...
    %PYTHON_EXE% -m pip install --upgrade pip --quiet
)
for /f "tokens=1,2" %%i in ('%PYTHON_EXE% -m pip --version 2^>nul') do set PIP_VERSION=%%j
echo ✅ Pip ready: version %PIP_VERSION%
echo.

:: Enhanced FFmpeg check
echo [3/4] 🎬 Checking FFmpeg installation...
ffmpeg -version >nul 2>&1
if %errorlevel% equ 0 (
    for /f "tokens=1,2,3" %%i in ('ffmpeg -version 2^>^&1 ^| findstr /C:"ffmpeg version"') do (
        echo ✅ FFmpeg detected: %%i %%j %%k
    )
) else (
    echo ❌ FFmpeg not found in PATH
    echo.
    echo 📝 Note: FFmpeg is required for audio processing and video merging.
    echo    You can install it from: https://ffmpeg.org/download.html
    echo    Some features may not work without FFmpeg.
)

echo.

:: Comprehensive yt-dlp check
echo [4/4] 📚 Checking Python dependencies...
%PYTHON_EXE% -c "import yt_dlp" >nul 2>&1
if %errorlevel% equ 0 (
    for /f "tokens=*" %%i in ('%PYTHON_EXE% -c "import yt_dlp; print(yt_dlp.version.__version__)" 2^>nul') do set YT_DLP_VERSION=%%i
    echo ✅ yt-dlp is already installed: version %YT_DLP_VERSION%
    set INSTALL_SUCCESS=1
    goto SKIP_INSTALL
)

echo.
echo 🔄 yt-dlp not found. Installing now...
set ATTEMPT=1
:DEPENDENCY_INSTALL
echo 🔄 Attempt %ATTEMPT%: Installing yt-dlp...
%PYTHON_EXE% -m pip install yt-dlp --upgrade --no-warn-script-location

:: Verify installation
%PYTHON_EXE% -c "import yt_dlp" >nul 2>&1
if %errorlevel% equ 0 (
    for /f "tokens=*" %%i in ('%PYTHON_EXE% -c "import yt_dlp; print(yt_dlp.version.__version__)" 2^>nul') do set YT_DLP_VERSION=%%i
    echo ✅ yt-dlp installed successfully: version %YT_DLP_VERSION%
    set INSTALL_SUCCESS=1
) else (
    echo ❌ yt-dlp installation failed on attempt %ATTEMPT%
    set /a ATTEMPT+=1
    if %ATTEMPT% leq 3 (
        echo 🔄 Retrying installation...
        timeout /t 2 >nul
        goto DEPENDENCY_INSTALL
    ) else (
        echo ❗ Failed to install yt-dlp after 3 attempts.
        echo.
        echo ⚠️  The application may not work properly without yt-dlp.
        echo.
        pause
    )
)

:SKIP_INSTALL
:: Create Downloads folder if it doesn't exist
if not exist "Downloads" (
    mkdir Downloads
    echo 📁 Created Downloads folder for your files
)

echo.
echo ════════════════════════════════════════════════════════════════
echo ✅ All systems ready! Launching PRO YouTube Downloader...
echo 📁 Downloads will be saved in: %CD%\Downloads
echo 📍 Running from: %CD%
echo ════════════════════════════════════════════════════════════════
echo.

:: Wait a moment then clear screen and launch
timeout /t 2 >nul

:: Clear the screen to remove all setup logs
cls

:: Launch main application directly
title PRO YouTube Downloader
echo.
echo 🚀 Launching PRO YouTube Downloader...
echo.
%PYTHON_EXE% "%SCRIPT_PATH%"
set APP_EXIT_CODE=%errorlevel%

if %APP_EXIT_CODE% neq 0 (
    echo.
    echo ❌ Application exited with error code: %APP_EXIT_CODE%
    echo.
    choice /C YN /M "Would you like to restart the application"
    if %errorlevel% equ 1 (
        echo.
        echo 🔄 Restarting application...
        timeout /t 3 >nul
        cls
        goto RUN_APP
    )
)

echo.
echo 👋 Thank you for using PRO YouTube Downloader!
echo 📂 Your downloaded files are in: %CD%\Downloads
echo.
pause