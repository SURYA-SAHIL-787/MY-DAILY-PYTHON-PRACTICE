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

    def get_words(self, node, prefix, result):
        if node.is_end:
            result.append(prefix)

        for ch, child in node.children.items():
            self.get_words(child, prefix + ch, result)

    def autocomplete(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        result = []
        self.get_words(node, prefix, result)

        return result


words = ["apple", "app", "application", "bat", "ball"]

trie = Trie()

for word in words:
    trie.insert(word)

prefix = input("Enter prefix: ")

result = trie.autocomplete(prefix)

print("Matching words:")

for word in result:
    print(word)
