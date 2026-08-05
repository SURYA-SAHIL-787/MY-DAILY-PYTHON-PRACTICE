class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None


class CharacterTree:
    def __init__(self):
        self.root = None

    def insert(self, character, frequency):
        self.root = self._insert(
            self.root,
            character,
            frequency
        )

    def _insert(self, node, character, frequency):
        if node is None:
            return Node(character, frequency)

        if character < node.character:
            node.left = self._insert(
                node.left,
                character,
                frequency
            )
        elif character > node.character:
            node.right = self._insert(
                node.right,
                character,
                frequency
            )

        return node

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(
                f"Character: {node.character}, "
                f"Frequency: {node.frequency}"
            )
            self._inorder(node.right)


text = "programming"

frequency = [0] * 256

for character in text:
    frequency[ord(character)] += 1

tree = CharacterTree()

for index in range(256):
    if frequency[index] > 0:
        tree.insert(chr(index), frequency[index])

print("Character frequencies:")
tree.inorder()
