class TreeNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None


class BinarySearchTree:
    def insert(self, root, word):
        if root is None:
            return TreeNode(word)

        if word.lower() < root.word.lower():
            root.left = self.insert(root.left, word)
        elif word.lower() > root.word.lower():
            root.right = self.insert(root.right, word)

        return root


def find_longest_string(root):
    if root is None:
        return ""

    left_longest = find_longest_string(root.left)
    right_longest = find_longest_string(root.right)

    longest = root.word

    if len(left_longest) > len(longest):
        longest = left_longest

    if len(right_longest) > len(longest):
        longest = right_longest

    return longest


tree = BinarySearchTree()
root = None

words = [
    "Python",
    "Tree",
    "Programming",
    "AVL",
    "Algorithm",
    "DataStructure"
]

for word in words:
    root = tree.insert(root, word)

longest_word = find_longest_string(root)

print("Longest string in the tree:", longest_word)
print("Length of the string:", len(longest_word))
