# i_love_you_python3
Compile to exe with PyInstaller and send to your love
# How to compile using PyInstaller?
1. Install Python [here](https://www.python.org/downloads/windows)
2. Download code [here](https://github.com/KhanhNguyen9872/i_love_you_python3/archive/refs/heads/main.zip)
3. Extract zip file
4. Open CMD in folder extracted
5. Install PyInstaller and PyPiWin32 (run on CMD)
```bash
python -m pip install pyinstaller pypiwin32
```
6. Compile main.py to main.exe (run on CMD)
- If you don't have icon (.ico file), you can remove --icon=<your-path-icon> in your command!
```bash
pyinstaller main.py --upx-dir=. --onefile --icon=<your-path-icon>
```
7. File exe in
```
./dist/main.exe
```
8. Send to your love and Enjoy
