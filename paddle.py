"""
Paddle Class for BreakOut Clone Game
Author: Hemant Vijay
Last Updated: 4-Nov-2025

This file defines the Paddle class which represents the player-controlled paddle
at the bottom of the game screen. The paddle moves left and right to bounce the ball
and prevent it from falling off the screen.

Project Credit: This project is part of the assignment for Angela Yu's course
"100 Days of Code: The Complete Python Pro Bootcamp"
Course URL: https://www.udemy.com/course/100-days-of-code/
"""

from turtle import Turtle

# Constants for paddle dimensions and movement
PADDLE_WIDTH = 5  # Width of the paddle (stretches horizontally)
PADDLE_HEIGHT = 1  # Height of the paddle (thin vertical size)
PADDLE_COLOR = "white"  # Color of the paddle on the screen
MOVE_DISTANCE = 20  # How many pixels the paddle moves per key press
SCREEN_EDGE = 350  # The right edge of the screen to prevent paddle from going off


class Paddle(Turtle):
    """
    The Paddle class creates a controllable paddle at the bottom of the screen.
    This paddle is used by the player to bounce the ball and keep it in play.
    The player can move the paddle left and right using keyboard controls.
    """

    def __init__(self, position):
        """
        Initialize the paddle at a given position on the screen.

        Args:
            position: A tuple (x, y) representing where to place the paddle
        """
        super().__init__()  # Initialize the parent Turtle class

        # Set up the paddle's appearance
        self.shape("square")  # Start with a square shape
        self.color(PADDLE_COLOR)  # Make it white to stand out on dark background
        self.shapesize(stretch_wid=PADDLE_HEIGHT, stretch_len=PADDLE_WIDTH)  # Stretch to paddle shape
        self.penup()  # Don't draw lines when moving
        self.goto(position)  # Move to starting position

    def go_left(self):
        """
        Move the paddle to the left by MOVE_DISTANCE pixels.
        This method checks that the paddle doesn't go past the left edge of the screen.
        """
        # Calculate new x position (current x minus move distance)
        new_x = self.xcor() - MOVE_DISTANCE

        # Only move if the paddle won't go past the left edge (-350 pixels)
        # We subtract half the paddle width to account for paddle size
        if new_x > -SCREEN_EDGE + (PADDLE_WIDTH * 10):
            self.goto(new_x, self.ycor())

    def go_right(self):
        """
        Move the paddle to the right by MOVE_DISTANCE pixels.
        This method checks that the paddle doesn't go past the right edge of the screen.
        """
        # Calculate new x position (current x plus move distance)
        new_x = self.xcor() + MOVE_DISTANCE

        # Only move if the paddle won't go past the right edge (350 pixels)
        # We add half the paddle width to account for paddle size
        if new_x < SCREEN_EDGE - (PADDLE_WIDTH * 10):
            self.goto(new_x, self.ycor())
