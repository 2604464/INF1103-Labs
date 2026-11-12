from supplier import Supplier
from product import PhysicalProduct, DigitalProduct
from inventory import Inventory

# Create Supplier
supplier = Supplier(
    "S001",
    "Tech Supplies Pte Ltd",
    "contact@techsupplies.com"
)

# Create Products before creating Inventories
guitar = PhysicalProduct(
    "P001",
    "Electric Guitar",
    599.90,
    10,
    4.5,
    supplier
)

software = DigitalProduct(
    "P002",
    "Antivirus Software",
    49.90,
    100,
    250,
    supplier
)

# Create Inventory A
inventory_a = Inventory()

# Add Products to Inventory A
inventory_a.add_product(guitar)
inventory_a.add_product(software)

print("=== Inventory A ===")
inventory_a.display_all_products()

# Find Product
print("\n=== Find Product ===")
found_product = inventory_a.find_product("P001")

print("Product found:", found_product is guitar)

# Remove Product from Inventory A
print("\n=== Remove Product ===")
removed = inventory_a.remove_product("P001")

print("Product removed:", removed)
print("Product in Inventory A:", inventory_a.find_product("P001"))

# Check if Product still exists
print("\n=== Product After Removal ===")
guitar.display_information()

# Create Inventory B
inventory_b = Inventory()

# Transfer same Product object to Inventory B
inventory_b.add_product(guitar)

print("\n=== Inventory B ===")
inventory_b.display_all_products()

# Confirm it is the same Product object
print(
    "Same Product Object:",
    inventory_b.find_product("P001") is guitar
)

# Confirm Inventory A no longer contains the Product
print(
    "Still in Inventory A:",
    inventory_a.find_product("P001") is not None
)
