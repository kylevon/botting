import easyocr
from PIL import ImageGrab
import numpy as np
import pyautogui
from pynput import keyboard
from .screen_finder import obtain_offset
from . import randomizations
from humancursor import SystemCursor

cursor = SystemCursor()


# Initialize easyocr reader
reader = easyocr.Reader(["en"])


def capture_text_below_mouse():
    x, y = pyautogui.position()
    region = (x, y, x + 180, y + 70)  # (left, top, right, bottom)
    screen = ImageGrab.grab(bbox=region)
    img = np.array(screen)
    result = reader.readtext(img)
    text = " ".join([res[1] for res in result])
    return text.strip()


def get_current_player_position():
    offset = obtain_offset()
    dx, dy = offset
    min_x = 233 + dx
    max_x = 279 + dx
    min_y = 218 + dy
    max_y = 265 + dy
    cursor.move_to()

    x, y = pyautogui.position()
    print(f"Current relative_mouse_position is: {x - dx}, {y - dy}")


def on_press(key):
    try:
        if key.char == "r":
            location_text = capture_text_below_mouse()
            print(get_current_player_position())
            print(f"Current Location: {location_text}")
    except AttributeError:
        pass


def main():
    print("Press 'r' to capture text below the mouse cursor. Press 'esc' to quit.")

    # Start listening to the keyboard events
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
