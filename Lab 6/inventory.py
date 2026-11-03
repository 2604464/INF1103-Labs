from product import Product


class Inventory:
    """Manages a collection of Product objects."""

    def __init__(self):
        self.__products = []

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to the inventory.")

        if self.search_product(product.get_product_id()) is not None:
            raise ValueError("A product with this ID already exists.")

        self.__products.append(product)

    def search_product(self, product_id: str):
        product_id = str(product_id).strip().lower()

        for product in self.__products:
            if product.get_product_id().lower() == product_id:
                return product

        return None

    def display_all(self) -> None:
        if not self.__products:
            print("The inventory is empty.")
            return

        print("\n--- All Products ---")
        for product in self.__products:
            product.display_information()
            print("--------------------")

    def get_all_products(self) -> list:
        """Return a copy so outside code cannot edit the internal list directly."""
        return self.__products.copy()
