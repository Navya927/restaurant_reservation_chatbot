import json

def load_menu():
    with open("data/menu.json", "r") as f:
        return json.load(f)
