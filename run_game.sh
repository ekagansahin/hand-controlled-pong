#!/bin/bash
# Hand-Controlled Pong Game Launcher

cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Error: Virtual environment not found!"
    echo "Please run: python3.12 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment and run game
source venv/bin/activate
echo "Starting Hand-Controlled Pong Game..."
echo "Controls:"
echo "  - Move your index finger up/down to control the paddle"
echo "  - P: Pause/unpause"
echo "  - Q: Quit"
echo ""
python pong_game.py

