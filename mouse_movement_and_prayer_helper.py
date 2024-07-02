import pynput
from utils import keyboard
from utils import cursor
from utils import randomizations
import pyautogui
from humancursor.utilities.human_curve_generator import HumanizeMouseTrajectory
from humancursor.utilities.calculate_and_randomize import (
    generate_random_curve_parameters,
)
import collections

Point = collections.namedtuple("Point", "x y")


multiplier = 3
prayer_polygons = {
    "mage": [
        (1537, 907),
        (1538, 849),
        (1600, 854),
        (1596, 918),
    ],
    "ranged": [
        (1639, 909),
        (1638, 850),
        (1692, 851),
        (1692, 913),
    ],
    "melee": [
        (1719, 915),
        (1724, 852),
        (1797, 848),
        (1792, 918),
    ],
    "mage_buff": [
        (1536, 1007),
        (1539, 946),
        (1597, 950),
        (1603, 1012),
    ],
    "ranged_buff": [
        (1632, 1002),
        (1630, 951),
        (1701, 953),
        (1695, 1012),
    ],
    "melee_buff": [
        (1722, 998),
        (1722, 950),
        (1797, 951),
        (1796, 1008),
    ],
}

key_to_move_mapping = {
    "q": (-39 * multiplier, 0),  # Left
    "w": (0, 35 * multiplier),  # Down
    "e": (0, -35 * multiplier),  # up
    "r": (39 * multiplier, 0),  # Right
    "z": (0, 52 * multiplier),  # Down
    "x": (0, -52 * multiplier),  # Up
    "s": (0, 82 * multiplier),  # Down
    "d": (0, -82 * multiplier),  # up
}

key_to_prayer_mapping = {
    "q": "mage",
    "a": "mage_buff",
    "w": "ranged",
    "s": "ranged_buff",
    "e": "melee",
    "d": "melee_buff",
}


def pray(prayer):
    keyboard.press("f2")
    from_point = pyautogui.position()
    to_point = Point(*randomizations.random_point_in_polygon(prayer_polygons[prayer]))
    print(from_point)
    print(to_point)
    (
        offset_boundary_x,
        offset_boundary_y,
        knots_count,
        distortion_mean,
        distortion_st_dev,
        distortion_frequency,
        tween,
        target_points,
    ) = generate_random_curve_parameters(pyautogui, from_point, to_point)
    print(target_points)
    human_curve = HumanizeMouseTrajectory(
        from_point,
        to_point,
        offset_boundary_x=offset_boundary_x,
        offset_boundary_y=offset_boundary_y,
        knots_count=knots_count,
        distortion_mean=distortion_mean,
        distortion_st_dev=distortion_st_dev,
        distortion_frequency=distortion_frequency,
        tween=tween,
        target_points=max(2, target_points // 10),
    )

    cursor.click_polygon(
        prayer_polygons[prayer],
        av_speed=0.005,
        disable_offset=True,
        curve=human_curve,
        ignore_post_randomness=True,
        ignore_predictive_movement=True,
    )


paused = False
ctrl_pressed = False


def on_press(key):
    global paused
    global ctrl_pressed
    try:
        if key == pynput.keyboard.Key.ctrl_l or key == pynput.keyboard.Key.ctrl_r:
            ctrl_pressed = True
            return

        if ctrl_pressed and key == pynput.keyboard.KeyCode.from_char("m"):
            paused = not paused
            ctrl_pressed = False
            return

        if not paused:
            if key.char in key_to_prayer_mapping:
                pray(key_to_prayer_mapping[key.char])
            # if key.char in key_to_move_mapping:
            # cursor.move_offset(*key_to_move_mapping[key.char], av_speed=0.0005)
            # elif key.char == "c":
            # cursor.click(button="left")
            # elif key.char == "f":
            # cursor.click(button="right")

    except AttributeError:
        pass


def on_release(key):
    global ctrl_pressed

    if key == pynput.keyboard.Key.ctrl_l or key == pynput.keyboard.Key.ctrl_r:
        ctrl_pressed = False


with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
