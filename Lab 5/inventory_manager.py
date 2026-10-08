import json
import math
import os


FILENAME = "inventory.json"


def load_inventory():
    """Read saved products, or start with an empty list."""
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


def save_inventory(inventory):
    """Write the current products and their stock history to JSON."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(inventory, file, indent=4, allow_nan=False)
    except (OSError, ValueError) as error:
        print(f"Could not save inventory: {error}")
        return False

    print("Inventory saved successfully to inventory.json.")
    return True


def find_product(inventory, product_id):
    """Return the matching dictionary, or None if it is missing."""
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None


def read_number(prompt, whole_number=False):
    """Keep asking until the user enters a valid non-negative number."""
    while True:
        text = input(prompt).strip()

        try:
            if whole_number:
                number = int(text)
            else:
                number = float(text)
        except ValueError:
            if whole_number:
                print("Please enter a whole number, such as 10.")
            else:
                print("Please enter a number, such as 25.50.")
            continue

        if number < 0:
            print("The number cannot be negative.")
            continue

        if not whole_number and not math.isfinite(number):
            print("Please enter a finite number.")
            continue

        return number


def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 65)

    if not inventory:
        print("No products in inventory.")
    else:
        for product in inventory:
            print(
                f"ID: {product['id']} | Name: {product['name']} | "
                f"Price: ${product['price']:.2f} | Stock: {product['stock']}"
            )

    print("-" * 65)


def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip().upper()

    if not product_id:
        print("Product ID cannot be empty.")
        return

    if find_product(inventory, product_id) is not None:
        print("This Product ID already exists.")
        return

    name = input("Product Name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return

    price = read_number("Price: ")
    stock = read_number("Stock Quantity: ", whole_number=True)

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock,
        "transactions": [stock]
    }
    inventory.append(product)
    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip().upper()
    product = find_product(inventory, product_id)

    if product is None:
        print("Product not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")

    old_stock = product["stock"]
    new_stock = read_number("New Stock Quantity: ", whole_number=True)

    # Each transaction records a change in units, not the new total.
    # For example, changing stock from 40 to 50 records +10.
    if "transactions" not in product:
        product["transactions"] = [old_stock]
    product["transactions"].append(new_stock - old_stock)
    product["stock"] = new_stock

    print("Stock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip().upper()
    product = find_product(inventory, product_id)

    if product is None:
        print("Product not found.")
        return

    print("\nProduct Found")
    print("-" * 40)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print(f"Stock changes (units): {product.get('transactions', [])}")
    print("-" * 40)


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    try:
        inventory = load_inventory()
    except (OSError, ValueError) as error:
        print(f"Could not load inventory: {error}")
        print("Check inventory.json, then run the program again.")
        return

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        option = input("Enter option: ").strip()

        if option == "1":
            display_all(inventory)
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)
        elif option == "6":
            print("\nSaving inventory before exit...")
            if save_inventory(inventory):
                print("Thank you for using Inventory Management System.")
                print("Program terminated.")
                break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
