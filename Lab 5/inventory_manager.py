import json
import os


FILENAME = "inventory.json"


def load_inventory():
    if not os.path.exists(FILENAME):
        print("inventory.json not found. Starting with an empty inventory.")
        return []

    print("inventory.json found.")
    with open(FILENAME, "r", encoding="utf-8") as file:
        inventory = json.load(file)

    if not isinstance(inventory, list):
        raise ValueError("inventory.json must contain a list of products.")

    print("Inventory loaded successfully.")
    return inventory


def display_all(inventory):
    print("\nCurrent Inventory")
    if not inventory:
        print("No products in inventory.")
    else:
        for product in inventory:
            print(
                f"ID: {product['id']} | Name: {product['name']} | "
                f"Price: ${product['price']:.2f} | Stock: {product['stock']}"
            )


if __name__ == "__main__":
    try:
        inventory = load_inventory()
    except (OSError, ValueError) as error:
        print(f"Could not load inventory: {error}")
    else:
        display_all(inventory)
