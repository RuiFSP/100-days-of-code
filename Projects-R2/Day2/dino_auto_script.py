import pyautogui
from time import sleep
from PIL import ImageGrab, ImageOps
import time

REPLAY_BUTTON_COORDINATES = (2883, 583)
DINO_COORDINATES = (65, 575, 220, 690)
CHECKER_DELTA = 195


def image_grab() -> int:
    """
    Grab an image of the game and return the sum of the pixels in the obstacle area.

    Returns:
        int: the sum of the pixels in the obstacle area.
    """
    bbox_obstacle_checker = (
        DINO_COORDINATES[0] + CHECKER_DELTA, DINO_COORDINATES[1], DINO_COORDINATES[2] + CHECKER_DELTA,
        DINO_COORDINATES[3])
    img_checker = ImageGrab.grab(bbox_obstacle_checker)
    gray_img_checker = ImageOps.grayscale(img_checker)
    sum_target = sum(map(sum, gray_img_checker.getcolors()))
    return sum_target


def jump() -> None:
    """
    Simulates a spacebar key press and release to make the dinosaur jump.
    """
    pyautogui.keyDown('space')
    sleep(0.001)
    pyautogui.keyUp('space')
    sleep(0.001)


def restart() -> None:
    """
    Clicks on the replay button to restart the game.
    """
    pyautogui.click(REPLAY_BUTTON_COORDINATES)


def main() -> None:
    """
    Plays the Chrome Dino game automatically.

    It continuously captures screenshots of the game, checks for obstacles,
    and jumps whenever there is an obstacle in front of the dino.
    """
    jump()
    successful_jumps = 0
    restart()
    # Click inside the browser window to give it focus
    browser_x, browser_y = (500, 500)  # Replace with the coordinates of a point inside the browser window
    pyautogui.click(browser_x, browser_y)

    while True:
        try:
            # Check if there is an obstacle
            if image_grab() != 17858:
                print(f"Obstacle , time to jump 😀, you did {successful_jumps} jumps")
                jump()
                successful_jumps += 1
        except Exception as e:
            print(f"Encountered an error: {e}")
            # Restart the game to recover from the error
            restart()
            time.sleep(2)
            # Click inside the browser window to give it focus
            pyautogui.click(browser_x, browser_y)


if __name__ == "__main__":
    # Open the game in the Chrome browser
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('chrome://dino')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('space')

    main()
