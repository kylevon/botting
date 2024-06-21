from typing import List, Tuple
import pyautogui
from PIL import Image, ImageDraw
import numpy as np
from . import screen_finder

def detect_color_polygon(color_low: Tuple[int, int, int], color_high: Tuple[int, int, int]) -> List[Tuple[int, int]]:
    """
    Detect all points on the current screen that match a specific range of colors.

    Parameters:
    color_low (Tuple[int, int, int]): The lower bound of the RGB color range to search for.
    color_high (Tuple[int, int, int]): The upper bound of the RGB color range to search for.

    Returns:
    List[Tuple[int, int]]: A list of points (x, y) where the color is found.
    """
    # Take a screenshot of the current screen
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.convert("RGB")
    
    # Convert the screenshot to a numpy array
    img_array = np.array(screenshot)

    # Create a mask for the color range
    mask = np.all((img_array >= color_low) & (img_array <= color_high), axis=-1)

    # Get the coordinates of the points where the mask is true
    points = np.argwhere(mask)

    # Convert the coordinates to a list of tuples (x, y) correctly
    dx, dy = screen_finder.obtain_offset()
    points = [(y, x) for x, y in points if (x - dx <= 512) and (y - dy <= 478)]
    return points

def visualize_color_points(points: List[Tuple[int, int]], save_path: str) -> None:
    """
    Visualize the detected points on the screenshot with pink color.

    Parameters:
    points (List[Tuple[int, int]]): A list of points (x, y) to highlight.
    save_path (str): Path to save the visualized image.
    """
    # Take a screenshot of the current screen
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.convert("RGB")
    
    # Create a drawing context
    draw = ImageDraw.Draw(screenshot)

    # Define the color for visualization (pink)
    pink_color = (255, 105, 180)

    # Draw small rectangles around each point to visualize them
    for point in points:
        x, y = point
        draw.rectangle([(x-2, y-2), (x+2, y+2)], fill=pink_color)

    # Save the visualized image
    screenshot.save(save_path)

# Example usage:
# target_color = (255, 0, 0)  # Red color
# points = detect_color_points(target_color)
# print(points)

YELLOW = ((236, 255, 0), (255, 255, 0))
GREEN = ((0, 213, 0), (2, 255, 2))
BLUE = ((0, 0, 205), (0, 0, 255))
RED = ((205, 0, 0), (255, 1, 1))
PINK = ((205, 0, 205), (255, 0, 255))

if __name__ == "__main__":
    # Detect a yellow box:
    visualize_color_points(detect_color_polygon(*BLUE), "out.png")
