import PIL
import pyautogui
import cv2
import numpy as np
import time

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('chrome://dino')
pyautogui.press('enter')
pyautogui.press('space')


def capture_screen(file_name=None):
    # Get the screen size
    screen_size = pyautogui.size()

    # Define the region of interest where the game is present
    # Adjust the coordinates according to your screen resolution
    box = (0, 500, screen_size[0] - 1300, 800)

    # Capture the screen
    screen = np.array(PIL.ImageGrab.grab(bbox=box))

    print("Screen capture shape:", screen.shape)

    # Save the screen capture
    if file_name:
        PIL.Image.fromarray(screen).save(file_name)

    return screen


def detect_game_over(screen):
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    if gray is None:
        print("Error: Failed to convert screen to grayscale")
        return False
    try:
        _, binary = cv2.threshold(np.array(gray), 200, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 5000:
                return True
    except TypeError:
        print("Error: Thresholding failed.")
    return False


def detect_obstacle(screen):
    # Get the width and height of the screen capture
    height, width, _ = screen.shape

    # Define the coordinates to check for the obstacle
    check_x = int(width * 0.75)
    check_y = int(height / 2)

    # Check the color of the pixel at the specified coordinates
    pixel_color = screen[check_y, check_x]

    # Check if the pixel color indicates an obstacle
    if np.all(pixel_color == [83, 83, 83]):
        print("Pixel is the same color")
        return True

    return False


def jump():
    pyautogui.press('space')


# Wait for the game to load
time.sleep(2)

while True:
    screen = capture_screen()

    # Save the screen capture to an image file
    PIL.Image.fromarray(screen).save('screen_capture.png')

    # Check if the game is over
    if detect_game_over(screen):
        pyautogui.press('space')
        time.sleep(1)
        pyautogui.press('space')
    else:
        # Check if there's an obstacle
        if detect_obstacle(screen):
            jump()

    # Wait for 0.1 seconds before checking again
    time.sleep(0.1)
