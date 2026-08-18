class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, name):
        node = self.root

        for ch in name.lower():
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.is_end = True

    def collect_names(self, node, prefix, result):
        if node.is_end:
            result.append(prefix)

        for ch, child in node.children.items():
            self.collect_names(child, prefix + ch, result)

    def search(self, prefix):
        node = self.root

        for ch in prefix.lower():
            if ch not in node.children:
                return []

            node = node.children[ch]

        result = []

        self.collect_names(node, prefix.lower(), result)

        return result


contacts = ["Alice", "Ali", "Alina", "Bob", "Bobby"]

trie = Trie()

for contact in contacts:
    trie.insert(contact)

search_word = input("Enter contact prefix: ")

result = trie.search(search_word)

print("Matching contacts:")

for name in result:
    print(name.capitalize())
