from pynput import mouse, keyboard
from .screen_finder import obtain_offset
from . import randomizations  # Assuming this file is named randomization.py
import pyautogui

# Initialize variables
polygon_vertices = []
recording = True
mouse_controller = mouse.Controller()

# Function to be called when a key is pressed
def on_press(key):
    global recording
    try:
        if key.char == 'r':
            x, y = mouse_controller.position
            dx, dy = obtain_offset()
            polygon_vertices.append((x - dx, y - dy))
            print(f"Recorded point: ({x - dx}, {y - dy})")
        elif key.char == 's':
            recording = False
            print("Stopped recording.")
    except AttributeError:
        pass

def obtain_polygon():
    global recording, polygon_vertices
    recording = True
    polygon_vertices = []

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Wait for the recording to stop
    while recording:
        pass

    # Stop the listener
    listener.stop()

    return polygon_vertices

# if __name__ == "__main__":
    # vertices = obtain_polygon()
    # print(f"Recorded vertices: {vertices}")
    # print(f"Random point: {randomizations.random_point_in_polygon(vertices)}")
