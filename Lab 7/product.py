
from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    """Interface defining shipping-related behaviour."""

    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass


class Product(ABC):
    """Abstract class representing a product in the inventory."""

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

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return information about how the product is delivered."""
        pass


class PhysicalProduct(Product, CanBeShipped):
    """Represents a physical product that requires shipping."""

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float
    ):
        super().__init__(product_id, name, price, stock)

        try:
            weight = float(weight)
        except (TypeError, ValueError) as error:
            raise ValueError("Weight must be a number.") from error

        if weight < 0:
            raise ValueError("Weight cannot be negative.")

        self.__weight = weight

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight:     {self.__weight} kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return 5.00 + (self.__weight * 2.00)


class DigitalProduct(Product):
    """Represents a digital product delivered electronically."""

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: float
    ):
        super().__init__(product_id, name, price, stock)

        try:
            download_size = float(download_size)
        except (TypeError, ValueError) as error:
            raise ValueError("Download size must be a number.") from error

        if download_size < 0:
            raise ValueError("Download size cannot be negative.")

        self.__download_size = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."
