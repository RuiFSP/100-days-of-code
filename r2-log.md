# #100DaysOfCode Log - Round 2 - [Rui Pinto]

The log of my <b>#100DaysOfCode</b> challenge. Started on [April 11, Sunday, 2023].

## Log

Yu [100 Days of Code: The Complete Python Pro Bootcamp for 2023](https://www.udemy.com/course/100-days-of-code/) which

All my projects and training exercises will be separated by day

- Project folder: [All Projects](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects-R2)

My working IDE

- Pycharm community version from JetBrains: https://www.jetbrains.com/pycharm/

### R2D1 --------------------------------------------------------------------------------

- Day1 - Write Python code to play the Google Dinosaur Game.
  - The game imports necessary libraries: PIL, pyautogui, cv2, numpy, and time. 
  - The game uses pyautogui to press the Windows key, type in "chrome," and press Enter to open Chrome. 
  - The game then types in the URL for the Chrome dinosaur game and presses the space bar to start the game. 
  - The game defines a function to capture a screen region where the game is located, and saves the captured screen to an image file if specified. 
  - Another function detects if the game is over by thresholding a grayscale version of the captured screen and looking for contours with an area greater than 5000 pixels. 
  - A third function detects obstacles by checking the color of a pixel at a specific coordinate on the screen. 
  - A fourth function makes the dinosaur jump by pressing the space bar. 
  - The game waits for the game to load for 2 seconds, then enters an infinite loop. 
  - In each loop iteration, the game captures the screen, checks if the game is over, and jumps if an obstacle is detected. 
  - The game waits for 0.1 seconds before checking again

The end project
is [GUI Automation Google Dinosaur Game](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects-R2/Day1)







