"""
Scoreboard Class for BreakOut Clone Game
Author: Hemant Vijay
Last Updated: 4-Nov-2025

This file defines the Scoreboard class which displays the player's score and
remaining lives on the screen. It updates as the player destroys bricks and
loses lives when the ball falls off the screen.

Project Credit: This project is part of the assignment for Angela Yu's course
"100 Days of Code: The Complete Python Pro Bootcamp"
Course URL: https://www.udemy.com/course/100-days-of-code/
"""

from turtle import Turtle

# Constants for scoreboard properties
FONT = ("Courier", 16, "normal")  # Font style for displaying text
ALIGNMENT = "center"  # Center-align the text
SCORE_COLOR = "white"  # Color of the score text
STARTING_LIVES = 3  # Number of lives the player starts with


class Scoreboard(Turtle):
    """
    The Scoreboard class displays the current score and lives remaining.
    It updates whenever the player destroys a brick or loses a life.
    The scoreboard is positioned at the top of the screen.
    """

    def __init__(self):
        """
        Initialize the scoreboard with starting score and lives.
        Display the initial scoreboard at the top of the screen.
        """
        super().__init__()  # Initialize the parent Turtle class

        # Initialize score and lives
        self.score = 0  # Player starts with 0 points
        self.lives = STARTING_LIVES  # Player starts with 3 lives

        # Set up the scoreboard appearance
        self.color(SCORE_COLOR)  # Make text white
        self.penup()  # Don't draw lines
        self.hideturtle()  # Hide the turtle cursor
        self.goto(0, 270)  # Position at top center of screen

        # Display the initial scoreboard
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clear the old scoreboard and display the updated score and lives.
        This method is called whenever the score or lives change.
        """
        # Clear the previous text
        self.clear()

        # Write the new score and lives to the screen
        # Format: "Score: 0 | Lives: 3"
        self.write(f"Score: {self.score} | Lives: {self.lives}",
                   align=ALIGNMENT,
                   font=FONT)

    def increase_score(self, points):
        """
        Increase the player's score by a certain number of points.
        This is called when a brick is destroyed.

        Args:
            points: The number of points to add to the score
        """
        # Add points to the current score
        self.score += points

        # Update the display
        self.update_scoreboard()

    def decrease_lives(self):
        """
        Decrease the player's remaining lives by 1.
        This is called when the ball falls off the bottom of the screen.
        """
        # Subtract one life
        self.lives -= 1

        # Update the display
        self.update_scoreboard()

    def game_over(self):
        """
        Display a "GAME OVER" message in the center of the screen.
        This is called when the player runs out of lives.
        """
        # Move to center of screen
        self.goto(0, 0)

        # Display game over message
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 40, "bold"))

    def you_win(self):
        """
        Display a "YOU WIN!" message in the center of the screen.
        This is called when the player destroys all the bricks.
        """
        # Move to center of screen
        self.goto(0, 0)

        # Display victory message
        self.write("YOU WIN!", align=ALIGNMENT, font=("Courier", 40, "bold"))
