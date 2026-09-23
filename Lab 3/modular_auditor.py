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