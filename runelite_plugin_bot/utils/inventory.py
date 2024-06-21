import requests

# From runelite plugin:
# GET http://localhost:8080/inv obtains the inventory.
# Format:
# [
# {"id": -1, "quantity": 0},
# ...
# ]
# SXpmO83h


def get_json_response(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Convert the response to JSON format
        json_data = response.json()

        return json_data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def get_inventory():
    url = "http://localhost:8081/inv"
    data = get_json_response(url)


class Box:
    def __init__(self, x_min: int, x_max: int, y_min: int, y_max: int):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def displace(self, delta_x: int, delta_y: int):
        return Box(
            self.x_min + delta_x,
            self.x_max + delta_x,
            self.y_min + delta_y,
            self.y_max + delta_y,
        )

    def click(self, offset=(0, 0)):
        x_mean = (self.x_min + self.x_max) / 2
        y_mean = (self.y_min + self.y_max) / 2
        x_sigma = (self.x_max - self.x_min) / 8  # approx 99.7% within +/- 3 sigma
        y_sigma = (self.y_max - self.y_min) / 8
        x = random.gauss(x_mean, x_sigma)
        y = random.gauss(y_mean, y_sigma)
        x = max(min(x, self.x_max), self.x_min)
        y = max(min(y, self.y_max), self.y_min)
        duration = random.uniform(0.2, 0.5)
        cursor.move_to([x + offset[0], y + offset[1]], duration=duration, steady=True)
        click_duration = random.uniform(0.1, 0.3)
        pyautogui.mouseDown()
        time.sleep(click_duration)
        pyautogui.mouseUp()

    def __str__(self):
        return f"[{self.x_min}, {self.x_max}, {self.y_min}, {self.y_max}]"


class InventorySlot:
    DELTA_X_BETWEEN_SLOTS = 606 - 564
    DELTA_Y_BETWEEN_SLOTS = 250 - 214

    def __init__(self, box=Box(564, 599, 214, 245)):
        self.box = box

    def left(self):
        return InventorySlot(self.box.displace(-InventorySlot.DELTA_X_BETWEEN_SLOTS, 0))

    def right(self):
        return InventorySlot(self.box.displace(InventorySlot.DELTA_X_BETWEEN_SLOTS, 0))

    def up(self):
        return InventorySlot(
            self.box.displace(
                0,
                -InventorySlot.DELTA_Y_BETWEEN_SLOTS,
            )
        )

    def down(self):
        return InventorySlot(
            self.box.displace(
                0,
                InventorySlot.DELTA_Y_BETWEEN_SLOTS,
            )
        )

    def click(self, offset=(0, 0)):
        self.box.click(offset=offset)

    def __str__(self):
        return str(self.box)


class Inventory:
    def __init__(self):
        self.grid = [[InventorySlot()]]
        for i in range(3):
            self.grid[0].append(self.grid[0][i].right())
        for i in range(6):
            self.grid.append([self.grid[i][j].down() for j in range(4)])

    def __str__(self):
        row_str = ""
        for row in self.grid:
            for slot in row:
                row_str += str(slot)
            row_str += "\n"
        return row_str

    def click(self, x: int, y: int, offset=(0, 0)):
        self.grid[y][x].click(offset=offset)
