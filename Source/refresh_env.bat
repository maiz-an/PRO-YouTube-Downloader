@echo off
echo Refreshing environment variables...
:: This method helps refresh PATH after Python installation
for /f "skip=2 tokens=3*" %%a in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PATH') do set "SYSTEMPATH=%%a %%b"
for /f "skip=2 tokens=3*" %%a in ('reg query "HKCU\Environment" /v PATH') do set "USERPATH=%%a %%b"
set "PATH=%SYSTEMPATH%;%USERPATH%"
echo Environment refreshed!