class TreeNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None


def count_vowel_words(root):
    if root is None:
        return 0

    count = 0

    if root.word and root.word[0].lower() in "aeiou":
        count = 1

    return (
        count
        + count_vowel_words(root.left)
        + count_vowel_words(root.right)
    )


root = TreeNode("Apple")
root.left = TreeNode("Banana")
root.right = TreeNode("Orange")
root.left.left = TreeNode("Umbrella")
root.left.right = TreeNode("Mango")
root.right.left = TreeNode("Elephant")
root.right.right = TreeNode("Grapes")

result = count_vowel_words(root)

print("Number of strings beginning with a vowel:", result)
