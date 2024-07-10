from utils import antiban_motions
from utils import randomizations
from utils import keyboard
from utils.logout import logout
from utils import game_information
from utils import cursor
from utils import tui
from utils.obtain_polygon import obtain_polygon
from utils.constants import colors
from utils.constants import polygons
import time
import pyautogui
import random
import json


class BankStandingConfigs:
    def __init__(self):
        load_file = tui.get_integer_input("Use previous configs? (1 = yes, 0 = no)")
        self.current_exp = 0
        if load_file == 1:
            self.load("previous_bank_standing_configs.json")
        else:
            self.modality = tui.get_integer_input("Modality: 1/2 items")
            assert self.modality == 1 or self.modality == 2
            self.bank_first_item_column = tui.get_integer_input("column at bank")
            self.bank_first_item_row = tui.get_integer_input("row at bank")
            self.min_seconds = tui.get_integer_input(
                "Min seconds to do loop (10 for herb finish)"
            )
            self.optimal_seconds = tui.get_integer_input(
                "optimal seconds to do loop (12 for herb finish)"
            )
            self.save("previous_bank_standing_configs.json")

    def save(self, save_path):
        with open(save_path, "w") as f:
            json.dump(self.__dict__, f)

    def load(self, save_path):
        with open(save_path, "r") as f:
            data = json.load(f)
            self.__dict__.update(data)

    def do_a_loop(self) -> int:
        # Returns time to wait
        if self.current_exp != 0:
            next_exp = game_information.get_total_exp()
            if next_exp == self.current_exp:
                raise Exception("Did not increase exp!")
            else:
                self.current_exp = next_exp
        else:
            self.current_exp = game_information.get_total_exp()
        cursor.click_color_polygon(
            colors.PINK, ignore_post_randomness=True, ignore_predictive_movement=True
        )
        time.sleep(randomizations.tick_duration())
        cursor.move_to_polygon(polygons.bank_deposit)
        time.sleep(randomizations.tick_duration() / 2)
        cursor.click()
        cursor.click_polygon(
            polygons.get_bank_polygon(
                column=self.bank_first_item_column, row=self.bank_first_item_row
            ),
            ignore_post_randomness=True,
            ignore_predictive_movement=True,
        )
        cursor.click_polygon(
            polygons.get_bank_polygon(
                column=self.bank_first_item_column + 1, row=self.bank_first_item_row
            ),
            ignore_post_randomness=True,
            ignore_predictive_movement=True,
        )
        cursor.click_polygon(
            polygons.bank_close,
            ignore_post_randomness=True,
            ignore_predictive_movement=True,
        )
        possible_two_items = [
            [(3, 0), (4, 0)],
            [(3, 1), (4, 1)],
            [(3, 1), (3, 2)],
            [(2, 2), (3, 2)],
            [(2, 3), (3, 3)],
        ]
        first_item, second_item = random.choice(possible_two_items)
        cursor.move_to_polygon(polygons.get_inventory_polygon(*first_item))
        time.sleep(randomizations.tick_duration() / 2)
        cursor.click()
        cursor.click_polygon(
            polygons.get_inventory_polygon(*second_item),
            ignore_predictive_movement=False,
        )
        time.sleep(randomizations.tick_duration())
        keyboard.press("space")
        time.sleep(2)
        if game_information.get_total_exp() == self.current_exp:
            keyboard.press("space")
        return randomizations.random_number_at_least(self.min_seconds - 2)


def main() -> None:
    configs = BankStandingConfigs()
    try:
        while True:
            time.sleep(configs.do_a_loop())
    except Exception as err:
        print(err)
        print("Loggin out!!!")
        logout()


if __name__ == "__main__":
    main()
