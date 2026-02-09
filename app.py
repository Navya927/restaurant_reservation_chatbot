import json
from datetime import datetime


def load_menu():
    return {
        "M1": {"name": "Pizza", "price": 250},
        "M2": {"name": "Burger", "price": 180},
        "M3": {"name": "Pasta", "price": 220}
    }


def load_availability():
    return {
        "18:00": 5,
        "19:00": 3,
        "20:00": 2
    }


def show_menu(menu):
    print("\n--- MENU ---")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - ₹{item['price']}")


def show_slots(slots):
    print("\n--- AVAILABLE SLOTS ---")
    for time, tables in slots.items():
        print(f"{time} → {tables} tables available")


def main():
    print("🍽️ Welcome to Restaurant Reservation Chatbot 🍽️")

    name = input("Enter your name: ")

    date = input("Enter reservation date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format")
        return

    menu = load_menu()
    availability = load_availability()

    show_menu(menu)
    show_slots(availability)

    time = input("\nChoose a time slot (HH:MM): ")

    if time not in availability or availability[time] == 0:
        print("❌ Slot not available")
        return

    availability[time] -= 1

    print("\n✅ Reservation Confirmed!")
    print(f"Name: {name}")
    print(f"Date: {date}")
    print(f"Time: {time}")
    print("Enjoy your meal! 🎉")


if __name__ == "__main__":
    main()
