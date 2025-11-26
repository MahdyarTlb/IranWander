@echo off
title IranWander - سرعت بالا
echo.
echo    سایت داره با سرعت بالا استارت می‌شه...
echo.
cd /d "C:\Users\Asiastock\OneDrive\Desktop\last version\IranWander"
waitress-serve --listen=127.0.0.1:5000 run:app
pause