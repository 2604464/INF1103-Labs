INF1103 LAB 6 - OOP INVENTORY SYSTEM

Files:
- product.py: Product class
- inventory.py: Inventory class
- main.py: menu, user input, JSON loading and saving
- inventory.json: sample saved products
- class_diagram.txt: UML class diagram content

Run locally:
1. Open this folder in VS Code.
2. Open the terminal in this folder.
3. Run: python main.py

The program loads inventory.json when it starts and saves it when you select
option 5 or option 6.

JSON format used:
[
    {
        "product_id": "P001",
        "name": "Laptop",
        "price": 1200.0,
        "stock": 15
    }
]

Notes:
- update_stock(quantity) sets stock to the new quantity.
- Product attributes use double underscores to indicate intended privacy.
- Only Product and Inventory are classes. The menu and file handling are
  functions in main.py, following the lab's Single Responsibility Principle.
