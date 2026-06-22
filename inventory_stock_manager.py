# inventory_stock_manager.py

inventory = {
    "Laptop": {"quantity": 5, "price": 55000},
    "Mouse": {"quantity": 25, "price": 600},
    "Keyboard": {"quantity": 15, "price": 1200},
    "Monitor": {"quantity": 7, "price": 9000}
}

new_stock = {
    "Laptop": 3,
    "Mouse": 10,
    "Printer": 4
}

sold_items = {
    "Mouse": 8,
    "Keyboard": 5,
    "Monitor": 2
}

for item, qty in new_stock.items():
    if item in inventory:
        inventory[item]["quantity"] += qty
    else:
        inventory[item] = {
            "quantity": qty,
            "price": int(input(f"Enter price for {item}: "))
        }

for item, qty in sold_items.items():
    if item in inventory:
        if inventory[item]["quantity"] >= qty:
            inventory[item]["quantity"] -= qty
        else:
            print(f"Not enough stock for {item}")
    else:
        print(f"{item} not found in inventory")

total_value = 0
product_values = {}

for item, details in inventory.items():
    value = details["quantity"] * details["price"]
    product_values[item] = value
    total_value += value

low_stock = {}

for item, details in inventory.items():
    if details["quantity"] < 5:
        low_stock[item] = details["quantity"]

most_valuable = max(product_values, key=product_values.get)

print("\nUpdated Inventory")
print("-" * 40)

for item, details in inventory.items():
    print(item, details)

print("\nTotal Inventory Value:", total_value)

print("\nLow Stock Items:")
print(low_stock)

print("\nMost Valuable Product:")
print(most_valuable, product_values[most_valuable])
