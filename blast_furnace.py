from utils import antiban_motions
from utils import randomizations
from utils import keyboard
from utils import cursor
from utils import game_information
from utils.logout import logout
from utils.obtain_polygon import obtain_polygon
from utils.constants import colors
from utils.constants import polygons
import time
import pyautogui
import random
import json


bank_minimap_location = [
    (669, 49),
    (658, 47),
    (658, 27),
    (672, 31),
]

ordan_minimap_location = [
    (614, 134),
    (612, 122),
    (596, 127),
    (607, 135),
]


def get_integer_input(prompt: str) -> int:
    while True:
        try:
            user_input = int(input(prompt + ": "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")


class SteelBarMaker:
    def __init__(self):
        # load_file = get_integer_input("Use previous configs? (1 = yes, 0 = no)")
        self.first_loop = True

    def save(self, save_path):
        with open(save_path, "w") as f:
            json.dump(self.__dict__, f)

    def load(self, save_path):
        with open(save_path, "r") as f:
            data = json.load(f)
            self.__dict__.update(data)

    def do_a_loop(self) -> float:
        for i in range(5):
            cursor.click_polygon(polygons.get_inventory_polygon(0, 0))
            if i != 0:
                cursor.click_polygon(polygons.get_inventory_polygon(0, 1))
            cursor.click_polygon(
                polygons.get_bank_polygon(0, 3),
                ignore_post_randomness=True,
                ignore_predictive_movement=True,
            )
            cursor.click_polygon(
                polygons.bank_close,
                ignore_post_randomness=True,
                ignore_predictive_movement=True,
            )
            randomizations.sleep_a_tick()
            previous_exp = game_information.get_total_exp()
            cursor.click_color_polygon(
                colors.GREEN,
                ignore_post_randomness=True,
                ignore_predictive_movement=False,
            )
            randomizations.sleep_at_least(6.5)
            if game_information.get_inventory_slot(2) is not None:
                print(f"Inventory is {game_information.get_inventory()}")
                cursor.click_color_polygon(
                    colors.GREEN,
                    ignore_post_randomness=True,
                    ignore_predictive_movement=False,
                )
                randomizations.sleep_at_least(4)
                if game_information.get_inventory_slot(2) is not None:
                    raise Exception("An error occured")
            print("Clicking")
            cursor.click_polygon(
                polygons.inventory_polygons[0],
                ignore_post_randomness=True,
                ignore_predictive_movement=True,
            )
            cursor.click_color_polygon(
                colors.GREEN,
                ignore_post_randomness=True,
                ignore_predictive_movement=False,
            )
            randomizations.sleep_a_tick()
            if game_information.get_inventory_slot(2) is not None:
                cursor.click_color_polygon(
                    colors.GREEN,
                    ignore_post_randomness=True,
                    ignore_predictive_movement=False,
                )
                randomizations.sleep_at_least(1)
                if game_information.get_inventory_slot(2) is not None:
                    raise Exception("An error occured, throwing bars")
            cursor.move_to_color_polygon(colors.BLUE)
            while game_information.get_total_exp() == previous_exp:
                randomizations.sleep_a_tick()
            cursor.click_color_polygon(
                colors.BLUE,
                ignore_post_randomness=True,
                ignore_predictive_movement=False,
            )
            randomizations.sleep_at_least(3.7)
            keyboard.press("space")
            randomizations.sleep_a_tick()
            randomizations.sleep_a_tick()
            if game_information.get_inventory_slot(2) is None:
                cursor.click_color_polygon(
                    colors.BLUE,
                    ignore_post_randomness=True,
                    ignore_predictive_movement=False,
                )
                randomizations.sleep_at_least(2)
                keyboard.press("space")
                randomizations.sleep_a_tick()
                randomizations.sleep_a_tick()
                if game_information.get_inventory_slot(2) is None:
                    raise Exception("An error occured, did not receive bars ")
            cursor.click_color_polygon(
                colors.PINK,
                ignore_post_randomness=True,
                ignore_predictive_movement=False,
            )
            randomizations.sleep_at_least(4.43)
        cursor.click_polygon(
            polygons.inventory_polygons[1],
            ignore_post_randomness=True,
            ignore_predictive_movement=True,
        )
        cursor.click_polygon(
            polygons.bank_polygons[5],
            ignore_post_randomness=True,
            ignore_predictive_movement=True,
        )
        cursor.click_polygon(
            polygons.bank_close,
            ignore_post_randomness=True,
            ignore_predictive_movement=True,
        )
        cursor.click_polygon(
            polygons.inventory_polygons[1],
            ignore_post_randomness=True,
            ignore_predictive_movement=True,
        )
        randomizations.sleep_a_tick()
        cursor.click_color_polygon(
            colors.PINK,
            ignore_post_randomness=True,
            ignore_predictive_movement=True,
        )
        randomizations.sleep_a_tick()
        return 0.1


def main() -> None:
    configs = SteelBarMaker()
    try:
        while True:
            time.sleep(configs.do_a_loop())
    except Exception as err:
        print(err)
        print("An Error Occured, logging out!")
        logout()





if __name__ == "__main__":
    main()
