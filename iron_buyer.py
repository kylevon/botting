from utils import antiban_motions
from utils import randomizations
from utils import keyboard
from utils import cursor
from utils import logout
from utils.obtain_polygon import obtain_polygon
from utils.constants import colors
from utils.constants import polygons
from utils import game_information
import utils.game_information
import time
import pyautogui
import random
import json
from utils import tui


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

class IronOreMaker:
    def __init__(self):
        load_file = tui.get_integer_input("Use previous configs? (1 = yes, 0 = no)")
        if load_file == 1:
            self.load("previous_iron_configs.json")
        else:
            self.bank_first_item_column = tui.get_integer_input("column of glass at bank")
            self.bank_first_item_row = tui.get_integer_input("row of glass at bank")
            print("This script will continue forever")
            self.save("previous_iron_configs.json")
        self.first_loop = True
        self.previous_exp = 0

    def save(self, save_path):
        with open(save_path, "w") as f:
            json.dump(self.__dict__, f)

    def load(self, save_path):
        with open(save_path, "r") as f:
            data = json.load(f)
            self.__dict__.update(data)

    def do_a_loop(self) -> float:
        next_exp = game_information.get_total_exp()
        if next_exp <= self.previous_exp:
            raise Exception("The loop did not gain exp!")
        else:
            self.previous_exp = next_exp
        pressed_f1 = False
        possible_banking_motions = [
            (row, column) for row in range(1, 7) for column in range(4)
        ]
        possible_banking_motions.append((0, 2))
        possible_banking_motions.append((0, 3))
        if not self.first_loop:
            # Bank
            cursor.click_color_polygon(colors.PINK)
            randomizations.sleep_a_tick()
            # Remove glass from inventory
            cursor.click_polygon(
                polygons.get_inventory_polygon(
                    *random.choice(possible_banking_motions),
                ),
                ignore_post_randomness=True,
                ignore_predictive_movement=True,
            )
            # Close bank
            cursor.click_polygon(
                polygons.bank_close,
                ignore_post_randomness=True,
                ignore_predictive_movement=False,
            )
            randomizations.sleep_a_tick()
            # Change world
            keyboard.multiple_key_press(["ctrl", "shift", "2"])
            randomizations.sleep_at_least(7.2)
        self.first_loop = False
        for shop_slot in (2, 6):
            for i in range(3):
                # Returns time to wait
                print("Moving to buy ore")
                # cursor.click_polygon(ordan_minimap_location)
                # Move to ore
                cursor.click_color_polygon(
                    colors.BLUE,
                    ignore_predictive_movement=False,
                    ignore_post_randomness=True,
                )
                randomizations.sleep_at_least(3.8)
                if random.randint(0, 1):
                    if not pressed_f1:
                        keyboard.press("f1")
                        pressed_f1 = True
                # randomizations.sleep_at_least(0.6)
                # Buying iron
                cursor.click_polygon(
                    polygons.shop_polygons[shop_slot],
                    ignore_post_randomness=True,
                    ignore_predictive_movement=True,
                )
                # Closing shop
                cursor.click_polygon(
                    polygons.shop_close_polygon,
                    ignore_predictive_movement=True,
                    ignore_post_randomness=True,
                )
                # randomizations.sleep_at_least(0.3)
                if random.randint(0, 1):
                    if not pressed_f1:
                        keyboard.press("f1")
                        pressed_f1 = True
                # Banking
                cursor.click_color_polygon(
                    colors.PINK,
                    ignore_post_randomness=True,
                    ignore_predictive_movement=False,
                )
                randomizations.sleep_at_least(1)
                if game_information.get_inventory_slot(27) is None:
                    will_break = True
                else:
                    will_break = False
                randomizations.sleep_at_least(3.3)
                # Insert iron into bank
                if i != 2 and not will_break:
                    cursor.click_polygon(
                        polygons.get_inventory_polygon(
                            *random.choice(possible_banking_motions)
                        ),
                        ignore_post_randomness=True,
                        ignore_predictive_movement=True,
                    )
                else:
                    cursor.click_polygon(
                        polygons.get_inventory_polygon(0, 2),
                        ignore_post_randomness=True,
                        ignore_predictive_movement=True,
                    )
                if not (shop_slot == 6 and (i == 2 or will_break)):
                    cursor.click_polygon(polygons.bank_close)
                randomizations.sleep_at_least(0.1)
                if will_break:
                    break
        cursor.click_polygon(
            polygons.get_bank_polygon(
                row=self.bank_first_item_row,
                column=self.bank_first_item_column,
            ),
            ignore_post_randomness=True,
            ignore_predictive_movement=True,
        )
        cursor.click_polygon(
            polygons.bank_close,
            ignore_predictive_movement=True,
            ignore_post_randomness=True,
        )
        if random.randint(0, 1):
            if not pressed_f1:
                keyboard.press("f1")
                pressed_f1 = True
        cursor.click_polygon(
            polygons.inventory_polygons[1],
            ignore_post_randomness=True,
            ignore_predictive_movement=True,
        )
        cursor.click_polygon(
            polygons.inventory_polygons[2],
            ignore_post_randomness=False,
            ignore_predictive_movement=True,
        )
        randomizations.sleep_at_least(0.6)
        keyboard.press("6")
        return 46.9


def main() -> None:
    configs = IronOreMaker()
    try:
        while True:
            time.sleep(configs.do_a_loop())
            next_exp = game_information.get_total_exp()
    except Exception as err:
        print(err)
        print("Error encountered, logging of")
        logout.logout()


if __name__ == "__main__":
    main()
