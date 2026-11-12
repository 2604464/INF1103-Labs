
from supplier import Supplier
from product import PhysicalProduct, DigitalProduct

# Create Supplier independently
supplier = Supplier(
    "S001",
    "Tech Supplies Pte Ltd",
    "contact@techsupplies.com"
)

# Create products using Supplier
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

# Display Supplier info through PhysicalProduct
print("=== Physical Product Supplier ===")
guitar.supplier.display_information()

print()

# Display Supplier info through DigitalProduct
print("=== Digital Product Supplier ===")
software.supplier.display_information()

print()

# Confirm both Products refer to the same Supplier
print(
    "Same Supplier:",
    guitar.supplier is software.supplier
)

print()

# Delete original Supplier variable
del supplier

# Products should still access Supplier
print("=== After Deleting Supplier Variable ===")
guitar.supplier.display_information()
software.supplier.display_information()
