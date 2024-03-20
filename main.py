import cv2
import numpy as np
import pyautogui
import time

# Function to identify color
def identify_color():
    while True:
        # Get the cursor position
        x, y = pyautogui.position()

        # Get the pixel color from the screen
        screenshot = pyautogui.screenshot()
        img = np.array(screenshot)
        b, g, r = img[y, x]  # Getting BGR values of the pixel
        print("Color (BGR):", b, g, r)

        # Converting BGR to HSV
        hsv_color = cv2.cvtColor(np.uint8([[[b, g, r]]]), cv2.COLOR_BGR2HSV)
        h, s, v = hsv_color[0][0]
        print("Color (HSV):", h, s, v)

        # Wait for 50 milliseconds
        time.sleep(0.05)

# Call the function to identify color
identify_color()