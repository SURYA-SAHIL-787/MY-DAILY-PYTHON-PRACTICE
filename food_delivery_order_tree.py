class OrderNode:
    def __init__(self, food_name, price):
        self.food_name = food_name
        self.price = price
        self.left = None
        self.right = None


def calculate_total(root):
    if root is None:
        return 0

    return (
        root.price
        + calculate_total(root.left)
        + calculate_total(root.right)
    )


def find_expensive_order(root):
    if root is None:
        return None

    expensive = root

    left_expensive = find_expensive_order(root.left)
    right_expensive = find_expensive_order(root.right)

    if (
        left_expensive is not None
        and left_expensive.price > expensive.price
    ):
        expensive = left_expensive

    if (
        right_expensive is not None
        and right_expensive.price > expensive.price
    ):
        expensive = right_expensive

    return expensive


root = OrderNode("Pizza", 350)

root.left = OrderNode("Burger", 180)
root.right = OrderNode("Biryani", 280)

root.left.left = OrderNode("Sandwich", 120)
root.left.right = OrderNode("Pasta", 220)

root.right.left = OrderNode("Dosa", 100)
root.right.right = OrderNode("Family Meal", 500)

total_price = calculate_total(root)
expensive_order = find_expensive_order(root)

print("Total value of all food orders:", total_price)

print(
    "Most expensive order:",
    expensive_order.food_name
)

print(
    "Price of most expensive order:",
    expensive_order.price
)
