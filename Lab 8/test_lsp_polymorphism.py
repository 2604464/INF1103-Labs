from supplier import Supplier
from product import Product, PhysicalProduct, DigitalProduct
from inventory import Inventory


# Accepts any Product
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


# Create Supplier
supplier = Supplier(
    "S001",
    "Tech Supplies Pte Ltd",
    "contact@techsupplies.com"
)


# Create PhysicalProduct
guitar = PhysicalProduct(
    "P001",
    "Electric Guitar",
    599.90,
    10,
    4.5,
    supplier
)


# Create DigitalProduct
software = DigitalProduct(
    "P002",
    "Antivirus Software",
    49.90,
    100,
    250,
    supplier
)


# Create Inventory
inventory = Inventory()

# Add both product types to the same Inventory
inventory.add_product(guitar)
inventory.add_product(software)


# Demo polymorphism
print("=== Polymorphism Test ===")

for product in inventory.get_all_products():
    show_product_details(product)
    print("--------------------")


# Demo LSP
print("\n=== LSP Test ===")

for product in inventory.get_all_products():
    product.update_stock(5)

    print(
        f"{product.get_name()} stock updated to: "
        f"{product.get_stock()}"
    )


# Both products should work through Product references
print("\n=== Product Type Test ===")

products: list[Product] = [
    guitar,
    software
]

for product in products:
    print(
        f"{product.get_name()}: "
        f"{product.get_fulfilment_info()}"
    )
