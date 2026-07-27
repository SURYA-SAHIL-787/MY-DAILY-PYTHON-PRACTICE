class AVLNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, node):
        new_root = node.left
        temporary = new_root.right

        new_root.right = node
        node.left = temporary

        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

        new_root.height = 1 + max(
            self.get_height(new_root.left),
            self.get_height(new_root.right)
        )

        return new_root

    def left_rotate(self, node):
        new_root = node.right
        temporary = new_root.left

        new_root.left = node
        node.right = temporary

        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

        new_root.height = 1 + max(
            self.get_height(new_root.left),
            self.get_height(new_root.right)
        )

        return new_root

    def insert(self, root, word):
        if root is None:
            return AVLNode(word)

        if word < root.word:
            root.left = self.insert(root.left, word)
        elif word > root.word:
            root.right = self.insert(root.right, word)
        else:
            return root

        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root)

        # Left-Left case
        if balance > 1 and word < root.left.word:
            return self.right_rotate(root)

        # Right-Right case
        if balance < -1 and word > root.right.word:
            return self.left_rotate(root)

        # Left-Right case
        if balance > 1 and word > root.left.word:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left case
        if balance < -1 and word < root.right.word:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.word, end=" ")
            self.inorder(root.right)


tree = AVLTree()
root = None

words = ["Mango", "Apple", "Orange", "Banana", "Grapes"]

for word in words:
    root = tree.insert(root, word)

print("Words in alphabetical order:")
tree.inorder(root)
