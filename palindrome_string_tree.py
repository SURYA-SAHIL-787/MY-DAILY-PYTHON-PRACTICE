class Node:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None


class PalindromeTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        self.root = self._insert(self.root, word)

    def _insert(self, node, word):
        if node is None:
            return Node(word)

        if word < node.word:
            node.left = self._insert(node.left, word)
        elif word > node.word:
            node.right = self._insert(node.right, word)

        return node

    def inorder(self, result):
        self._inorder(self.root, result)

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.word)
            self._inorder(node.right, result)


def is_palindrome(word):
    cleaned_word = word.lower().replace(" ", "")
    return cleaned_word == cleaned_word[::-1]


words = [
    "level",
    "python",
    "radar",
    "tree",
    "madam",
    "array",
    "civic"
]

tree = PalindromeTree()
palindrome_count = 0

for word in words:
    if is_palindrome(word):
        tree.insert(word.lower())
        palindrome_count += 1

palindromes = []
tree.inorder(palindromes)

print("Original Array:", words)
print("Palindrome Strings:", palindromes)
print("Number of Palindromes:", palindrome_count)
