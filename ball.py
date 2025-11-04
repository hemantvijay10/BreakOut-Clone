"""
Ball Class for BreakOut Clone Game
Author: Hemant Vijay
Last Updated: 4-Nov-2025

This file defines the Ball class which represents the bouncing ball in the game.
The ball moves continuously, bounces off walls, the paddle, and bricks.
The ball's speed increases slightly with each paddle bounce to increase difficulty.

Project Credit: This project is part of the assignment for Angela Yu's course
"100 Days of Code: The Complete Python Pro Bootcamp"
Course URL: https://www.udemy.com/course/100-days-of-code/
"""

from turtle import Turtle

# Constants for ball properties
BALL_COLOR = "white"  # Color of the ball
BALL_SIZE = 1  # Size of the ball (1 = normal size)
INITIAL_MOVE_SPEED = 10  # Starting speed of the ball in pixels
SPEED_INCREMENT = 1.1  # How much faster the ball gets after hitting paddle


class Ball(Turtle):
    """
    The Ball class creates a bouncing ball that moves around the screen.
    The ball bounces off the walls, paddle, and bricks.
    If the ball falls off the bottom, the player loses a life.
    """

    def __init__(self):
        """
        Initialize the ball at the center of the screen.
        The ball starts moving in an upward diagonal direction.
        """
        super().__init__()  # Initialize the parent Turtle class

        # Set up the ball's appearance
        self.shape("circle")  # Make it a circular ball
        self.color(BALL_COLOR)  # Make it white to stand out
        self.shapesize(stretch_wid=BALL_SIZE, stretch_len=BALL_SIZE)  # Normal size
        self.penup()  # Don't draw lines when moving

        # Set up ball movement direction
        # x_move and y_move control the direction and speed of the ball
        self.x_move = INITIAL_MOVE_SPEED  # Move right initially
        self.y_move = INITIAL_MOVE_SPEED  # Move up initially
        self.move_speed = 0.1  # Time delay between moves (lower = faster)

    def move(self):
        """
        Move the ball by updating its position based on x_move and y_move.
        This method is called repeatedly in the game loop to animate the ball.
        """
        # Calculate new position
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        # Move to new position
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Bounce the ball vertically (reverse its up/down direction).
        This happens when the ball hits the top wall or the paddle.
        """
        # Reverse the y direction (if going up, now go down, and vice versa)
        self.y_move *= -1

    def bounce_x(self):
        """
        Bounce the ball horizontally (reverse its left/right direction).
        This happens when the ball hits the left or right walls.
        """
        # Reverse the x direction (if going right, now go left, and vice versa)
        self.x_move *= -1

    def increase_speed(self):
        """
        Increase the ball's speed slightly to make the game more challenging.
        This is called each time the ball successfully bounces off the paddle.
        """
        # Reduce the move_speed delay to make the ball faster
        self.move_speed *= 0.9

    def reset_position(self):
        """
        Reset the ball to the center of the screen after a player loses a life.
        The ball also bounces in the opposite direction to give the player time to prepare.
        """
        # Move ball back to center
        self.goto(0, 0)

        # Reset the speed to initial value
        self.move_speed = 0.1

        # Reverse the y direction so the ball goes in opposite direction
        self.bounce_y()
