import numpy as np
from humancursor import SystemCursor
import pyautogui
import time
from .screen_finder import obtain_offset
from . import randomizations
from pynput import mouse, keyboard
import random

_cursor = SystemCursor()
_mouse_controller = mouse.Controller()


def move_to(x, y, av_speed=0.4, disable_offset=False, curve=None):
    if disable_offset:
        dx, dy = 0, 0
    else:
        dx, dy = obtain_offset()
    duration = max(0, np.random.normal(av_speed, av_speed / 4))
    _cursor.move_to([x + dx, y + dy], duration=duration, steady=True, human_curve=curve)

def move_offset(dx, dy, av_speed=0.4):
    duration = max(0, np.random.normal(av_speed, av_speed / 4))
    x, y = _mouse_controller.position
    _cursor.move_to([x + dx, y + dy], duration=duration, steady=True)

def click(duration=0.05, button='left'):
    click_duration = max(0, np.random.normal(duration, 0.005))
    pyautogui.mouseDown(button=button)
    time.sleep(click_duration)
    pyautogui.mouseUp(button=button)

def click_at(x, y, av_speed=0.4, disable_offset=False, curve=None):
    move_to(x, y, av_speed=av_speed, disable_offset=disable_offset, curve=curve)
    click_duration = max(0, np.random.normal(0.1, 0.05))
    pyautogui.mouseDown()
    time.sleep(click_duration)
    pyautogui.mouseUp()

def move_to_poligon(polygon, av_speed=0.4, disable_offset=False, curve=None):
    move_to(*randomizations.random_point_in_polygon(polygon), av_speed=av_speed, disable_offset=disable_offset, curve=curve)

def click_polygon(polygon, av_speed=0.4, disable_offset=False, curve=None):
    click_at(*randomizations.random_point_in_polygon(polygon), av_speed=av_speed, disable_offset=disable_offset, curve=curve)

def move_to_with_noise(polygon, noise=50, disable_offset=False):
    x, y = randomizations.random_point_in_polygon(polygon)
    move_to(x + random.gauss(0, noise), y + random.gauss(0, noise), disable_offset=disable_offset)
