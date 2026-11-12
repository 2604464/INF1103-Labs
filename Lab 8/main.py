import json
from pathlib import Path

from inventory import Inventory
from product import PhysicalProduct, DigitalProduct, CanBeShipped
from supplier import Supplier
from order import Order

DATA_FILE = Path(__file__).with_name("inventory.json")



def load_inventory(inventory: Inventory) -> None:
    """Load saved product data and create the appropriate objects."""

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

            product_type = item["type"]

            # Load Supplier information
            supplier_data = item.get("supplier")

            # Support older Lab 7 inventory records
            if supplier_data is None:
                supplier_data = {}

            if not isinstance(supplier_data, dict):
                raise ValueError("Invalid supplier data.")

            supplier = Supplier(
                str(supplier_data.get("supplier_id", "S000")),
                str(supplier_data.get("name", "Legacy Supplier")),
                str(supplier_data.get("contact_email", "Not provided"))
            )

            if product_type == "physical":
                product = PhysicalProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["weight"],
                    supplier
                )

            elif product_type == "digital":
                product = DigitalProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"],
                    supplier
                )

            else:
                raise ValueError("Unknown product type.")

            inventory.add_product(product)
            loaded_count += 1

        except (KeyError, TypeError, ValueError) as error:
            print(f"Skipping an invalid product record: {error}")

    print(f"Loaded {loaded_count} product(s).")



def save_inventory(inventory: Inventory) -> None:
    """Save products and their supplier information as JSON."""

    data = []

    for product in inventory.get_all_products():

        product_data = {
            "product_id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock(),

            "supplier": {
                "supplier_id": product.supplier.supplier_id,
                "name": product.supplier.name,
                "contact_email": product.supplier.contact_email
            }
        }

        if isinstance(product, PhysicalProduct):
            product_data["type"] = "physical"
            product_data["weight"] = product.get_weight()

        elif isinstance(product, DigitalProduct):
            product_data["type"] = "digital"
            product_data["download_size"] = product.get_download_size()

        else:
            raise TypeError("Unsupported product type.")

        data.append(product_data)

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
    print("6. Create customer order")
    print("7. Exit")



def add_product(inventory: Inventory) -> None:
    try:
        print("\nChoose product type:")
        print("1. Physical Product")
        print("2. Digital Product")

        product_type = input("Enter your choice (1-2): ").strip()

        if product_type not in ("1", "2"):
            print("Invalid product type.")
            return

        product_id = input("Enter product ID: ").strip()
        name = input("Enter product name: ").strip()
        price = float(input("Enter product price: "))
        stock = int(input("Enter stock quantity: "))

        # Get Supplier information
        print("\nEnter Supplier Information")

        supplier_id = input("Enter supplier ID: ").strip()
        supplier_name = input("Enter supplier name: ").strip()
        supplier_email = input("Enter supplier email: ").strip()

        supplier = Supplier(
            supplier_id,
            supplier_name,
            supplier_email
        )

        if product_type == "1":
            weight = float(input("Enter product weight (kg): "))

            product = PhysicalProduct(
                product_id,
                name,
                price,
                stock,
                weight,
                supplier
            )

        else:
            download_size = float(
                input("Enter download size (MB): ")
            )

            product = DigitalProduct(
                product_id,
                name,
                price,
                stock,
                download_size,
                supplier
            )

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
        print(product.get_fulfilment_info())

        if isinstance(product, CanBeShipped):
            print(
                f"Shipping Cost: "
                f"${product.calculate_shipping_cost():.2f}"
            )

        print("\n--- Supplier Information ---")
        product.supplier.display_information()



def create_order(inventory: Inventory) -> None:
    """Create an order containing existing inventory products."""

    order_id = input("Enter order ID: ").strip()
    order = Order(order_id)

    print("\nEnter products for this order.")
    print("Type 'done' when you have finished.")

    while True:
        product_id = input(
            "\nEnter product ID (or done): "
        ).strip()

        if product_id.lower() == "done":
            break

        product = inventory.find_product(product_id)

        if product is None:
            print("Product not found.")
            continue

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            order.add_order_line(product, quantity)

            print("Product added to order.")

        except ValueError:
            print("Please enter a valid whole number.")

    if not order.order_lines:
        print("No products were added. Order cancelled.")
        return

    print("\n========== ORDER SUMMARY ==========")
    print("Order ID:", order.order_id)

    for line in order.order_lines:
        print(
            f"{line.product.get_name()} "
            f"x {line.quantity} = "
            f"${line.calculate_subtotal():.2f}"
        )

    print("-----------------------------------")
    print(f"Order Total: ${order.calculate_total():.2f}")



def main() -> None:
    inventory = Inventory()
    load_inventory(inventory)

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            inventory.display_all_products()

        elif choice == "2":
            add_product(inventory)

        elif choice == "3":
            update_stock(inventory)

        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            create_order(inventory)

        elif choice == "7":
            save_inventory(inventory)
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
