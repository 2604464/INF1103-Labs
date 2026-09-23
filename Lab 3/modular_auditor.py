# Initialize inventory and failed entries
inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    # Exit condition
    if stock.lower() == "quit":
        print("Total Units Processed:", inventory)
        print("Number of Failed/Rejected Entries:", failed_entries)
        break

    # Check if input is a valid integer
    if not stock.isdigit():
        print("Error: Please enter a valid integer.")
        failed_entries += 1
        continue

    stock = int(stock)

    # Reject negative numbers
    if stock < 0:
        print("Error: Negative stock quantities are not allowed.")
        failed_entries += 1
        continue

    # Add valid stock to inventory
    inventory += stock

    # Overstock alert
    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break

    print("Current inventory:", inventory)