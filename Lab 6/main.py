import json
from pathlib import Path

from inventory import Inventory
from product import Product

DATA_FILE = Path(__file__).with_name("inventory.json")


def load_inventory(inventory: Inventory) -> None:
    """Load saved product data and convert each record into a Product object."""
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No inventory.json found. Starting with an empty inventory.")
        return
    except json.JSONDecodeError:
        print("inventory.json is not valid JSON. Starting with an empty inventory.")
        return
    except OSError as error:
        print(f"Could not read inventory.json: {error}")
        return

    if not isinstance(data, list):
        print("inventory.json must contain a list of products. Starting empty.")
        return

    loaded_count = 0
    for item in data:
        try:
            if not isinstance(item, dict):
                raise ValueError("Product record must be a JSON object.")

            product = Product(
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"],
            )
            inventory.add_product(product)
            loaded_count += 1
        except (KeyError, TypeError, ValueError) as error:
            print(f"Skipping an invalid product record: {error}")

    print(f"Loaded {loaded_count} product(s).")


def save_inventory(inventory: Inventory) -> None:
    """Save Product objects as JSON data."""
    data = []
    for product in inventory.get_all_products():
        data.append(
            {
                "product_id": product.get_product_id(),
                "name": product.get_name(),
                "price": product.get_price(),
                "stock": product.get_stock(),
            }
        )

    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("Inventory saved successfully.")
    except OSError as error:
        print(f"Could not save inventory.json: {error}")


def display_menu() -> None:
    print("\n===== Inventory Management System =====")
    print("1. Display all products")
    print("2. Add a product")
    print("3. Update stock")
    print("4. Search for a product")
    print("5. Save inventory")
    print("6. Exit")


def add_product(inventory: Inventory) -> None:
    try:
        product_id = input("Enter product ID: ").strip()
        name = input("Enter product name: ").strip()
        price = float(input("Enter product price: "))
        stock = int(input("Enter stock quantity: "))

        product = Product(product_id, name, price, stock)
        inventory.add_product(product)
        print("Product added successfully.")
    except ValueError as error:
        print(f"Unable to add product: {error}")
    except TypeError as error:
        print(f"Unable to add product: {error}")


def update_stock(inventory: Inventory) -> None:
    product_id = input("Enter the product ID to update: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    try:
        new_stock = int(input("Enter the new stock quantity: "))
        product.update_stock(new_stock)
        print("Stock updated successfully.")
    except ValueError as error:
        print(f"Unable to update stock: {error}")


def search_product(inventory: Inventory) -> None:
    product_id = input("Enter the product ID to search: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
    else:
        print("\n--- Product Found ---")
        product.display_information()


def main() -> None:
    inventory = Inventory()
    load_inventory(inventory)

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            save_inventory(inventory)
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
