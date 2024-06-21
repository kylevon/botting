import cv2
import numpy as np
import pyautogui
import os


# Load the inventory image in color
def obtain_offset():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, "imgs", "screen.png")
    template = cv2.imread(template_path)

    # Take a screenshot of the current screen
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Perform template matching to find the location with the highest matching score
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Get the top-left corner of the best match location
    top_left = max_loc
    height, width, _ = template.shape
    bottom_right = (top_left[0] + width, top_left[1] + height)

    # Draw a rectangle around the matched region (for visualization)
    # cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)

    # Print the location of the best match
    return top_left

    # Display the result (for debugging purposes)
    # cv2.imshow('Result', screenshot)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    print(f"Top-left corner of the best match: {obtain_offset()}")
