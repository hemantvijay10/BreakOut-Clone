"""
BreakOut Clone Game - Main Program
Author: Hemant Vijay
Last Updated: 4-Nov-2025

This is the main file that runs the BreakOut game. BreakOut is a classic arcade game
from the 1980s where a player controls a paddle to bounce a ball and destroy bricks.
The goal is to destroy all the bricks without letting the ball fall off the screen.

Game Rules:
- Use Left Arrow and Right Arrow keys to move the paddle
- Keep the ball bouncing by hitting it with the paddle
- Destroy all bricks to win the game
- You have 3 lives - if the ball falls off the screen, you lose a life
- Different colored bricks are worth different points:
  Red = 10 points, Orange = 8, Yellow = 6, Green = 4, Blue = 2

Project Credit: This project is part of the assignment for Angela Yu's course
"100 Days of Code: The Complete Python Pro Bootcamp"
Course URL: https://www.udemy.com/course/100-days-of-code/

Compatibility: Works on Windows 11 Pro 64-bit and up, Ubuntu 24.04.3 LTS and up
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import BrickManager
from scoreboard import Scoreboard
import time
import sys

# Set up the game screen
screen = Screen()
screen.title("BreakOut Clone")  # Window title
screen.bgcolor("black")  # Black background like classic arcade games
screen.setup(width=800, height=600)  # Screen dimensions: 800 pixels wide, 600 tall
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Add a flag to track if the window is still valid
# This helps prevent errors if the window is closed during gameplay
window_active = True

# Create the game objects
# The paddle is positioned at the bottom center of the screen
paddle = Paddle((0, -250))

# The ball starts in the center of the screen
ball = Ball()

# The brick manager creates all the bricks at the top
brick_manager = BrickManager()

# The scoreboard displays score and lives at the top
scoreboard = Scoreboard()

# Function to handle window close event
# This prevents errors when the user closes the window during gameplay
def on_window_close():
    """
    This function is called when the user closes the game window.
    It sets a flag to stop the game loop gracefully.
    """
    global game_is_on, window_active
    game_is_on = False
    window_active = False

# Set up keyboard controls
# Listen for keyboard input
screen.listen()

# When Left Arrow is pressed, move paddle left
screen.onkey(paddle.go_left, "Left")

# When Right Arrow is pressed, move paddle right
screen.onkey(paddle.go_right, "Right")

# Set up the window close handler
# This ensures the program exits gracefully when the window is closed
try:
    screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_window_close)
except:
    # If protocol setup fails, continue anyway (for compatibility)
    pass

# Main game loop - this runs continuously while the game is active
game_is_on = True
while game_is_on:
    try:
        # Small delay to control game speed (makes the animation smooth)
        time.sleep(ball.move_speed)

        # Check if window is still active before updating
        if not window_active:
            break

        # Update the screen to show the latest positions
        screen.update()

        # Move the ball to its next position
        ball.move()
    except Exception as e:
        # If any graphics error occurs (like window being closed), exit gracefully
        # This prevents the TclError that can happen on Windows
        print(f"Game window was closed or an error occurred: {type(e).__name__}")
        game_is_on = False
        window_active = False
        break

    # Check if ball hits the top wall
    if ball.ycor() > 280:
        # Bounce the ball downward
        ball.bounce_y()

    # Check if ball hits the left or right walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        # Bounce the ball horizontally
        ball.bounce_x()

    # Check if ball hits the paddle
    # The ball must be close to the paddle's y position AND close to paddle horizontally
    if (ball.distance(paddle) < 50 and ball.ycor() < -230):
        # Bounce the ball upward
        ball.bounce_y()

        # Increase the ball speed slightly to make game harder
        ball.increase_speed()

    # Check if ball hits any bricks
    # This returns the point value of any destroyed brick
    points_earned = brick_manager.check_collision(ball)

    # If a brick was hit, update the score and bounce the ball
    if points_earned > 0:
        # Add points to the score
        scoreboard.increase_score(points_earned)

        # Bounce the ball downward
        ball.bounce_y()

    # Check if all bricks are destroyed (player wins)
    if brick_manager.all_bricks_destroyed():
        # Display victory message
        scoreboard.you_win()

        # End the game
        game_is_on = False

    # Check if ball falls off the bottom of the screen (player loses a life)
    if ball.ycor() < -290:
        # Reset the ball to center
        ball.reset_position()

        # Decrease lives by 1
        scoreboard.decrease_lives()

        # Check if player has run out of lives
        if scoreboard.lives <= 0:
            # Display game over message
            scoreboard.game_over()

            # End the game
            game_is_on = False

# Keep the window open until user clicks to close it
# Only call exitonclick if the window is still active
if window_active:
    try:
        screen.exitonclick()
    except:
        # If exitonclick fails (window already closed), just exit
        pass
else:
    # If window was closed during gameplay, exit cleanly
    try:
        screen.bye()
    except:
        pass
    sys.exit(0)
