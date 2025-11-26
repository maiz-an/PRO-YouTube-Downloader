@echo off
chcp 65001 >nul
title PRO YouTube Downloader

echo.
echo ════════════════════════════════════════════════════════════════
echo                    PRO YouTube Downloader
echo ════════════════════════════════════════════════════════════════
echo.

:: Change to script directory
cd /d "%~dp0"

:: Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found! Please install Python from:
    echo    https://python.org
    echo.
    pause
    exit /b 1
)

:: Run the main launcher directly
echo 🚀 Starting PRO YouTube Downloader...
echo.
python "Source\launcher.py"

:: If application exits, pause to show any messages
if %errorlevel% neq 0 (
    echo.
    echo ❌ Application exited with error code: %errorlevel%
    pause
)