# Quick Start Guide

Get up and running with Hand-Controlled Pong in 5 minutes!

## 🚀 Quick Installation

### Windows
```cmd
git clone https://github.com/ekagansahin/hand-controlled-pong.git
cd hand-controlled-pong
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python pong_game.py
```

### macOS/Linux
```bash
git clone https://github.com/ekagansahin/hand-controlled-pong.git
cd hand-controlled-pong
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python pong_game.py
```

## 🎮 First Time Playing

1. **Position yourself**: Sit in front of your webcam with good lighting
2. **Click START**: Click the green START button
3. **Calibration - High**: Raise your index finger as HIGH as possible (5 seconds)
4. **Calibration - Low**: Lower your index finger as LOW as possible (5 seconds)
5. **Play!**: Move your finger up and down to control the paddle

## 💡 Pro Tips

- **Rest your elbow** on the table for stability
- **Keep your arm vertical** and straight
- **Use good lighting** for better hand detection
- **Press P** to pause anytime
- **Press Q** to quit

## 🎯 Game Rules

- First to **5 points** wins
- Ball gets **faster** after each paddle hit
- Computer opponent tries to block your shots

## 🆘 Problems?

### Camera not working?
- Check if another app is using it
- Grant camera permissions
- Try unplugging/replugging if external

### Hand not detected?
- Improve lighting
- Get closer to camera
- Clear background behind hand

### Game too hard?
Edit `Config.OPPONENT_SPEED` in `pong_game.py` (lower = easier)

## 📚 Learn More

- Full documentation: [README.md](README.md)
- Detailed installation: [INSTALL.md](INSTALL.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Enjoy the game! 🎉**

