from pynput import mouse, keyboard
from utils.screen_finder import obtain_offset

# Function to be called when the "r" key is pressed
def on_press(key):
    try:
        if key.char == 'r':
            x, y = mouse_controller.position
            dx, dy = obtain_offset()
            # dx, dy = 0,0
            print(f"Mouse is at ({x - dx}, {y - dy})")
    except AttributeError:
        pass

# Setting up mouse controller to get the current position
mouse_controller = mouse.Controller()

# Setting up keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
