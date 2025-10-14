@echo off
REM Hand-Controlled Pong Game Launcher for Windows

cd /d "%~dp0"

REM Check if virtual environment exists
if not exist "venv\" (
    echo Error: Virtual environment not found!
    echo Please run: python -m venv venv
    echo Then: venv\Scripts\activate
    echo Then: pip install -r requirements.txt
    pause
    exit /b 1
)

REM Activate virtual environment and run game
call venv\Scripts\activate.bat
echo Starting Hand-Controlled Pong Game...
echo Controls:
echo   - Move your index finger up/down to control the paddle
echo   - P: Pause/unpause
echo   - Q: Quit
echo.
python pong_game.py
pause

