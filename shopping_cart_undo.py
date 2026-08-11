class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - Rs.{self.price}"


class ShoppingCart:
    def __init__(self):
        self.cart = {}
        self.history = []

    def add_product(self, product):
        self.cart[product.name] = product

        self.history.append(
            ("ADD", product)
        )

        print(f"{product.name} added to cart.")

    def remove_product(self, product_name):
        if product_name not in self.cart:
            print("Product not found in cart.")
            return

        product = self.cart.pop(product_name)

        self.history.append(
            ("REMOVE", product)
        )

        print(f"{product_name} removed from cart.")

    def undo(self):
        if not self.history:
            print("No operation to undo.")
            return

        operation, product = self.history.pop()

        if operation == "ADD":
            self.cart.pop(product.name, None)

            print(
                f"Undo: {product.name} removed from cart."
            )

        elif operation == "REMOVE":
            self.cart[product.name] = product

            print(
                f"Undo: {product.name} added back to cart."
            )

    def display_cart(self):
        if not self.cart:
            print("\nCart is empty.")
            return

        print("\nShopping Cart:")

        total = 0

        for product in self.cart.values():
            print(product)
            total += product.price

        print("Total Price: Rs.", total)


cart = ShoppingCart()

cart.add_product(Product("Keyboard", 1500))
cart.add_product(Product("Mouse", 700))
cart.add_product(Product("Headphones", 2000))

cart.display_cart()

cart.remove_product("Mouse")

cart.display_cart()

print("\nUndoing last operation...")
cart.undo()

cart.display_cart()
