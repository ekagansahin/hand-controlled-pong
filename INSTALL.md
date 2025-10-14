# Installation Guide

This guide provides detailed installation instructions for the Hand-Controlled Pong Game on different operating systems.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Windows Installation](#windows-installation)
- [macOS Installation](#macos-installation)
- [Linux Installation](#linux-installation)
- [Troubleshooting](#troubleshooting)
- [Development Installation](#development-installation)

## Prerequisites

### Required Hardware
- **Webcam**: Built-in or USB webcam
- **RAM**: At least 4GB recommended
- **Processor**: Modern dual-core processor or better

### Software Requirements
- **Python**: Version 3.8 or higher
- **pip**: Python package installer (usually comes with Python)
- **Git**: For cloning the repository (optional)

## Windows Installation

### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Verify installation:
   ```cmd
   python --version
   pip --version
   ```

### Step 2: Install Git (Optional)

Download and install from [git-scm.com](https://git-scm.com/download/win)

### Step 3: Clone or Download the Repository

**Option A - Using Git:**
```cmd
git clone https://github.com/ekagansahin/hand-controlled-pong.git
cd hand-controlled-pong
```

**Option B - Direct Download:**
1. Download ZIP from GitHub
2. Extract to desired location
3. Open Command Prompt in that folder

### Step 4: Create Virtual Environment

```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 5: Install Dependencies

```cmd
pip install -r requirements.txt
```

### Step 6: Run the Game

```cmd
python pong_game.py
```

## macOS Installation

### Step 1: Install Python

**Option A - Using Homebrew (Recommended):**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11
```

**Option B - Download from python.org:**
Download from [python.org](https://www.python.org/downloads/macos/)

### Step 2: Verify Installation

```bash
python3 --version
pip3 --version
```

### Step 3: Clone the Repository

```bash
git clone https://github.com/ekagansahin/hand-controlled-pong.git
cd hand-controlled-pong
```

### Step 4: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Grant Camera Permissions

1. System Preferences → Security & Privacy → Camera
2. Allow Terminal or your IDE to access the camera

### Step 7: Run the Game

```bash
python pong_game.py
```

## Linux Installation

### Step 1: Install Python and Dependencies

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
sudo apt install python3-opencv  # Optional: system OpenCV
```

**Fedora:**
```bash
sudo dnf install python3 python3-pip python3-virtualenv
```

**Arch Linux:**
```bash
sudo pacman -S python python-pip
```

### Step 2: Install Additional Libraries

Some distributions may need additional packages:

```bash
# Ubuntu/Debian
sudo apt install libportaudio2 libportaudiocpp0 portaudio19-dev
sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

# Fedora
sudo dnf install portaudio portaudio-devel SDL2 SDL2-devel
```

### Step 3: Clone the Repository

```bash
git clone https://github.com/ekagansahin/hand-controlled-pong.git
cd hand-controlled-pong
```

### Step 4: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Game

```bash
python pong_game.py
```

## Troubleshooting

### Python Not Found

**Windows:**
- Reinstall Python and check "Add to PATH"
- Manually add Python to PATH in Environment Variables

**macOS/Linux:**
- Use `python3` instead of `python`
- Use `pip3` instead of `pip`

### Permission Denied on Linux

```bash
chmod +x pong_game.py
```

### Camera Not Working

**Windows:**
- Check Camera privacy settings
- Ensure no other app is using the camera

**macOS:**
- Grant camera permissions in System Preferences

**Linux:**
- Add user to video group:
  ```bash
  sudo usermod -a -G video $USER
  ```
- Log out and log back in

### Module Import Errors

```bash
# Ensure virtual environment is activated
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### MediaPipe Installation Issues

If MediaPipe fails to install:

```bash
# Try installing pre-built wheel
pip install --upgrade pip
pip install mediapipe --no-cache-dir

# For Apple Silicon Macs
arch -arm64 pip install mediapipe
```

### Pygame Display Issues on Linux

```bash
# Install additional SDL libraries
sudo apt install libsdl2-2.0-0 libsdl2-image-2.0-0 libsdl2-mixer-2.0-0 libsdl2-ttf-2.0-0
```

### Performance Issues

- Close other applications using the camera
- Reduce game resolution in `Config` class
- Lower FPS setting
- Ensure adequate lighting for better hand detection

## Development Installation

For developers who want to contribute:

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR-USERNAME/hand-controlled-pong.git
cd hand-controlled-pong
```

### 2. Install Development Dependencies

```bash
pip install -r requirements.txt
pip install flake8 black mypy pytest
```

### 3. Install in Editable Mode

```bash
pip install -e .
```

### 4. Set Up Pre-commit Hooks (Optional)

```bash
pip install pre-commit
pre-commit install
```

## Verifying Installation

Run this command to verify everything is installed correctly:

```bash
python -c "import pygame; import cv2; import mediapipe; import numpy; print('All dependencies installed successfully!')"
```

## Uninstallation

### Remove Virtual Environment

```bash
# Deactivate if active
deactivate

# Delete virtual environment folder
rm -rf venv  # Linux/macOS
rmdir /s venv  # Windows
```

### Uninstall Package

If installed via pip:
```bash
pip uninstall hand-controlled-pong
```

## Getting Help

If you encounter issues not covered here:

1. Check the [README.md](README.md) for basic troubleshooting
2. Search [existing issues](https://github.com/ekagansahin/hand-controlled-pong/issues)
3. Create a [new issue](https://github.com/ekagansahin/hand-controlled-pong/issues/new) with:
   - Your OS and Python version
   - Complete error message
   - Steps you've already tried

---

**Happy Gaming! 🎮**

