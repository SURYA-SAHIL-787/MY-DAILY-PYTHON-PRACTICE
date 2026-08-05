class Node:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None


class WordLengthTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        self.root = self._insert(self.root, word)

    def _insert(self, node, word):
        if node is None:
            return Node(word)

        if len(word) < len(node.word):
            node.left = self._insert(node.left, word)
        else:
            node.right = self._insert(node.right, word)

        return node

    def display_shortest_to_longest(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)

            print(
                f"{node.word} - "
                f"{len(node.word)} characters"
            )

            self._inorder(node.right)

    def find_longest_word(self):
        if self.root is None:
            return None

        current = self.root

        while current.right is not None:
            current = current.right

        return current.word


sentence = "Python arrays strings and trees are useful"

words = sentence.split()

tree = WordLengthTree()

for word in words:
    tree.insert(word)

print("Array of Words:")
print(words)

print("\nWords from shortest to longest:")
tree.display_shortest_to_longest()

longest_word = tree.find_longest_word()

print(
    f"\nLongest Word: {longest_word} "
    f"({len(longest_word)} characters)"
)
