from utils import cursor
from utils.constants import polygons

def logout() -> None:
    cursor.click_polygon(polygons.logout_interface)
    cursor.click_polygon(polygons.logout_interface_close_if_world_switch_is_on)
    cursor.click_polygon(polygons.logout_button)
