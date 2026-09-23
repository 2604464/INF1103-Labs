def get_valid_input():
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock.lower() == "quit":
        return "quit"

    # Check for negative whole numbers before the general digit check
    if stock.startswith("-") and stock[1:].isdigit():
        raise ValueError("Negative stock quantities are not allowed.")

    if not stock.isdigit():
        raise ValueError("Please enter a valid integer.")

    return int(stock)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

def main():
    inventory = 0
    failed_entries = 0
    deliveries_processed = 0

    while True:
        try:
            stock = get_valid_input()
        except ValueError as error:
            print("Error:", error)
            failed_entries += 1
            continue

        # Print the final report when the user quits
        if stock == "quit":
            print("Total Deliveries Processed:", deliveries_processed)
            generate_report(inventory, failed_entries)
            break

        # Process a valid delivery
        inventory = process_delivery(inventory, stock)
        tax = calculate_tax(stock)
        deliveries_processed += 1

        print(f"Tax for this delivery: {tax:.2f}")

        # Preserve the Lab 2 overstock rule
        if inventory > 500:
            print("ALERT: Overstock! Inventory exceeds 500 units.")
            break

        print("Current inventory:", inventory)


if __name__ == "__main__":
    main()