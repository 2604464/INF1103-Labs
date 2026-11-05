
from product import (
    Product,
    PhysicalProduct,
    DigitalProduct,
    CanBeShipped
)

# Create physical product
guitar = PhysicalProduct(
    "P001",
    "Electric Guitar",
    599.90,
    10,
    4.5
)

# Create digital product
software = DigitalProduct(
    "P002",
    "Antivirus Software",
    49.90,
    100,
    250
)

# Test physical product
print("=== Physical Product ===")
guitar.display_information()
print(guitar.get_fulfilment_info())
print(f"Shipping Cost: ${guitar.calculate_shipping_cost():.2f}")

print()

# Test digital product
print("=== Digital Product ===")
software.display_information()
print(software.get_fulfilment_info())

print()

# Test interface implementation
print("=== Interface Tests ===")
print("Physical can be shipped:", isinstance(guitar, CanBeShipped))
print("Digital can be shipped:", isinstance(software, CanBeShipped))

print()

# Test abstract class
print("=== Abstract Class Test ===")

try:
    product = Product("P003", "Generic Product", 10, 5)  # type: ignore[abstract]
except TypeError as error:
    print("Successfully prevented Product instantiation.")
    print(error)
