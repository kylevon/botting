from utils import cursor
from utils.constants import polygons

def logout() -> None:
    cursor.click_polygon(polygons.logout_interface)
    cursor.click_polygon(polygons.logout_button)
