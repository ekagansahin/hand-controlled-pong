#!/usr/bin/env python3
"""
Hand-Controlled Pong Game

A modern take on classic Pong that uses MediaPipe to track the player's hand via
a webcam. The player moves the paddle by raising/lowering the index finger.
The game ends when either side reaches the winning score. Includes dynamic
ball speed on paddle collisions and a pause menu.

Author: ekagansahin
Repository: https://github.com/ekagansahin/hand-controlled-pong
License: MIT
"""

import sys
import random
import pygame
import cv2
import numpy as np
import mediapipe as mp


# =============================================================================
# CONFIGURATION AND CONSTANTS
# =============================================================================

class Config:
    """Game configuration constants."""
    # Display settings
    FULLSCREEN = True
    DEFAULT_WIDTH = 1280
    DEFAULT_HEIGHT = 720
    
    # Game parameters
    FPS = 60
    WINNING_SCORE = 5
    OPPONENT_SPEED = 21
    SMOOTHING_FACTOR = 0.2  # Dampens jitter in hand tracking
    
    # Ball settings
    BALL_INITIAL_SPEED_MIN = 12
    BALL_INITIAL_SPEED_MAX = 19
    BALL_COLLISION_SPEED_MIN = 12
    BALL_COLLISION_SPEED_MAX = 25
    BALL_MIN_VERTICAL_SPEED = 8
    
    # Paddle settings
    PADDLE_WIDTH = 15
    PADDLE_HEIGHT = 140
    PADDLE_MARGIN = 50
    
    # Visual settings
    BALL_SIZE = 30
    TRAIL_COUNT = 5
    TRAIL_START_COLOR = 240
    CAMERA_PREVIEW_WIDTH = 160
    CAMERA_PREVIEW_HEIGHT = 120
    CAMERA_PREVIEW_MARGIN = 10
    
    # Hand tracking settings
    MIN_DETECTION_CONFIDENCE = 0.7
    MIN_TRACKING_CONFIDENCE = 0.5
    MAX_NUM_HANDS = 1
    
    # Calibration settings
    CALIBRATION_COUNTDOWN = 5
    
    # Colors (RGB)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)


# =============================================================================
# INITIALIZATION
# =============================================================================

def initialize_pygame():
    """Initialize Pygame and create display."""
    pygame.init()
    
    if Config.FULLSCREEN:
        try:
            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        except pygame.error as e:
            print(f"Warning: Could not set fullscreen mode: {e}")
            print(f"Falling back to windowed mode {Config.DEFAULT_WIDTH}x{Config.DEFAULT_HEIGHT}")
            screen = pygame.display.set_mode((Config.DEFAULT_WIDTH, Config.DEFAULT_HEIGHT))
    else:
        screen = pygame.display.set_mode((Config.DEFAULT_WIDTH, Config.DEFAULT_HEIGHT))
    
    pygame.display.set_caption("Hand Tracking Pong")
    return screen


def initialize_mediapipe():
    """Initialize MediaPipe Hands solution."""
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        min_detection_confidence=Config.MIN_DETECTION_CONFIDENCE,
        min_tracking_confidence=Config.MIN_TRACKING_CONFIDENCE,
        max_num_hands=Config.MAX_NUM_HANDS
    )
    mp_drawing = mp.solutions.drawing_utils
    return mp_hands, hands, mp_drawing


def initialize_camera():
    """Initialize webcam with error handling."""
    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        print("Error: Could not open webcam.")
        print("Please ensure:")
        print("  1. A webcam is connected")
        print("  2. No other application is using the webcam")
        print("  3. You have granted camera permissions")
        return None
    
    # Set camera properties for better performance
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.CAP_PROP_FPS, 30)
    
    return camera


def generate_trail_colors():
    """Generate gradient colors for ball trail."""
    trail_colors = []
    for i in range(Config.TRAIL_COUNT):
        val = Config.TRAIL_START_COLOR - (i * (Config.TRAIL_START_COLOR / Config.TRAIL_COUNT))
        trail_colors.append((val, val, val))
    return trail_colors


# Initialize global components
screen = initialize_pygame()
WIDTH, HEIGHT = screen.get_size()

mp_hands, hands, mp_drawing = initialize_mediapipe()
camera = initialize_camera()

