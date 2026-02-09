import json

def check_availability(date, time):
    with open("data/availability.json", "r") as f:
        data = json.load(f)

    if date in data and time in data[date]:
        return data[date][time] > 0
    return False
