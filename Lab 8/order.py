from product import Product


class OrderLine:
    """Represents a product and its quantity in an order."""

    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        """Calculate the subtotal for this order line."""

        return self.product.get_price() * self.quantity


class Order:
    """Represents an order containing multiple OrderLine objects."""

    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        """Create and add a new OrderLine to this Order."""

        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        """Calculate the total value of the order."""

        total = 0.0

        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()

        return total

    def remove_order_line(self, index: int) -> bool:
        """Remove an OrderLine using its position in the order."""

        if index < 0 or index >= len(self.order_lines):
            return False

        self.order_lines.pop(index)
        return True
