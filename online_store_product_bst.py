class ProductNode:
    def __init__(self, product_name):
        self.product_name = product_name
        self.left = None
        self.right = None


class ProductBST:
    def insert(self, root, product_name):
        if root is None:
            return ProductNode(product_name)

        if product_name.lower() < root.product_name.lower():
            root.left = self.insert(
                root.left, product_name
            )

        elif product_name.lower() > root.product_name.lower():
            root.right = self.insert(
                root.right, product_name
            )

        return root

    def search(self, root, product_name):
        if root is None:
            return False

        if product_name.lower() == root.product_name.lower():
            return True

        if product_name.lower() < root.product_name.lower():
            return self.search(root.left, product_name)

        return self.search(root.right, product_name)

    def display_products(self, root):
        if root:
            self.display_products(root.left)
            print(root.product_name)
            self.display_products(root.right)


store = ProductBST()
root = None

products = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Camera",
    "Smartwatch"
]

for product in products:
    root = store.insert(root, product)

print("Available products:")

store.display_products(root)

search_product = input("\nEnter product to search: ")

if store.search(root, search_product):
    print(search_product, "is available in the store.")
else:
    print(search_product, "is not available in the store.")
