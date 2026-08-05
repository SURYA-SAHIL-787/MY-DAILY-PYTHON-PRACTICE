class Node:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None


class WordBST:
    def __init__(self):
        self.root = None

    def insert(self, word):
        self.root = self._insert(self.root, word.lower())

    def _insert(self, node, word):
        if node is None:
            return Node(word)

        if word < node.word:
            node.left = self._insert(node.left, word)
        elif word > node.word:
            node.right = self._insert(node.right, word)

        return node

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.word, end=" ")
            self._inorder(node.right)

    def search(self, word):
        current = self.root
        word = word.lower()

        while current is not None:
            if word == current.word:
                return True
            elif word < current.word:
                current = current.left
            else:
                current = current.right

        return False


words = ["Mango", "Apple", "Orange", "Banana", "Grapes"]

tree = WordBST()

for word in words:
    tree.insert(word)

print("Words in alphabetical order:")
tree.inorder()

search_word = "Orange"

if tree.search(search_word):
    print(f"\n{search_word} is present in the tree.")
else:
    print(f"\n{search_word} is not present in the tree.")
