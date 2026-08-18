class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.is_end = True

    def longest_common_prefix(self):
        node = self.root
        prefix = ""

        while len(node.children) == 1 and not node.is_end:
            ch = next(iter(node.children))

            prefix += ch
            node = node.children[ch]

        return prefix


words = ["flower", "flow", "flight"]

trie = Trie()

for word in words:
    trie.insert(word)

print("Longest Common Prefix:", trie.longest_common_prefix())
