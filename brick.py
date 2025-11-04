"""
Brick Class for BreakOut Clone Game
Author: Hemant Vijay
Last Updated: 4-Nov-2025

This file defines the Brick class which represents the colored bricks at the top
of the screen. These bricks are destroyed when the ball hits them, and the player
earns points. The game is won when all bricks are destroyed.

Project Credit: This project is part of the assignment for Angela Yu's course
"100 Days of Code: The Complete Python Pro Bootcamp"
Course URL: https://www.udemy.com/course/100-days-of-code/
"""

from turtle import Turtle

# Constants for brick properties
BRICK_WIDTH = 3  # Width of each brick (stretches horizontally)
BRICK_HEIGHT = 1  # Height of each brick (stretches vertically)
BRICK_COLORS = ["red", "orange", "yellow", "green", "blue"]  # Different colors for brick rows


class Brick(Turtle):
    """
    The Brick class creates a single brick that can be destroyed by the ball.
    When the ball hits a brick, the brick disappears and the player scores points.
    Different colored bricks may be worth different point values.
    """

    def __init__(self, position, color):
        """
        Initialize a brick at a specific position with a specific color.

        Args:
            position: A tuple (x, y) representing where to place the brick
            color: The color of the brick (affects its appearance)
        """
        super().__init__()  # Initialize the parent Turtle class

        # Set up the brick's appearance
        self.shape("square")  # Start with a square shape
        self.color(color)  # Set the brick color based on its row
        self.shapesize(stretch_wid=BRICK_HEIGHT, stretch_len=BRICK_WIDTH)  # Stretch to brick shape
        self.penup()  # Don't draw lines when moving
        self.goto(position)  # Move to the specified position

    def destroy(self):
        """
        Remove the brick from the screen when it's hit by the ball.
        This makes the brick disappear and allows the ball to pass through.
        """
        # Hide the brick by making it invisible
        self.goto(1000, 1000)  # Move off-screen
        self.hideturtle()  # Make it invisible


class BrickManager:
    """
    The BrickManager class creates and manages all the bricks in the game.
    It creates a grid of colored bricks at the top of the screen and
    provides methods to check for collisions and remove bricks.
    """

    def __init__(self):
        """
        Initialize the brick manager and create the initial grid of bricks.
        """
        self.bricks = []  # List to store all brick objects
        self.create_bricks()  # Create the initial brick layout

    def create_bricks(self):
        """
        Create a grid of colored bricks at the top of the screen.
        The bricks are arranged in rows with different colors.
        Each row has a specific color from the BRICK_COLORS list.
        """
        # Starting position for the first brick (top-left area)
        start_x = -360  # Left side of the screen
        start_y = 250  # Near the top of the screen

        # Space between bricks
        brick_spacing_x = 65  # Horizontal space between brick centers
        brick_spacing_y = 25  # Vertical space between rows

        # Create 5 rows of bricks
        for row in range(5):
            # Each row has a different color from the BRICK_COLORS list
            color = BRICK_COLORS[row]

            # Create 11 bricks in each row
            for col in range(11):
                # Calculate the position for this brick
                x_pos = start_x + (col * brick_spacing_x)
                y_pos = start_y - (row * brick_spacing_y)

                # Create a new brick at this position
                brick = Brick((x_pos, y_pos), color)

                # Add the brick to our list
                self.bricks.append(brick)

    def check_collision(self, ball):
        """
        Check if the ball has collided with any brick.
        If a collision is detected, destroy the brick and return the score value.

        Args:
            ball: The ball object to check for collisions

        Returns:
            The point value of the destroyed brick, or 0 if no collision
        """
        # Loop through all bricks to check for collision
        for brick in self.bricks:
            # Check if the ball is close enough to this brick to count as a hit
            # We use distance() to measure how close the ball is to the brick center
            if brick.distance(ball) < 40:  # 40 pixels is the collision threshold
                # Destroy the brick
                brick.destroy()

                # Remove the brick from our list
                self.bricks.remove(brick)

                # Calculate points based on brick color (higher rows = more points)
                if brick.color()[0] == "red":
                    return 10  # Red bricks worth 10 points
                elif brick.color()[0] == "orange":
                    return 8  # Orange bricks worth 8 points
                elif brick.color()[0] == "yellow":
                    return 6  # Yellow bricks worth 6 points
                elif brick.color()[0] == "green":
                    return 4  # Green bricks worth 4 points
                elif brick.color()[0] == "blue":
                    return 2  # Blue bricks worth 2 points

        # No collision detected
        return 0

    def all_bricks_destroyed(self):
        """
        Check if all bricks have been destroyed (game won).

        Returns:
            True if no bricks remain, False otherwise
        """
        return len(self.bricks) == 0