# Initialize fonts
try:
    main_font = pygame.font.Font(None, 74)
    comment_font = pygame.font.Font(None, 44)
    ui_font = pygame.font.Font(None, 50)
    calibration_font = pygame.font.Font(None, 40)
    game_over_font = pygame.font.Font(None, 100)
    pause_font = pygame.font.Font(None, 84)
except Exception as e:
    print(f"Error loading fonts: {e}")
    sys.exit(1)

# Generate trail colors
trail_colors = generate_trail_colors()

# Initialize game objects
player_paddle = pygame.Rect(
    Config.PADDLE_MARGIN, 
    HEIGHT // 2 - Config.PADDLE_HEIGHT // 2, 
    Config.PADDLE_WIDTH, 
    Config.PADDLE_HEIGHT
)
opponent_paddle = pygame.Rect(
    WIDTH - Config.PADDLE_MARGIN - Config.PADDLE_WIDTH,
    HEIGHT // 2 - Config.PADDLE_HEIGHT // 2,
    Config.PADDLE_WIDTH,
    Config.PADDLE_HEIGHT
)
ball = pygame.Rect(
    WIDTH // 2 - Config.BALL_SIZE // 2,
    HEIGHT // 2 - Config.BALL_SIZE // 2,
    Config.BALL_SIZE,
    Config.BALL_SIZE
)

# Initialize trail
trail_rects = [
    pygame.Rect(
        WIDTH // 2 - Config.BALL_SIZE // 2,
        HEIGHT // 2 - Config.BALL_SIZE // 2,
        Config.BALL_SIZE,
        Config.BALL_SIZE
    )
    for _ in range(Config.TRAIL_COUNT)
]

