import pyautogui
import random
import time

def press(key):
    pyautogui.press(key)
    # pyautogui.keyDown(key)
    # time_to_sleep = random.gauss(0.3, 0.1)
    # while time_to_sleep < 0:
        # time_to_sleep = random.gauss(0.3, 0.1)
    # time.sleep(time_to_sleep)
    # pyautogui.keyUp(key)

def multiple_key_press(keys):
    if len(keys) == 1:
        press(keys[0])
    else:
        with pyautogui.hold(keys[0]):
            multiple_key_press(keys[1:])
