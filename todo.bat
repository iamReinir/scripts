@echo off
echo.
cd /d D:\todo
git pull
"C:\\Program Files\\Notepad++\\notepad++.exe" D:\todo\todo.txt
git add .
git commit -m "Edit"
git push
cd /d "C:\Users\Giga P34"