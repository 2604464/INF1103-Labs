# Phase 1: Each product is a dictionary. The inventory is a list.
inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.0,
        "stock": 15,
        "transactions": [15]
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.5,
        "stock": 40,
        "transactions": [40]
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.0,
        "stock": 25,
        "transactions": [25]
    }
]


def display_all(inventory):
    print("Current Inventory")
    for product in inventory:
        print(
            f"ID: {product['id']} | Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | Stock: {product['stock']}"
        )


if __name__ == "__main__":
    display_all(inventory)
