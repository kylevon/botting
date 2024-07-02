import time
from pyvirtualdisplay import Display
from easyprocess import EasyProcess
with Display(visible=True, backend="xephyr", extra_args=["-sw-cursor", "-fullscreen"]) as disp:
    with EasyProcess(["bolt"]) as proc:
        from utils import cursor
        input("Press enter to start bot")
        import iron_buyer
        iron_buyer.main()
        # proc.wait()
