import json


def load_inventory():
    try:
        with open("inventory.txt", "r", encoding="utf-8") as file:
            data = json.load(file)

        return data["total"], data["history"]

    except FileNotFoundError:
        return 0, []


def get_valid_input():
    value = input("Enter quantity (or 'quit' to exit): ").strip()

    if value.lower() == "quit":
        return "quit"

    if not value.isdigit():
        raise ValueError("Enter a whole number of 0 or more.")

    return int(value)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

def save_inventory(total, history):
    data = {
        "total": total,
        "history": history
    }

    with open("inventory.txt", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved to inventory.txt")

def main():
    inventory, history = load_inventory()
    failed_attempts = 0
    deliveries = 0

    print(f"Loaded inventory: {inventory}")
    print(f"Loaded history: {history}")

    while True:
        if inventory > 500:
            print("ALERT: Inventory exceeds 500. Stopping.")
            break

        try:
            quantity = get_valid_input()
        except ValueError as error:
            print(f"Error: {error}")
            failed_attempts += 1
            continue

        if quantity == "quit":
            break

        inventory = process_delivery(inventory, quantity)
        history.append(quantity)
        deliveries += 1

        print(f"Tax for this delivery: {calculate_tax(quantity):.2f}")
        print(f"Current inventory: {inventory}")

    print(f"Total Deliveries Processed (this run): {deliveries}")
    generate_report(inventory, failed_attempts)
    print(f"Transaction history: {history}")
    save_inventory(inventory, history)


if __name__ == "__main__":
    main()