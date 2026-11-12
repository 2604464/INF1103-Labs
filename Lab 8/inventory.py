from product import Product


class Inventory:
    """Manages a collection of Product objects."""

    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        """Add an existing Product object to the inventory."""

        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to the inventory.")

        if self.find_product(product.get_product_id()) is not None:
            raise ValueError("A product with this ID already exists.")

        self.__products.append(product)

    def remove_product(self, product_id: str) -> bool:
        """Remove a Product reference using its product ID."""

        product = self.find_product(product_id)

        if product is None:
            return False

        self.__products.remove(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        """Find a Product by ID. Return None if not found."""

        product_id = str(product_id).strip().lower()

        for product in self.__products:
            if product.get_product_id().lower() == product_id:
                return product

        return None

    def search_product(self, product_id: str) -> Product | None:
        """Maintain compatibility with the existing Lab 7 main.py."""

        return self.find_product(product_id)

    def display_all(self) -> None:
        """Display all products in the inventory."""

        if not self.__products:
            print("The inventory is empty.")
            return

        print("\n--- All Products ---")

        for product in self.__products:
            product.display_information()
            print("--------------------")

    def display_all_products(self) -> None:
        """Display all products using the Lab 8 method name."""

        self.display_all()

    def get_all_products(self) -> list[Product]:
        """Return a copy of the product collection."""

        return self.__products.copy()
