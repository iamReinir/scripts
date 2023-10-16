@echo off
echo.

set backlogfile="D:\#Reinir\Doc\notes\backlog.txt"

if [%~1] == [] (goto noarg) else goto arg

:NOARG
echo ## BACKLOG ##
echo:
type %backlogfile%
echo:
echo:
echo ## END OF BACKLOG ##
goto END

:ARG
echo %* >> %backlogfile%
:END