class Order:
    def __init__(self, distance):
        self.distance = distance


class ZomatoOrder(Order):

    def __init__(self, distance, restaurant_open, partner_available):

        super().__init__(distance)

        self.restaurant_open = restaurant_open
        self.partner_available = partner_available

    def check_order(self):

        if self.restaurant_open != "yes":
            return "Restaurant is closed"

        elif self.distance > 12:
            return "Location outside delivery range"

        elif self.partner_available != "yes":
            return "No delivery partner available"

        else:
            return "Order Accepted"


distance = float(input("Enter distance: "))

restaurant = input("Restaurant open? (yes/no): ").lower()

partner = input("Delivery partner available? (yes/no): ").lower()


order = ZomatoOrder(
    distance,
    restaurant,
    partner
)

print(order.check_order())
