from utils import cursor
from utils.constants.colors import GREEN, YELLOW, RED, BLUE, PINK
from utils.constants.polygons import bank_polygons, inventory_polygons
from utils import detect_color_polygon
from utils import keyboard
import time
from utils import game_information
from utils.logout import logout

if __name__ == "__main__":
    # for polygon in bank_polygons:
    # cursor.move_to_polygon(polygon)
    # for polygon in inventory_polygons:
    # cursor.move_to_polygon(polygon)
    # for i in range(5):
    # print("PINK")
    # cursor.move_to_color_polygon(PINK)
    # time.sleep(1)
    # print("BLUE")
    # cursor.move_to_color_polygon(BLUE)
    # time.sleep(2)
    # time.sleep(1)
    # cursor.scroll_in()
    # cursor.scroll_out()
    # detect_color_polygon.visualize_color_points(
        # detect_color_polygon.detect_color_polygon(*BLUE), "out.png"
    # )
    # time.sleep(1)
    # keyboard.multiple_key_press(["ctrl", "shift", "right"])
    logout()
    

