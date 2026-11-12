
from supplier import Supplier
from product import PhysicalProduct, DigitalProduct
from order import Order

# Create Supplier
supplier = Supplier(
    "S001",
    "Tech Supplies Pte Ltd",
    "contact@techsupplies.com"
)

# Create Products independently
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

# Create Order 1
order1 = Order("ORD001")

# Add products to Order 1
order1.add_order_line(guitar, 2)
order1.add_order_line(software, 3)

# Display Order 1
print("=== Order 1 ===")
print("Order ID:", order1.order_id)

for line in order1.order_lines:
    print(
        f"Product: {line.product.get_name()}, "
        f"Quantity: {line.quantity}, "
        f"Subtotal: ${line.calculate_subtotal():.2f}"
    )

print(f"Order Total: ${order1.calculate_total():.2f}")

# Create Order 2
order2 = Order("ORD002")

# Add same Product to another Order
order2.add_order_line(guitar, 1)

print("\n=== Order 2 ===")
print("Order ID:", order2.order_id)

for line in order2.order_lines:
    print(
        f"Product: {line.product.get_name()}, "
        f"Quantity: {line.quantity}, "
        f"Subtotal: ${line.calculate_subtotal():.2f}"
    )

print(f"Order Total: ${order2.calculate_total():.2f}")

# Compare OrderLine objects
print("\n=== Composition Tests ===")

print(
    "Same Product Object:",
    order1.order_lines[0].product is order2.order_lines[0].product
)

print(
    "Same OrderLine Object:",
    order1.order_lines[0] is order2.order_lines[0]
)

print(
    "Number of OrderLine Objects:",
    len(order1.order_lines) + len(order2.order_lines)
)

# Remove an OrderLine through its Order
print("\n=== Remove OrderLine ===")

removed = order1.remove_order_line(0)

print("OrderLine removed:", removed)
print("Remaining Order 1 lines:", len(order1.order_lines))
print(f"Updated Order 1 Total: ${order1.calculate_total():.2f}")

# Confirm Product still exists
print("\n=== Product After OrderLine Removal ===")
guitar.display_information()
