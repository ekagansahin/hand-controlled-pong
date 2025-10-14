# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-14

### Added
- Initial release of Hand-Controlled Pong Game
- Hand gesture control using MediaPipe hand tracking
- Two-stage calibration system for personalized hand movement range
- Real-time webcam feed with hand landmark visualization
- AI opponent with adjustable difficulty
- Ball trail visual effect
- Pause functionality (P key)
- Fullscreen mode with automatic fallback to windowed mode
- "Play Again" feature for quick restarts
- Comprehensive error handling and user feedback
- Camera preview in bottom-right corner during gameplay
- Smooth hand tracking with configurable smoothing factor

### Features
- **Hand Tracking**: Real-time hand detection and index finger tracking
- **Calibration**: Adaptive calibration system that works for any hand size
- **Visual Feedback**: Live camera preview with hand landmarks
- **Game Controls**:
  - Index finger up/down: Control paddle
  - P key: Pause/unpause
  - Q key: Quit game
- **AI Opponent**: Responsive computer opponent
- **Scoring System**: First to 5 points wins
- **Ball Physics**: Dynamic ball speed that changes on paddle collision
- **User Interface**: Clean, modern UI with start screen and game over screen

### Technical Details
- Python 3.8+ support
- Pygame-based game engine
- MediaPipe for hand tracking
- OpenCV for camera handling
- Configurable game parameters via Config class
- FPS-locked gameplay at 60 FPS
- Resolution: Auto-detects in fullscreen, 1280x720 in windowed mode

### Documentation
- Comprehensive README.md with installation and usage instructions
- CONTRIBUTING.md with contribution guidelines
- LICENSE file (MIT License)
- Setup.py for easy installation
- Requirements.txt with pinned dependencies

### Known Issues
- None reported yet

---

## [Unreleased]

### Planned Features
- Two-player mode with two hands
- Difficulty levels (Easy, Medium, Hard)
- Power-ups and special effects
- Sound effects and background music
- High score tracking
- Multiple gesture controls
- Tournament mode
- Custom themes and skins

---

[1.0.0]: https://github.com/ekagansahin/hand-controlled-pong/releases/tag/v1.0.0

