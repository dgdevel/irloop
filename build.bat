del dist\irloop.exe
python -m PyInstaller --onefile irloop.py
"C:\Program Files (x86)\Windows Kits\10\bin\10.0.19041.0\x64\signtool.exe" sign /s dgcertstore /n dgdevel dist/irloop.exe
pause