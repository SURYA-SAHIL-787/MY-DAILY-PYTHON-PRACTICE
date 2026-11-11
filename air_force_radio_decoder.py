class RadioDecoder:
    """
    Decode an Air Force radio message.

    Message format:
    * Words are separated by "/"
    * Each word contains dot-dash Morse code letters separated by spaces
    * For example: "... --- ..." decodes to "SOS"
    """

    MORSE_TO_LETTER = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
        ".": "E", "..-.": "F", "--.": "G", "....": "H",
        "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
        "--": "M", "-.": "N", "---": "O", ".--.": "P",
        "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
        "-.--": "Y", "--..": "Z",
        "-----": "0", ".----": "1", "..---": "2", "...--": "3",
        "....-": "4", ".....": "5", "-....": "6", "--...": "7",
        "---..": "8", "----.": "9",
    }

    def decode(self, message):
        decoded_words = []

        for encoded_word in message.strip().split("/"):
            letters = encoded_word.split()
            decoded_word = []

            for code in letters:
                if code not in self.MORSE_TO_LETTER:
                    raise ValueError(f"Unknown Morse code: {code}")
                decoded_word.append(self.MORSE_TO_LETTER[code])

            decoded_words.append("".join(decoded_word))

        return " ".join(decoded_words)


decoder = RadioDecoder()
print(decoder.decode("... --- ... / .- .-. . .-"))
# SOS AREA
