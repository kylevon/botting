import time
from pyvirtualdisplay import Display
from easyprocess import EasyProcess
from utils import cursor
with Display(visible=True, backend="xephyr") as disp:
    # Open a connection to the virtual display
    d = display.Display(disp.display)
    root = d.screen().root

    # Function to move the cursor within the virtual display
    def move_cursor(x, y):
        root.warp_pointer(x, y)
        d.sync()

    with EasyProcess(["bolt"]) as proc:
        move_cursor(10, 10)
        move_cursor(10, 20)
        time.sleep(1000000)
        # proc.wait()
    # with EasyProcess(["bolt"]) as proc:
        # cursor.move_to(10,10)
        # cursor.move_to(10,20)
        # time.sleep(1000000)
        # # proc.wait()
