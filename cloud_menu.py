@echo off
title Cloud Backup & Restore Menu

REM === Create logs folder if missing ===
if not exist "C:\Users\Eugene\Documents\backup_files\logs" mkdir "C:\Users\Eugene\Documents\backup_files\logs"

:menu
cls
echo ===================================
echo      Cloud Backup & Restore
echo ===================================
echo 1. Backup files
echo 2. Restore files
echo 3. Exit
echo ===================================
set /p choice="Choose option (1/2/3): "

if "%choice%"=="1" goto backup
if "%choice%"=="2" goto restore
if "%choice%"=="3" exit
echo Invalid choice, try again.
pause
goto menu


:backup
set LOGFILE=C:\Users\Eugene\Documents\backup_files\logs\backup_%date:~-4%-%date:~4,2%-%date:~7,2%_%time:~0,2%-%time:~3,2%.log
echo Running Backup... > "%LOGFILE%"
echo. >> "%LOGFILE%"
echo.|set /p=1| python C:\Users\Eugene\Documents\cloud_backup.py >> "%LOGFILE%" 2>&1
echo. >> "%LOGFILE%"
echo Backup finished! Log saved to %LOGFILE%
pause
goto menu


:restore
set LOGFILE=C:\Users\Eugene\Documents\backup_files\logs\restore_%date:~-4%-%date:~4,2%-%date:~7,2%_%time:~0,2%-%time:~3,2%.log
echo Running Restore... > "%LOGFILE%"
echo. >> "%LOGFILE%"
echo.|set /p=2| python C:\Users\Eugene\Documents\cloud_backup.py >> "%LOGFILE%" 2>&1
echo. >> "%LOGFILE%"
echo Restore finished! Log saved to %LOGFILE%
pause
goto menu
