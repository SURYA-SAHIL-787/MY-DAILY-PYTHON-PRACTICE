class TreeNode:
    def __init__(self, city):
        self.city = city
        self.left = None
        self.right = None


class BinarySearchTree:
    def insert(self, root, city):
        if root is None:
            return TreeNode(city)

        if city.lower() < root.city.lower():
            root.left = self.insert(root.left, city)
        elif city.lower() > root.city.lower():
            root.right = self.insert(root.right, city)

        return root

    def search(self, root, city):
        if root is None:
            return False

        if city.lower() == root.city.lower():
            return True

        if city.lower() < root.city.lower():
            return self.search(root.left, city)

        return self.search(root.right, city)


tree = BinarySearchTree()
root = None

cities = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Bengaluru"]

for city in cities:
    root = tree.insert(root, city)

search_city = input("Enter the city to search: ")

if tree.search(root, search_city):
    print(search_city, "is present in the tree.")
else:
    print(search_city, "is not present in the tree.")
