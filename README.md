# Hand-Controlled Pong Game 🎮✋

A modern take on the classic Pong game that uses computer vision and hand tracking to control the paddle with your hand movements! Built with Python, Pygame, and MediaPipe.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange.svg)

## 🎯 Features

- **Hand Gesture Control**: Control your paddle by raising and lowering your index finger
- **Real-time Hand Tracking**: Uses Google's MediaPipe for accurate hand detection
- **Calibration System**: Two-stage calibration adapts to your hand movement range
- **Visual Feedback**: Live camera preview shows hand tracking in real-time
- **Ball Trail Effect**: Smooth visual trail following the ball
- **Pause Functionality**: Press 'P' to pause/unpause the game
- **Fullscreen Mode**: Automatic fullscreen with windowed fallback
- **AI Opponent**: Challenging computer opponent with adjustable speed
- **Play Again Feature**: Quick restart without relaunching the application

## 🎮 How to Play

1. **Setup**: Position yourself in front of your webcam with good lighting
2. **Posture**: Rest your elbow on a table and keep your arm straight and vertical
3. **Calibration**: 
   - First, raise your index finger as HIGH as possible (5 seconds)
   - Then, lower your index finger as LOW as possible (5 seconds)
4. **Play**: Move your index finger up and down to control the paddle
5. **Win**: First player to reach 5 points wins!

### Controls

- **Index Finger**: Move up/down to control your paddle
- **P Key**: Pause/unpause the game
- **Q Key**: Quit the game
- **Mouse**: Click buttons on menu screens

## 📋 Requirements

### System Requirements

- Python 3.8 or higher
- Webcam (built-in or external)
- Operating System: Windows, macOS, or Linux

### Python Dependencies

- `pygame >= 2.6.0` - Game engine and graphics
- `opencv-python >= 4.10.0` - Computer vision and webcam handling
- `mediapipe >= 0.10.21` - Hand tracking and gesture recognition
- `numpy >= 1.26.4` - Array processing

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ekagansahin/hand-controlled-pong.git
cd hand-controlled-pong
```

### 2. Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🎯 Usage

### Running the Game

```bash
python pong_game.py
```

### Quick Start

1. Launch the game
2. Click the **START** button
3. Follow the calibration instructions on screen
4. Play and enjoy!

### Tips for Best Performance

- **Lighting**: Ensure good, even lighting on your hand
- **Background**: Use a plain background behind your hand for better tracking
- **Camera Position**: Position the camera at eye level
- **Hand Position**: Keep your hand within the camera's field of view
- **Arm Stability**: Rest your elbow on a table to reduce jitter

## 🛠️ Configuration

You can customize the game by modifying the `Config` class in `pong_game.py`:

```python
class Config:
    # Display settings
    FULLSCREEN = True
    DEFAULT_WIDTH = 1280
    DEFAULT_HEIGHT = 720
    
    # Game parameters
    FPS = 60
    WINNING_SCORE = 5
    OPPONENT_SPEED = 21
    SMOOTHING_FACTOR = 0.2  # Adjust hand tracking sensitivity
    
    # Ball settings
    BALL_INITIAL_SPEED_MIN = 12
    BALL_INITIAL_SPEED_MAX = 19
    
    # Hand tracking settings
    MIN_DETECTION_CONFIDENCE = 0.7
    MIN_TRACKING_CONFIDENCE = 0.5
```

## 🐛 Troubleshooting

### Camera Not Working

**Error**: "Error: Could not open webcam"

**Solutions**:
- Check if another application is using the webcam
- Grant camera permissions to Python/Terminal
- Try unplugging and replugging external webcam
- Update your webcam drivers

### Hand Not Detected

**Solutions**:
- Improve lighting conditions
- Move closer to the camera
- Ensure your hand is clearly visible
- Reduce background clutter
- Check that your hand is within the camera frame

### Game Running Slowly

**Solutions**:
- Close other resource-intensive applications
- Reduce screen resolution (edit `Config.DEFAULT_WIDTH` and `Config.DEFAULT_HEIGHT`)
- Lower FPS (edit `Config.FPS`)
- Ensure your computer meets minimum requirements

### Calibration Failed

**Solutions**:
- Make a larger range of motion during calibration
- Keep your arm stable during calibration
- Ensure good lighting and clear hand visibility
- Restart the game and try again

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google MediaPipe** - For the amazing hand tracking solution
- **Pygame Community** - For the excellent game development framework
- **OpenCV** - For computer vision capabilities

## 📸 Screenshots

*Add your screenshots here after testing the game!*

## 🔮 Future Enhancements

- [ ] Two-player mode with two hands
- [ ] Difficulty levels (Easy, Medium, Hard)
- [ ] Power-ups and special effects
- [ ] Sound effects and background music
- [ ] High score tracking
- [ ] Multiple gesture controls
- [ ] Tournament mode
- [ ] Custom themes and skins

## 📞 Contact

**ekagansahin**

- GitHub: [@ekagansahin](https://github.com/ekagansahin)
- Project Link: [https://github.com/ekagansahin/hand-controlled-pong](https://github.com/ekagansahin/hand-controlled-pong)

## ⭐ Show Your Support

Give a ⭐️ if this project helped you or if you found it interesting!

---

**Made with ❤️ and Python**

