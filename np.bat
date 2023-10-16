@echo off
echo.

if [%~1]==[] (goto noargstart) else goto ARGSTART
goto END

:NOARGSTART
start "notepad" "C:\\Program Files\\Notepad++\\notepad++.exe"
goto END

:ARGSTART
start "notepad" "C:\\Program Files\\Notepad++\\notepad++.exe" -nosession -openFoldersAsWorkspace %*
goto END


:END