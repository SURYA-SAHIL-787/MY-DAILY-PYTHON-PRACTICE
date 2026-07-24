class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def product_details(self):
        return (
            self.name,
            self.price,
            self.quantity,
            self.calculate_total()
        )


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_bill(self):
        total_bill = 0

        for product in self.products:
            total_bill += product.calculate_total()

        return total_bill

    def display_cart(self):
        print("Shopping cart:")

        for product in self.products:
            details = product.product_details()

            print(
                f"Product: {details[0]}, "
                f"Price: {details[1]}, "
                f"Quantity: {details[2]}, "
                f"Total: {details[3]}"
            )

        print("Final bill:", self.calculate_bill())


cart = ShoppingCart()

cart.add_product(Product("Mouse", 700, 2))
cart.add_product(Product("Keyboard", 1500, 1))
cart.add_product(Product("USB Cable", 300, 3))

cart.display_cart()
