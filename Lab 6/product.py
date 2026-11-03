class Product:
    """Represents and manages one product in the inventory."""

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        product_id = str(product_id).strip()
        name = str(name).strip()

        if not product_id:
            raise ValueError("Product ID cannot be empty.")
        if not name:
            raise ValueError("Product name cannot be empty.")

        try:
            price = float(price)
        except (TypeError, ValueError) as error:
            raise ValueError("Price must be a number.") from error

        if price < 0:
            raise ValueError("Price cannot be negative.")

        if isinstance(stock, bool) or not isinstance(stock, int):
            raise ValueError("Stock must be a whole number.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")

        # Double underscores indicate attributes intended to be private.
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def update_stock(self, quantity: int) -> None:
        """Set the product's stock to a new quantity."""
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise ValueError("Stock must be a whole number.")
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")

        self.__stock = quantity

    def display_information(self) -> None:
        print(f"Product ID: {self.__product_id}")
        print(f"Name:       {self.__name}")
        print(f"Price:      ${self.__price:.2f}")
        print(f"Stock:      {self.__stock}")
