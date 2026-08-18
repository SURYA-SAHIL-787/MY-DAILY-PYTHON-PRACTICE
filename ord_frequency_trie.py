class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.count += 1

    def display_words(self, node=None, word=""):
        if node is None:
            node = self.root

        if node.count > 0:
            print(word, "->", node.count)

        for ch, child in node.children.items():
            self.display_words(child, word + ch)


sentence = input("Enter a sentence: ")

words = sentence.lower().split()

trie = Trie()

for word in words:
    trie.insert(word)

print("Word frequencies:")

trie.display_words()
