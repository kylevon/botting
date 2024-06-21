FIRST_SLOT_BANK = [(69, 84), (104, 84), (104, 115), (69, 115)]
FIRST_SLOT_INVENTORY = [[559, 245], [559, 214], [594, 214], [594, 245]]

FIRST_SHOP_POLYGON = [(73, 65), (108, 65), (108, 96), (73, 96)]

DELTA_X_BANK = 48
DELTA_Y_BANK = 36

DELTA_X_INVENTORY = 42
DELTA_Y_INVENTORY = 36

def create_grid(original_polygon, delta_x, delta_y, num_rows, num_columns):
    out = []
    for row in range(num_rows):
        for column in range(num_columns):
            dy = row * delta_y
            dx = column * delta_x
            polygon = []
            for x, y in original_polygon:
                polygon.append((x + dx, y + dy))
            out.append(polygon)
    return out


bank_polygons = create_grid(FIRST_SLOT_BANK, DELTA_X_BANK, DELTA_Y_BANK, 10, 8)
inventory_polygons = create_grid(
    FIRST_SLOT_INVENTORY, DELTA_X_INVENTORY, DELTA_Y_INVENTORY, 7, 4
)

shop_polygons = create_grid(
    FIRST_SHOP_POLYGON, DELTA_X_BANK, DELTA_Y_BANK, 1, 7
)

shop_close_polygon = [
    [473, 32], [473, 49], [489, 49], [489, 32]
]

def get_bank_polygon(row=0, column=0):
    return bank_polygons[row * 8 + column]

def get_inventory_polygon(row=0, column=0):
    return inventory_polygons[row * 4 + column]

bank_close = [
    (475, 30),
    (474, 16),
    (490, 15),
    (489, 31),
]

bank_deposit = [
    (427, 467),
    (423, 466),
    (423, 443),
    (426, 439),
    (448, 439),
    (454, 441),
    (454, 465),
]

logout_interface = [
    (626, 497),
    (626, 469),
    (648, 467),
    (650, 498),
]

logout_button = [
    (573, 445),
    (571, 441),
    (571, 421),
    (574, 419),
    (703, 418),
    (706, 423),
    (705, 441),
    (703, 445),
]