# Game state variables
ball_speed_x = 0
ball_speed_y = 0
player_score = 0
opponent_score = 0


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def reset_game_state():
    """Reset scores, speeds, and object positions for a new game."""
    global player_score, opponent_score, ball_speed_x, ball_speed_y
    player_score = 0
    opponent_score = 0
    player_paddle.y = HEIGHT // 2 - Config.PADDLE_HEIGHT // 2
    opponent_paddle.y = HEIGHT // 2 - Config.PADDLE_HEIGHT // 2
    ball.center = (WIDTH // 2, HEIGHT // 2)
    initial_speed = random.randint(Config.BALL_INITIAL_SPEED_MIN, Config.BALL_INITIAL_SPEED_MAX)
    ball_speed_x = initial_speed * random.choice([1, -1])
    ball_speed_y = initial_speed * random.choice([1, -1])

def draw_elements(frame_surface=None):
    """Render all visual elements (paddles, ball, scores, optional camera feed)."""
    screen.fill(Config.BLACK)
    pygame.draw.rect(screen, Config.WHITE, player_paddle)
    pygame.draw.rect(screen, Config.WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, Config.WHITE, ball)

    # Ball trail
    for i in range(Config.TRAIL_COUNT):
        pygame.draw.ellipse(screen, trail_colors[i], trail_rects[i])

    # Center dividing line
    pygame.draw.aaline(screen, Config.WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Scores
    player_text = main_font.render(str(player_score), True, Config.WHITE)
    screen.blit(player_text, (WIDTH // 4, 20))
    opponent_text = main_font.render(str(opponent_score), True, Config.WHITE)
    screen.blit(opponent_text, (WIDTH * 3 // 4, 20))

    # Mini camera preview (bottom-right)
    if frame_surface:
        preview_width = Config.CAMERA_PREVIEW_WIDTH
        preview_height = Config.CAMERA_PREVIEW_HEIGHT
        margin = Config.CAMERA_PREVIEW_MARGIN
        frame_surface_scaled = pygame.transform.scale(frame_surface, (preview_width, preview_height))
        screen.blit(frame_surface_scaled, (WIDTH - preview_width - margin, HEIGHT - preview_height - margin))

def reset_ball():
    """Center the ball after a point and flip its direction."""
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= -1
    ball_speed_y *= random.choice([1, -1])

def safe_exit():
    """Release resources (camera, models) and terminate cleanly."""
    print("Exiting game...")
    if camera is not None and camera.isOpened():
        camera.release()
    if hands is not None:
        hands.close()
    pygame.quit()
    sys.exit()

def calibrate_finger():
    """
    Two-stage calibration to measure the player's finger motion range.
    
    Returns:
        tuple: (min_diff, max_diff) representing the calibrated range
    """
    if camera is None or not camera.isOpened():
        print("Warning: Camera not available. Using default calibration values.")
        return 0.0, 0.2
    
    min_diff = 1.0
    max_diff = 0.0
    
    for stage in range(2):  # 0: raise finger; 1: lower finger
        message = (
            "Raise your index finger as HIGH as possible"
            if stage == 0 else
            "Now, lower it as LOW as possible"
        )
        countdown = Config.CALIBRATION_COUNTDOWN
        start_time = pygame.time.get_ticks()

        while True:
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
            time_left = countdown - elapsed_time
            if time_left < 0:
                break

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    safe_exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    safe_exit()

            # Grab a frame
            success, frame = camera.read()
            if not success:
                continue

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                wrist_y = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                diff_y = wrist_y - finger_y

                if stage == 0:
                    if diff_y > max_diff:
                        max_diff = diff_y
                else:
                    if diff_y < min_diff:
                        min_diff = diff_y

            # Draw calibration UI
            screen.fill(Config.BLACK)
            frame_surface = pygame.surfarray.make_surface(
                cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).swapaxes(0, 1)
            )
            frame_surface = pygame.transform.scale(frame_surface, (WIDTH, HEIGHT))
            screen.blit(frame_surface, (0, 0))

            msg_text = calibration_font.render(message, True, Config.WHITE, Config.BLACK)
            screen.blit(msg_text, (50, 50))

            countdown_text = main_font.render(str(time_left), True, Config.WHITE)
            screen.blit(countdown_text, (WIDTH // 2 - 20, 100))

            pygame.display.flip()

    print(f"Calibration complete. Min Diff: {min_diff:.4f}, Max Diff: {max_diff:.4f}")
    if max_diff <= min_diff:
        print("Warning: Calibration failed. Using default values.")
        return 0.0, 0.2
    return min_diff, max_diff

def start_screen():
    """Show the start screen, wait for the user to click START or quit."""
    clock = pygame.time.Clock()
    start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 60)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                safe_exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                safe_exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return

        # UI
        screen.fill(Config.BLACK)
        title_text = main_font.render("Hand Tracking PONG", True, Config.WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        instruction_text = comment_font.render(
            "Please rest your elbow on the table. Keep your arm straight.",
            True,
            Config.WHITE
        )
        screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 3))

        pygame.draw.rect(screen, Config.GREEN, start_button)
        start_text = ui_font.render("START", True, Config.BLACK)
        screen.blit(start_text, (start_button.x + 55, start_button.y + 15))

        pygame.display.flip()
        clock.tick(15)

def game_over_screen(winner):
    """
    Show winner and let the user choose 'Play Again' or 'Quit'.
    
    Args:
        winner (str): The winner of the game ("Player" or "Computer")
        
    Returns:
        bool: True if user wants to play again, False to quit
    """
    clock = pygame.time.Clock()
    play_again_button = pygame.Rect(WIDTH // 2 - 250, HEIGHT * 3 // 4 - 30, 200, 60)
    quit_button = pygame.Rect(WIDTH // 2 + 50, HEIGHT * 3 // 4 - 30, 200, 60)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    return True
                if quit_button.collidepoint(event.pos):
                    return False

        # UI
        screen.fill(Config.BLACK)
        game_over_text = game_over_font.render("GAME OVER", True, Config.RED)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 4))

        winner_text_str = "USER WINS!" if winner == "Player" else "COMPUTER WINS!"
        winner_text = main_font.render(winner_text_str, True, Config.WHITE)
        screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - 50))

        pygame.draw.rect(screen, Config.GREEN, play_again_button)
        play_again_text = ui_font.render("Play Again", True, Config.BLACK)
        screen.blit(play_again_text, (play_again_button.x + 20, play_again_button.y + 15))

        pygame.draw.rect(screen, Config.BLUE, quit_button)
        quit_text = ui_font.render("Quit", True, Config.WHITE)
        screen.blit(quit_text, (quit_button.x + 70, quit_button.y + 15))

        pygame.display.flip()
        clock.tick(15)


# =============================================================================
# MAIN GAME LOOP
# =============================================================================

def game_loop(min_diff, max_diff):
    """
    Run the main game loop.
    
    Args:
        min_diff (float): Minimum calibrated finger position difference
        max_diff (float): Maximum calibrated finger position difference
        
    Returns:
        str: Winner of the game ("Player", "Computer", or "Quit")
    """
    global player_score, opponent_score, ball_speed_x, ball_speed_y
    clock = pygame.time.Clock()
    paused = False

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return "Quit"
                if event.key == pygame.K_p:
                    paused = not paused  # Toggle pause

        frame_surface = None
        
        if not paused:
            # Hand tracking & player control
            if camera is not None and camera.isOpened():
                success, frame = camera.read()
                if success:
                    frame = cv2.flip(frame, 1)
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    results = hands.process(rgb_frame)
                    
                    if results.multi_hand_landmarks:
                        hand_landmarks = results.multi_hand_landmarks[0]
                        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                        
                        wrist_y = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                        finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                        current_diff = wrist_y - finger_y
                        motion_range = max_diff - min_diff
                        
                        if motion_range > 0:
                            percentage = max(0.0, min(1.0, (current_diff - min_diff) / motion_range))
                            target_y = HEIGHT - (percentage * HEIGHT)
                            player_paddle.centery += (target_y - player_paddle.centery) * Config.SMOOTHING_FACTOR
                    
                    frame_surface = pygame.surfarray.make_surface(
                        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).swapaxes(0, 1)
                    )

            # Simple opponent AI
            if opponent_paddle.centery < ball.centery:
                opponent_paddle.y += Config.OPPONENT_SPEED
            if opponent_paddle.centery > ball.centery:
                opponent_paddle.y -= Config.OPPONENT_SPEED

            # Ball physics: update trail first
            for i in range(Config.TRAIL_COUNT - 1, 0, -1):
                trail_rects[i].center = trail_rects[i - 1].center
            trail_rects[0].center = ball.center

            # Move ball
            ball.x += ball_speed_x
            ball.y += ball_speed_y

            # Collisions: walls
            if ball.top <= 0 or ball.bottom >= HEIGHT:
                ball_speed_y *= -1

            # Collisions: paddles
            if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
                ball_speed_x *= -1
                new_speed_x = random.randint(Config.BALL_COLLISION_SPEED_MIN, Config.BALL_COLLISION_SPEED_MAX)
                sign_x = 1 if ball_speed_x > 0 else -1
                ball_speed_x = new_speed_x * sign_x
                ball_speed_y += random.uniform(-3, 3)
                
                if abs(ball_speed_y) < Config.BALL_MIN_VERTICAL_SPEED:
                    sign_y = 1 if ball_speed_y >= 0 else -1
                    ball_speed_y = Config.BALL_MIN_VERTICAL_SPEED * sign_y

            # Scoring & win condition
            if ball.left <= 0:
                opponent_score += 1
                if opponent_score >= Config.WINNING_SCORE:
                    return "Computer"
                reset_ball()
            if ball.right >= WIDTH:
                player_score += 1
                if player_score >= Config.WINNING_SCORE:
                    return "Player"
                reset_ball()

            # Paddle bounds
            player_paddle.top = max(0, player_paddle.top)
            player_paddle.bottom = min(HEIGHT, player_paddle.bottom)
            opponent_paddle.top = max(0, opponent_paddle.top)
            opponent_paddle.bottom = min(HEIGHT, opponent_paddle.bottom)

        # --- Render (runs even when paused) ---
        draw_elements(frame_surface)

        if paused:
            pause_text = pause_font.render("PAUSED", True, Config.WHITE)
            text_rect = pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(pause_text, text_rect)

        pygame.display.flip()
        clock.tick(Config.FPS)


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main entry point for the game."""
    if camera is None or not camera.isOpened():
        print("\nError: Cannot start game without a working camera.")
        print("Please check your webcam and try again.")
        input("Press Enter to exit...")
        safe_exit()
    
    # Main game loop (enables "Play Again" functionality)
    while True:
        reset_game_state()
        start_screen()

        # Calibrate hand tracking
        min_val, max_val = calibrate_finger()
        
        # Run game
        winner = game_loop(min_val, max_val)

        if winner == "Quit":
            break

        # Show game over screen and check if user wants to play again
        play_again = game_over_screen(winner)
        if not play_again:
            break

    safe_exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
        safe_exit()
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()
        safe_exit()
