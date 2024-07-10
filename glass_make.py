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

super_glass_polygon = [
    (671, 279),
    (669, 261),
    (685, 264),
    (687, 279),
]


class SuperGlassMake:
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
        cursor.click_color_polygon(colors.PINK)
        time.sleep(randomizations.tick_duration())
        cursor.move_to_polygon(polygons.get_inventory_polygon(1, 0))
        time.sleep(randomizations.tick_duration() / 2)
        cursor.click()
        cursor.click_polygon(
            polygons.get_bank_polygon(**self.sand_coords),
            ignore_post_randomness=True,
            ignore_predictive_movement=True,
        )
        time.sleep(0.2)
        cursor.click()
        time.sleep(0.2)
        cursor.click()
        time.sleep(0.2)
        with pyautogui.hold("shift"):
            cursor.click()
            time.sleep(0.2)
        cursor.click_polygon(polygons.get_bank_polygon(**self.seaweed_coords))
        cursor.click_polygon(polygons.bank_close)
        current_exp = game_information.get_total_exp()
        if current_exp == self.previous_exp:
            raise Exception("Did not increase EXP!")
        else:
            self.previous_exp = current_exp
        cursor.move_to_polygon(super_glass_polygon)
        time.sleep(randomizations.tick_duration() / 2)
        cursor.click()
        return 3.3


def main() -> None:
    configs = SuperGlassMake()
    try:
        while True:
            time.sleep(configs.do_a_loop())
    except Exception as error:
        print(error)
        print("Logging out!")
        logout()


if __name__ == "__main__":
    main()
