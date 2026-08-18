class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        reversed_word = word[::-1]

        node = self.root

        for ch in reversed_word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]
            node.words.append(word)

    def search_suffix(self, suffix):
        reversed_suffix = suffix[::-1]

        node = self.root

        for ch in reversed_suffix:
            if ch not in node.children:
                return []

            node = node.children[ch]

        return node.words


words = ["playing", "reading", "player", "singing", "book"]

trie = Trie()

for word in words:
    trie.insert(word)

suffix = input("Enter suffix: ")

result = trie.search_suffix(suffix)

print("Words ending with", suffix, ":")

for word in result:
    print(word)
