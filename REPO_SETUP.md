# Repository Setup Guide

Follow these steps to create your GitHub repository for this project.

## 1. Create Repository on GitHub

1. Go to [https://github.com/ekagansahin](https://github.com/ekagansahin)
2. Click the "+" icon in the top right → "New repository"
3. Repository settings:
   - **Name**: `hand-controlled-pong`
   - **Description**: `A hand-controlled Pong game using MediaPipe hand tracking`
   - **Visibility**: Public
   - **Do NOT initialize** with README, .gitignore, or license (we already have these)
4. Click "Create repository"

## 2. Setup GitHub Authentication

⚠️ **IMPORTANT**: GitHub requires SSH keys or Personal Access Token (not passwords).

### Quick SSH Setup (Recommended):
```bash
cd /home/mint/python/game/Trifaze
./setup_github_ssh.sh
```

This script will:
1. Generate an SSH key for you
2. Show you the key to copy
3. Guide you to add it to GitHub
4. Set up your repository automatically

**For detailed instructions**, see [GITHUB_AUTH_SETUP.md](GITHUB_AUTH_SETUP.md)

## 3. Initialize and Push Your Code

After setting up authentication, run:

```bash
# Navigate to your project directory
cd /home/mint/python/game/Trifaze

# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Hand-Controlled Pong Game v1.0.0"

# Rename branch to main
git branch -M main

# If you used SSH setup script, this is already done!
# Otherwise, add remote repository:
git remote add origin git@github.com:ekagansahin/hand-controlled-pong.git

# Push to GitHub
git push -u origin main
```

## 4. Configure Repository Settings on GitHub

### Add Topics
Go to your repository → Click the gear icon next to "About" → Add topics:
- `pong`
- `hand-tracking`
- `mediapipe`
- `opencv`
- `pygame`
- `computer-vision`
- `gesture-control`
- `python`
- `game`
- `hand-gesture`

### Update Repository Description
In the same "About" section, add:
- **Description**: `A hand-controlled Pong game using MediaPipe hand tracking`
- **Website**: Leave blank or add your demo URL
- Check ✓ "Releases"
- Check ✓ "Packages"

### Enable Features (Optional)
Go to Settings → General:
- ✓ Issues
- ✓ Projects (if you want project boards)
- ✓ Discussions (for community discussions)
- ✓ Preserve this repository (under "Danger Zone")

## 5. Create Your First Release

1. Go to Releases → "Create a new release"
2. Click "Choose a tag" → Type `v1.0.0` → "Create new tag"
3. Release title: `Hand-Controlled Pong v1.0.0`
4. Description:
   ```markdown
   ## 🎮 Hand-Controlled Pong Game v1.0.0
   
   First stable release of Hand-Controlled Pong!
   
   ### Features
   - Real-time hand tracking using MediaPipe
   - Adaptive calibration system
   - AI opponent
   - Ball trail effects
   - Pause functionality
   - Fullscreen support
   
   ### Installation
   ```bash
   pip install -r requirements.txt
   python pong_game.py
   ```
   
   See [README.md](https://github.com/ekagansahin/hand-controlled-pong#readme) for detailed instructions.
   ```
5. Click "Publish release"

## 6. Add Screenshots/Demo (Recommended)

1. Take screenshots of your game
2. Create a `screenshots` folder in your repo
3. Add images to README.md
4. Optional: Record a demo video and upload to YouTube, then embed in README

## 7. Share Your Project

Your project is now live at:
**https://github.com/ekagansahin/hand-controlled-pong**

Share it on:
- Twitter/X with hashtags: #Python #GameDev #ComputerVision #MediaPipe
- Reddit: r/Python, r/gamedev, r/computervision
- LinkedIn
- Dev.to
- Hacker News

## 8. Optional Enhancements

### Add README Badge
Add this badge to your README.md (already included):
```markdown
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
```

### Enable GitHub Pages (for documentation)
Settings → Pages → Source: Deploy from branch → Select `main` branch

### Add Social Preview Image
Settings → General → Social Preview → Upload image (1280x640px recommended)

---

**You're all set! 🎉**

Your repository is now production-ready and follows all GitHub best practices.
