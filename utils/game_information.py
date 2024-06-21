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
    url = "http://localhost:8080/inv"
    data = get_json_response(url)
    return data

def get_inventory_slot(num):
    inventory = get_inventory()
    if len(inventory) <= num:
        return None
    if inventory[num]['quantity'] == 0:
        return None
    return inventory[num]


def get_stats():
    url = "http://localhost:8080/stats"
    data = get_json_response(url)
    return data

def get_total_exp():
    stats = get_stats()
    total_exp = 0
    for stat in stats:
        total_exp += stat['xp']
    return total_exp


if __name__ == "__main__":
    print(get_total_exp)

# stats = [
    # {"stat": "Attack", "level": 99, "boostedLevel": 99, "xp": 13212919},
    # {"stat": "Defence", "level": 99, "boostedLevel": 99, "xp": 13037328},
    # {"stat": "Strength", "level": 99, "boostedLevel": 99, "xp": 13815096},
    # {"stat": "Hitpoints", "level": 99, "boostedLevel": 99, "xp": 17357044},
    # {"stat": "Ranged", "level": 97, "boostedLevel": 97, "xp": 11213905},
    # {"stat": "Prayer", "level": 78, "boostedLevel": 78, "xp": 1780034},
    # {"stat": "Magic", "level": 99, "boostedLevel": 99, "xp": 13581693},
    # {"stat": "Cooking", "level": 93, "boostedLevel": 93, "xp": 7750208},
    # {"stat": "Woodcutting", "level": 92, "boostedLevel": 92, "xp": 6695788},
    # {"stat": "Fletching", "level": 86, "boostedLevel": 86, "xp": 3959595},
    # {"stat": "Fishing", "level": 99, "boostedLevel": 99, "xp": 14704390},
    # {"stat": "Firemaking", "level": 99, "boostedLevel": 99, "xp": 13102952},
    # {"stat": "Crafting", "level": 95, "boostedLevel": 95, "xp": 8779351},
    # {"stat": "Smithing", "level": 89, "boostedLevel": 89, "xp": 5064098},
    # {"stat": "Mining", "level": 99, "boostedLevel": 99, "xp": 14239012},
    # {"stat": "Herblore", "level": 90, "boostedLevel": 90, "xp": 5398919},
    # {"stat": "Agility", "level": 99, "boostedLevel": 99, "xp": 13399676},
    # {"stat": "Thieving", "level": 99, "boostedLevel": 99, "xp": 16620550},
    # {"stat": "Slayer", "level": 78, "boostedLevel": 78, "xp": 1776779},
    # {"stat": "Farming", "level": 99, "boostedLevel": 99, "xp": 18334869},
    # {"stat": "Runecraft", "level": 99, "boostedLevel": 99, "xp": 13077050},
    # {"stat": "Hunter", "level": 93, "boostedLevel": 93, "xp": 7315126},
    # {"stat": "Construction", "level": 77, "boostedLevel": 77, "xp": 1509717},
# ]
