from utils import antiban_motions
from utils import randomizations
from utils import keyboard
from utils import cursor
from utils import game_information
from utils.obtain_polygon import obtain_polygon
from utils.constants import colors
from utils.constants import polygons
from utils.logout import logout
import time
import random
import json


class CannonBallsMaker:
    def __init__(self):
        # load_file = get_integer_input("Use previous configs? (1 = yes, 0 = no)")
        self.steel_column = 2
        self.steel_row = 6

    def save(self, save_path):
        with open(save_path, "w") as f:
            json.dump(self.__dict__, f)

    def load(self, save_path):
        with open(save_path, "r") as f:
            data = json.load(f)
            self.__dict__.update(data)

    def do_a_loop(self) -> float:
        cursor.click_color_polygon(colors.PINK)
        # randomizations.sleep_at_least(4.9)
        randomizations.sleep_at_least(5.3)
        cursor.click_polygon(
            polygons.get_bank_polygon(row=self.steel_row,
                                      column=self.steel_column)
        )
        cursor.click_polygon(polygons.bank_close, ignore_post_randomness=False)
        randomizations.sleep_at_least(0.2)
        cursor.click_color_polygon(colors.BLUE)
        current_exp = game_information.get_total_exp()
        cursor.move_offset(random.gauss(0, 3), random.gauss(0, 3))
        randomizations.sleep_at_least(5.32)
        keyboard.press("space")
        cursor.move_offset(random.gauss(0, 3), random.gauss(0, 3))
        randomizations.sleep_at_least(6)
        cursor.move_offset(random.gauss(0, 3), random.gauss(0, 3))
        if game_information.get_total_exp() == current_exp:
            cursor.click_color_polygon(colors.BLUE)
            randomizations.sleep_at_least(0.6)
            keyboard.press("space")
            randomizations.sleep_at_least(6)
            if game_information.get_total_exp() == current_exp:
                raise Exception("Something went wrong, not increasing exp")
        return randomizations.random_number_at_least(78 - 6)


def main() -> None:
    configs = CannonBallsMaker()
    try:
        while True:
            to_sleep = configs.do_a_loop()
            cursor.move_to(random.randint(600, 1200), random.randint(600, 1200))
            time.sleep(to_sleep)
    except Exception as err:
        print(err)
        print("Logging out!")
        logout()


if __name__ == "__main__":
    main()
