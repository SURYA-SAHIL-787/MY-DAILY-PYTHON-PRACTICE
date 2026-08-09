class AlienDecoder:
    def __init__(self, symbol_map):
        self.symbol_map = symbol_map
        self.words = []
        self.results = []

    def add_word(self, word):
        self.words.append(word)

    def decode(self):
        for word in self.words:
            decoded = ""

            for ch in word:
                decoded += self.symbol_map.get(ch, "?")

            self.results.append((word, decoded))

    def display(self):
        unique_letters = set()

        for alien, decoded in self.results:
            print(alien, "->", decoded)

            for ch in decoded:
                unique_letters.add(ch)

        print("Unique decoded letters:", unique_letters)


mapping = {
    "@": "A",
    "#": "B",
    "$": "C",
    "%": "D"
}

decoder = AlienDecoder(mapping)

decoder.add_word("@#$")
decoder.add_word("$%@")
decoder.add_word("##@")

decoder.decode()
decoder.display()
