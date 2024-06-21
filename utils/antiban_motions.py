from . import cursor
from . import randomizations
from .randomizations import generate_gaussian_position
import random
import time

is_in_exp_tab = False
is_in_item_tab = False


exp_coordinates = {
    "attack": (549, 601, 209, 233),
    "strength": (546, 602, 241, 263),
    "Defence": (546, 602, 274, 297),
    "Ranged": (547, 602, 305, 329),
    "Prayer": (548, 600, 338, 359),
    "Magic": (548, 602, 369, 390),
    "Runecrafting": (548, 600, 404, 424),
    "Construction": (548, 602, 431, 453),
    "Hitpoints": (612, 666, 208, 232),
    "Agility": (609, 665, 239, 264),
    "Herblore": (611, 663, 271, 298),
    "Thieving": (611, 665, 305, 329),
    "Crafting": (610, 668, 336, 360),
    "Fletching": (612, 667, 368, 390),
    "Slayer": (612, 667, 401, 422),
    "Hunter": (612, 668, 431, 455),
    "Mining": (673, 729, 211, 232),
    "Smithing": (672, 726, 239, 265),
    "Fishing": (673, 729, 273, 296),
    "Cooking": (671, 730, 304, 329),
    "Firemaking": (672, 728, 335, 361),
    "Woodcutting": (674, 731, 368, 393),
    "Farming": (673, 731, 400, 423),
    "Total": (675, 728, 436, 456),
}

random_weights = {
    "attack": 1,
    "strength": 1,
    "Defence": 20,
    "Ranged": 5,
    "Prayer": 5,
    "Magic": 1,
    "Runecrafting": 1,
    "Construction": 5,
    "Hitpoints": 1,
    "Agility": 1,
    "Herblore": 5,
    "Thieving": 1,
    "Crafting": 5,
    "Fletching": 5,
    "Slayer": 6,
    "Hunter": 5,
    "Mining": 1,
    "Smithing": 5,
    "Fishing": 1,
    "Cooking": 5,
    "Firemaking": 1,
    "Woodcutting": 5,
    "Farming": 1,
    "Total": 10,
}


def change_to_exp_tab():
    exp_box_coordiantes = (558, 587, 170, 198)
    cursor.click_at(*generate_gaussian_position(*exp_box_coordiantes))


def change_to_item_tab():
    item_tab_coordinates = (625, 650, 169, 195)
    cursor.click_at(*generate_gaussian_position(*item_tab_coordinates))


def check_exp(name):
    magic_exp_coordinates = (549, 600, 367, 394)
    cursor.move_to(*generate_gaussian_position(*exp_coordinates[name]))


def check_random_exp(average_time=4):
    change_to_exp_tab()
    amount_of_exps_to_check = random.randint(1, 4)
    change_to_exp_tab()
    keys = list(random_weights.keys())
    values = list(random_weights.values())
    for _ in range(amount_of_exps_to_check):
        check_exp(random.choices(keys, weights=values, k=1)[0])
        time_to_sleep = randomizations.generate_gaussian(average_time, average_time / 2)
        time.sleep(max(0, time_to_sleep))
    change_to_item_tab()
