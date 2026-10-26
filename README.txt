SUSHI desktop app (.exe) - build steps

1. Install Python 3.10 or newer on Windows (tick "Add Python to PATH").
2. Put this folder's files together: main.py, requirements.txt, build_exe.bat,
   sushi_study_helper_v46.html.
3. Double-click build_exe.bat.
4. The finished file is dist\SUSHI.exe. You can copy that single file anywhere.

Notes:
- The app uses Microsoft Edge WebView2 (already on Windows 10/11).
- Internet is needed the first time for the 3D library (three.js) and fonts.
- Voice input (microphone) may ask for permission; if it does not work in the
  .exe, the same features work fully in a normal browser.
