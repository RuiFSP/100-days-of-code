# #100DaysOfCode Log - Round 2 - [Rui Pinto]

The log of my <b>#100DaysOfCode</b> challenge. Started on [April 11, Sunday, 2023].

## Log

All my projects and training exercises will be separated by day

- Project folder: [All Projects](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects-R2)

My working IDE

- Pycharm community version from JetBrains: https://www.jetbrains.com/pycharm/

### R2D7 --------------------------------------------------------------------------------

- Day7 - Capstone Project 14/20 - Using Python Turtle, build the classic space invaders - Part 5/5
    - Set up the game screen and background
    - Create the player's spaceship, enemies, and scoring/game over system
    - Define the player's movement functions and projectile firing function
    - Define the enemy movement function and enemy projectile firing function
    - Define the collision detection function to handle when a projectile hits an enemy or the player
    - Define the explosion function to add a visual effect when a projectile hits an enemy or the player
    - Set up keyboard events to move the player's spaceship and fire projectiles
    - Use a loop to continuously update the game by moving the enemies and enemy projectiles,
    - checking for collisions, and updating the score

The end project is [Space Invaders](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects-R2/Day7)

### R2D6 --------------------------------------------------------------------------------

- Day6 - Capstone Project 14/20 - Using Python Turtle, build the classic space invaders - Part 4/5
    - Refactoring the code

The end project is [Space Invaders](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects-R2/Day6)

### R2D5 --------------------------------------------------------------------------------

- Day5 - Capstone Project 14/20 - Using Python Turtle, build the classic space invaders - Part 3/5
    - Refactoring the code
    - Incorporating sounds

The end project is [Space Invaders](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects-R2/Day5)

### R2D4 --------------------------------------------------------------------------------

- Day4 - Capstone Project 14/20 - Using Python Turtle, build the classic space invaders - Part 2/5
    - Refactoring the code

The end project is [Space Invaders](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects-R2/Day4)

### R2D3 --------------------------------------------------------------------------------

- Day3 - Capstone Project 14/20 - Using Python Turtle, build the classic space invaders - Part 1/5
    - The game involves shooting down alien ships using a space ship controlled by the player.
    - The player's space ship can move left and right using the left and right arrow keys on the keyboard.
    - The player's space ship can fire bullets using the space bar on the keyboard.
    - The game features multiple alien ships that move closer to the player's ship every second.
    - The game includes barriers that offer the player defensive positions.
    - The player must avoid colliding with the alien ships or the game will end.
    - The player can score points by shooting down alien ships, with each alien ship being worth 10 points.
    - The game features sound effects for shooting and collisions.
    - The game keeps track of the player's score and displays it on the screen.
    - The game is designed using Python Turtle, which allows for easy graphical design and animations.

The end project is [Space Invaders](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects-R2/Day3)

### R2D2 --------------------------------------------------------------------------------

- Day2 - Capstone Project 13/20 - Write Python code to play the Google Dinosaur Game - Part 2/2
    - Changed the code form yesterday and found a simpler solution:
        - This code uses Python's pyautogui module to play the Chrome Dino game automatically.
        - The image_grab() function grabs an image of the game and returns the sum of the pixels in the obstacle area.
        - The jump() function simulates a spacebar key press and release to make the dinosaur jump.
        - The restart() function clicks on the replay button to restart the game.
        - The main() function plays the game by continuously capturing screenshots of the game, checking for obstacles,
        - and jumping whenever there is an obstacle in front of the dinosaur.
        - The function also handles any exceptions that might occur during gameplay by restarting
        - the game to recover from the error.

    - At the end of the code, the game is opened in the Chrome browser and main() is called to play the game
      automatically

The end project is [GUI Dinosaur Game](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects-R2/Day2)

### R2D1 --------------------------------------------------------------------------------

- Day1 - Capstone Project 13/20 - Write Python code to play the Google Dinosaur Game - Part 1/2
    - The game imports necessary libraries: PIL, pyautogui, cv2, numpy, and time.
    - The game uses pyautogui to press the Windows key, type in "chrome," and press Enter to open Chrome.
    - The game then types in the URL for the Chrome dinosaur game and presses the space bar to start the game.
    - The game defines a function to capture a screen region where the game is located, and saves the captured screen
    - to an image file if specified.
    - Another function detects if the game is over by thresholding a grayscale version of the captured screen and
    - looking for contours with an area greater than 5000 pixels.
    - A third function detects obstacles by checking the color of a pixel at a specific coordinate on the screen.
    - A fourth function makes the dinosaur jump by pressing the space bar.
    - The game waits for the game to load for 2 seconds, then enters an infinite loop.
    - In each loop iteration, the game captures the screen, checks if the game is over, and jumps if an obstacle is
      detected.
    - The game waits for 0.1 seconds before checking again

The end project is [GUI Dinosaur Game](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects-R2/Day1)






