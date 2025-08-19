@echo off
REM Automated Cloud Backup (always option 1)
set LOGFILE=C:\Users\Eugene\Documents\backup_files\logs\backup_%date:~-4%-%date:~4,2%-%date:~7,2%_%time:~0,2%-%time:~3,2%.log

if not exist "C:\Users\Eugene\Documents\backup_files\logs" mkdir "C:\Users\Eugene\Documents\backup_files\logs"

echo Running Automated Backup... > "%LOGFILE%"
echo. >> "%LOGFILE%"

echo.|set /p=1| python C:\Users\Eugene\Documents\cloud_backup.py >> "%LOGFILE%" 2>&1

echo. >> "%LOGFILE%"
echo Backup finished! Log saved to %LOGFILE%
