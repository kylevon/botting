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
        [1534, 1055],
        [1534, 973],
        [1605, 983],
        [1601, 1055],
    ],
    "ranged": [
        [1630, 1056],
        [1634, 982],
        [1697, 982],
        [1695, 1051],
    ],
    "melee": [
        [1718, 1060],
        [1720, 980],
        [1795, 980],
        [1790, 1055],
    ],
    "mage_buff": [
        [1535, 1168],
        [1535, 1097],
        [1599, 1101],
        [1603, 1170],
    ],
    "ranged_buff": [
        [1637, 1168],
        [1635, 1095],
        [1695, 1100],
        [1695, 1172],
    ],
    "melee_buff": [
        [1727, 1168],
        [1724, 1103],
        [1797, 1102],
        [1790, 1163],
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
        target_points=max(2, target_points//10),
    )

    cursor.click_polygon(
        prayer_polygons[prayer], av_speed=0.005, disable_offset=True, curve=human_curve
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
