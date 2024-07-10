from utils import antiban_motions
from utils import randomizations
from utils import keyboard
from utils import cursor
from utils import tui
from utils import game_information
from utils.logout import logout
from utils.obtain_polygon import obtain_polygon
from utils.constants import colors
from utils.constants import polygons
import time
import pyautogui
import random
import json

spin_flax_polygon = [
    (614, 290),
    (613, 274),
    (630, 274),
    (631, 290),
]


class SpinFlax:
    def __init__(self):
        # load_file = tui.get_integer_input("Use previous configs? (1 = yes, 0 = no)")
        # if load_file == 1:
        # self.load("previous_super_glass_make_configs.json")
        # else:
        self.sand_coords = {"column": 3, "row": 4}
        self.seaweed_coords = {"column": 4, "row": 4}
        self.previous_exp = 0
        # self.save("previous_super_glass_make_configs.json")

    def do_a_loop(self) -> int:
        # Returns time to wait
        if self.previous_exp == 0:
            keyboard.press("f1")
        current_exp = game_information.get_total_exp()
        if current_exp == self.previous_exp:
            raise Exception("Didn't increase exp!")
        self.previous_exp = current_exp
        cursor.click_polygon(polygons.get_inventory_polygon(0,0))
        cursor.click_color_polygon(colors.BLUE)
        randomizations.sleep_at_least(1.4)
        keyboard.press("1")
        randomizations.sleep_at_least(0.1)
        keyboard.press("f3")
        cursor.click_polygon(spin_flax_polygon, ignore_post_randomness=True, ignore_predictive_movement=True)
        for _ in range(4):
            randomizations.sleep_at_least(2.3)
            cursor.click_polygon(spin_flax_polygon, ignore_post_randomness=True, ignore_predictive_movement=True)
        randomizations.sleep_at_least(1)
        keyboard.press("f1")
        randomizations.sleep_at_least(1)
        cursor.click_polygon(polygons.get_inventory_polygon(1, 0))
        cursor.click_color_polygon(colors.PINK)
        randomizations.sleep_at_least(1.4)
        keyboard.press("4")
        return 0.6


def main() -> None:
    configs = SpinFlax()
    try:
        while True:
            time.sleep(configs.do_a_loop())
    except Exception as error:
        print(error)
        print("Logging out!")
        # logout()


if __name__ == "__main__":
    main()
