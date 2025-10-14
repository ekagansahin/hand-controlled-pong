# How to Run the Game

## ✅ Installation Complete!

All dependencies have been installed successfully using Python 3.12.

## 🎮 Running the Game

### Option 1: Using the Launch Script (Easiest)

**On Linux/macOS:**
```bash
./run_game.sh
```

**On Windows:**
```cmd
run_game.bat
```

### Option 2: Manual Launch

**On Linux/macOS:**
```bash
cd /home/mint/python/game/Trifaze
source venv/bin/activate
python pong_game.py
```

**On Windows:**
```cmd
cd C:\path\to\Trifaze
venv\Scripts\activate
python pong_game.py
```

## 🎯 First Time Playing

1. **Position yourself** in front of your webcam with good lighting
2. **Rest your elbow** on a table and keep your arm vertical
3. **Click START** when the game opens
4. **Calibration:**
   - Raise your index finger as HIGH as possible (5 seconds)
   - Lower your index finger as LOW as possible (5 seconds)
5. **Play!** Move your finger up and down to control the paddle

## 🎮 Controls

- **Index Finger Up/Down**: Control your paddle
- **P Key**: Pause/unpause the game
- **Q Key**: Quit the game
- **Mouse**: Click buttons on menus

## ⚠️ Troubleshooting

### Camera Not Working
```bash
# Check if camera is available
ls /dev/video*

# Grant permissions if needed
sudo usermod -a -G video $USER
# Then log out and log back in
```

### Display Issues
If you get display errors, try:
```bash
export DISPLAY=:0
./run_game.sh
```

### Performance Issues
- Close other applications using the camera
- Ensure good lighting for better hand detection
- Lower FPS in `pong_game.py` Config class if needed

## 🐛 Still Having Issues?

1. Check the webcam is connected and working
2. Ensure no other app is using the camera
3. Verify virtual environment is activated (you should see `(venv)` in your terminal)
4. Try reinstalling dependencies:
   ```bash
   source venv/bin/activate
   pip install --upgrade -r requirements.txt
   ```

## 📝 Note About Python Version

This game requires Python 3.8-3.12. Your installation uses **Python 3.12** which is perfect!

MediaPipe doesn't support Python 3.14 yet, which is why we use Python 3.12.

---

**Enjoy the game! 🎉**

