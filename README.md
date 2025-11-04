# BreakOut Clone Game

Author: Hemant Vijay
Last Updated: 4-Nov-2025

## Project Overview

This is a Python implementation of the classic 1980s arcade game BreakOut. The game features a controllable paddle, a bouncing ball, and colorful bricks that the player must destroy to win. Built using Python's Turtle graphics library, this project demonstrates fundamental game development concepts including object oriented programming, collision detection, and game loop mechanics.

## Course Credit

This project is part of the assignment for Angela Yu's course "100 Days of Code: The Complete Python Pro Bootcamp" available on Udemy.

Course URL: https://www.udemy.com/course/100-days-of-code/
Practice Assignment: https://www.udemy.com/course/100-days-of-code/learn/practice/1251140#overview

Instructor: Angela Yu
Student Developer: Hemant Vijay

## How to Play

The objective is simple: destroy all the colored bricks at the top of the screen without letting the ball fall off the bottom.

**Controls:**
* Press the Left Arrow key to move the paddle left
* Press the Right Arrow key to move the paddle right

**Game Rules:**
* You start with 3 lives
* Keep the ball bouncing by hitting it with your paddle
* Each brick destroyed earns you points
* Red bricks are worth 10 points
* Orange bricks are worth 8 points
* Yellow bricks are worth 6 points
* Green bricks are worth 4 points
* Blue bricks are worth 2 points
* If the ball falls off the bottom, you lose one life
* The game ends when you run out of lives or destroy all bricks
* The ball gets slightly faster each time it bounces off the paddle

## System Requirements

This game is compatible with the following operating systems:

* Windows 11 Pro 64 bit and later versions
* Ubuntu 24.04.3 LTS and later versions

**Required Software:**
* Python 3.6 or higher
* Python Turtle graphics library (included with Python standard library)

## Installation and Setup

1. Make sure Python 3.6 or higher is installed on your system
2. Download or clone this repository to your computer
3. Navigate to the project directory
4. No additional packages need to be installed as the game uses only Python standard libraries

## Running the Game

Open a terminal or command prompt in the project directory and run:

```
python main.py
```

On some systems you may need to use:

```
python3 main.py
```

The game window will open and you can start playing immediately using the arrow keys.

## Project Structure

The project is organized into multiple Python files for better code organization:

**main.py**
The main game file that sets up the screen, creates game objects, handles the game loop, and manages game logic including collision detection and win/lose conditions.

**paddle.py**
Defines the Paddle class which creates the player controlled paddle at the bottom of the screen. Handles left and right movement with boundary checking to prevent the paddle from moving off screen.

**ball.py**
Defines the Ball class which creates the bouncing ball. Includes methods for movement, bouncing in different directions, speed increases, and resetting position when a life is lost.

**brick.py**
Defines both the Brick class (individual bricks) and BrickManager class (manages all bricks). Creates the colorful brick layout, handles collision detection with the ball, and tracks when all bricks are destroyed.

**scoreboard.py**
Defines the Scoreboard class which displays the current score and remaining lives at the top of the screen. Updates the display when points are earned or lives are lost, and shows game over or victory messages.

**LICENSE.txt**
Contains project credits, copyright information, third party library acknowledgments, and the MIT license under which this software is distributed.

**README.md**
This file, providing comprehensive documentation about the project, how to play, system requirements, and project structure.

## Features

* Classic BreakOut gameplay with smooth animation
* Five rows of colored bricks with different point values
* Progressive difficulty as the ball speed increases
* Score tracking and lives system
* Collision detection for walls, paddle, and bricks
* Win and lose conditions with appropriate messages
* Keyboard controls for paddle movement
* Clean object oriented code structure
* Extensive comments explaining the code logic

## Technical Implementation

The game uses Python's Turtle graphics library, which provides a simple way to create 2D graphics and animations. The project demonstrates several important programming concepts:

**Object Oriented Programming:** Each game component (paddle, ball, bricks, scoreboard) is implemented as a class, making the code modular and maintainable.

**Game Loop:** The main game loop continuously updates the game state, checking for collisions, updating positions, and redrawing the screen.

**Collision Detection:** Uses distance calculations to detect when the ball hits the paddle or bricks, and boundary checks for wall collisions.

**Event Handling:** Keyboard input is captured and processed to control the paddle movement in real time.

**State Management:** Tracks game state including score, lives, ball position and velocity, and brick status.

## Learning Outcomes

By studying this project, you will learn:

* How to structure a complete game project with multiple classes
* Implementing game physics like ball movement and bouncing
* Collision detection techniques
* Managing game state and win/lose conditions
* Creating interactive graphics with Python Turtle
* Writing clean, well documented code
* Object oriented programming principles in practice

## Credits and Acknowledgments

**Course Instructor:** Angela Yu
**Developer:** Hemant Vijay
**Original Game:** BreakOut (Atari, 1976)

This project uses only Python standard libraries:
* turtle (graphics and animation)
* time (game timing and speed control)

Both libraries are part of the Python Standard Library and licensed under the Python Software Foundation License.

## License

This project is licensed under the MIT License. See LICENSE.txt for full details.

Copyright 2025 Hemant Vijay

Permission is granted to use, modify, and distribute this software for educational and personal purposes with proper attribution to the original course and instructor.

## Support and Contact

This is an educational project created as part of a programming course. For questions about the course content, please refer to the Udemy course page linked above.

For technical issues with this specific implementation, please review the code comments and documentation provided within each Python file.

## Version History

**Version 1.0** (4-Nov-2025)
* Initial release
* Complete game implementation with all core features
* Full documentation and code comments
* Tested on Windows 11 Pro and Ubuntu 24.04.3 LTS

Enjoy playing BreakOut Clone!
