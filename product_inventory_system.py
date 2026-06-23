# Question Name: Product Inventory System Using Set, Dictionary, and Tuple
# Concept: Sets + Dictionaries + Tuples

# Dictionary:
# key = product ID
# value = tuple containing product name, category, price

products = {
    1: ("Laptop", "Electronics", 55000),
    2: ("Mouse", "Electronics", 700),
    3: ("Notebook", "Stationery", 60),
    4: ("Pen", "Stationery", 20),
    5: ("Chair", "Furniture", 2500)
}

categories = set()

for product in products.values():
    categories.add(product[1])

print("Product Inventory:")
for product_id, details in products.items():
    print("Product ID:", product_id)
    print("Name:", details[0])
    print("Category:", details[1])
    print("Price:", details[2])
    print()

print("Available Categories:")
print(categories)

max_price = int(input("Enter maximum price: "))

print("\nProducts below or equal to", max_price, ":")
found = False

for product_id, details in products.items():
    if details[2] <= max_price:
        print(product_id, "-", details[0], "-", details[2])
        found = True

if not found:
    print("No products found within this price range")
