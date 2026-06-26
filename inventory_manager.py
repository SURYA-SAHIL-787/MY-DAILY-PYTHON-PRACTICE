class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def sell_item(self, item_name, quantity):
        if item_name not in self.items:
            print("Item not found")
        elif self.items[item_name] < quantity:
            print("Not enough stock")
        else:
            self.items[item_name] -= quantity
            print(f"{quantity} {item_name} sold")

    def show_inventory(self):
        print("\nInventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")


shop = Inventory()

shop.add_item("Pen", 50)
shop.add_item("Notebook", 30)
shop.add_item("Pencil", 40)

shop.show_inventory()

shop.sell_item("Pen", 10)

shop.show_inventory()
