import cv2
import numpy as np
def hex_to_bgr(hex_color):
    """
    Convert a HEX color string to BGR format.
    
    :param hex_color: A string representing the HEX color (e.g., "#FFFFFF" for white).
    :return: A tuple representing the BGR color.
    """
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return rgb[::-1]  # Convert RGB to BGR

def from_color(hex_color, tolerance=0):
    """
    Detects a polygon on the screen with a specified pixel color in HEX format and returns its vertices.

    :param hex_color: A string representing the HEX color to detect (e.g., "#FF0000" for red).
    :param tolerance: The tolerance for color matching.
    :return: A list of vertices of the detected polygon.
    """
    # Convert HEX color to BGR
    target_color = hex_to_bgr(hex_color)
    
    # Take a screenshot of the current screen
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Define the lower and upper bounds of the target color
    lower_bound = np.array([max(c - tolerance, 0) for c in target_color])
    upper_bound = np.array([min(c + tolerance, 255) for c in target_color])

    # Create a mask for the target color
    mask = cv2.inRange(screenshot, lower_bound, upper_bound)

    # Find the coordinates of all pixels that match the target color
    coordinates = np.column_stack(np.where(mask == 255))

    return coordinates
