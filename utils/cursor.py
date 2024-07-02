import numpy as np
from humancursor import SystemCursor
import pyautogui
import time
from .screen_finder import obtain_offset
from . import randomizations
from pynput import mouse, keyboard
import random
from .detect_color_polygon import GREEN, RED, BLUE, YELLOW, detect_color_polygon
from collections import deque
from scipy.stats import norm

_cursor = SystemCursor()
_mouse_controller = mouse.Controller()

positions = deque(maxlen=40)  # Cache only the last 40 positions


def scroll_in():
    time = 0.4 + random.expovariate(0.1)
    pyautogui.scroll(10, duration=time)


def scroll_out():
    time = 0.4 + random.expovariate(0.1)
    pyautogui.scroll(-10, duration=time)


def move_to(x, y, av_speed=0.4, disable_offset=False, curve=None, store_position=True):
    if disable_offset:
        dx, dy = 0, 0
    else:
        dx, dy = obtain_offset()

    if x < 1:
        x = 1
    if y < 1:
        y = 1

    duration = (av_speed / 2) + random.expovariate(1 / (av_speed / 2))
    while duration > 2 * av_speed:
        duration = (av_speed / 2) + random.expovariate(1 / (av_speed / 2))
    print(f"movement duration: {duration}")
    _cursor.move_to([x + dx, y + dy], duration=duration, steady=True, human_curve=curve)
    if store_position:
        positions.append((x + dx, y + dy))


def move_offset(dx, dy, av_speed=0.4):
    duration = (3 * av_speed / 4) + random.expovariate(4 / av_speed)
    print(f"Offset movement duration: {duration}")
    x, y = _mouse_controller.position
    _cursor.move_to([x + dx, y + dy], duration=duration, steady=True)


def click(duration=0.05, button="left"):
    click_duration = 0.05 + random.expovariate(10)
    print(f"Click_duration = {click_duration}")
    pyautogui.mouseDown(button=button)
    time.sleep(click_duration)
    pyautogui.mouseUp(button=button)


def predict_next_position(current_position):
    if len(positions) < 2:
        return None

    # Extract x and y coordinates from the deque
    xs, ys = zip(*positions)

    # Fit Gaussian distributions to the x and y coordinates
    mu_x, std_x = np.mean(xs), np.std(xs)
    mu_y, std_y = np.mean(ys), np.std(ys)

    # Adjust the mean based on the current position
    alpha = 0.5  # weight for current position
    mu_x = alpha * current_position[0] + (1 - alpha) * mu_x
    mu_y = alpha * current_position[1] + (1 - alpha) * mu_y

    # Predict the next position
    next_x = norm(mu_x, std_x).rvs()
    next_y = norm(mu_y, std_y).rvs()

    return next_x, next_y


def click_at(
    x,
    y,
    av_speed=0.4,
    disable_offset=False,
    curve=None,
    ignore_post_randomness=False,
    ignore_predictive_movement=True,
):
    move_to(x, y, av_speed=av_speed, disable_offset=disable_offset, curve=curve)
    click_duration = 0.05 + random.expovariate(10)
    print(f"Click_duration = {click_duration}, x,y: {x}, {y}")
    pyautogui.mouseDown()
    time.sleep(click_duration)
    pyautogui.mouseUp()
    if not ignore_post_randomness:
        if random.randint(0, 4) <= 3:
            move_offset(random.gauss(0, 10), random.gauss(0, 10))
    if not ignore_predictive_movement:
        prediction = predict_next_position((x, y))
        if prediction is not None:
            next_x, next_y = prediction
        else:
            next_x, next_y = (0, 0)
        move_to(
            next_x + random.gauss(0, 10),
            next_y + random.gauss(0, 10),
            store_position=False,
        )


def move_to_polygon(polygon, av_speed=0.4, disable_offset=False, curve=None):
    move_to(
        *randomizations.random_point_in_polygon(polygon),
        av_speed=av_speed,
        disable_offset=disable_offset,
        curve=curve,
    )


def move_to_color_polygon(color, av_speed=0.4, curve=None):
    move_to_polygon(
        detect_color_polygon(*color),
        av_speed=av_speed,
        disable_offset=True,
        curve=curve,
    )


def click_polygon(
    polygon,
    av_speed=0.4,
    disable_offset=False,
    curve=None,
    ignore_predictive_movement=True,
    ignore_post_randomness=False,
):
    click_at(
        *randomizations.random_point_in_polygon(polygon),
        av_speed=av_speed,
        disable_offset=disable_offset,
        curve=curve,
        ignore_predictive_movement=ignore_predictive_movement,
        ignore_post_randomness=ignore_post_randomness,
    )


def click_color_polygon(
    color,
    av_speed=0.4,
    curve=None,
    click_duration=0.05,
    button="left",
    ignore_predictive_movement=True,
    ignore_post_randomness=False,
):
    click_polygon(
        detect_color_polygon(*color),
        av_speed=av_speed,
        disable_offset=True,
        curve=curve,
        ignore_predictive_movement=ignore_predictive_movement,
        ignore_post_randomness=ignore_post_randomness,
    )


def move_to_with_noise(polygon, noise=50, disable_offset=False):
    x, y = randomizations.random_point_in_polygon(polygon)
    move_to(
        x + random.gauss(0, noise),
        y + random.gauss(0, noise),
        disable_offset=disable_offset,
    )
