import string
from collections import Counter


def clean_word(word):
    cleaned = word.lower().strip(string.punctuation)
    return cleaned


def count_characters(text):
    return len(text)


def count_words(text):
    words = text.split()
    return len(words)


def count_lines(text):
    if not text:
        return 0

    return len(text.splitlines())


def count_sentences(text):
    sentence_endings = ".!?"
    count = 0

    for character in text:
        if character in sentence_endings:
            count += 1

    return count


def get_word_frequency(text):
    words = text.split()
    cleaned_words = []

    for word in words:
        cleaned = clean_word(word)

        if cleaned:
            cleaned_words.append(cleaned)

    return Counter(cleaned_words)


def display_top_words(frequency, limit=10):
    if not frequency:
        print("No words found.")
        return

    print(f"\nTop {limit} Words:")

    for word, count in frequency.most_common(limit):
        print(f"{word}: {count}")


def analyze_text(text):
    characters = count_characters(text)
    words = count_words(text)
    lines = count_lines(text)
    sentences = count_sentences(text)
    frequency = get_word_frequency(text)

    print("\n===== TEXT ANALYSIS RESULT =====")
    print(f"Characters: {characters}")
    print(f"Words     : {words}")
    print(f"Lines     : {lines}")
    print(f"Sentences : {sentences}")

    display_top_words(frequency)


def read_manual_input():
    print("\nEnter your text.")
    print("Type END on a new line to finish.\n")

    lines = []

    while True:
        line = input()

        if line == "END":
            break

        lines.append(line)

    return "\n".join(lines)


def read_file_input():
    file_name = input("\nEnter file name: ").strip()

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return ""
    except PermissionError:
        print("Permission denied.")
        return ""


def menu():
    while True:
        print("\n===== TEXT ANALYZER =====")
        print("1. Enter Text Manually")
        print("2. Analyze Text File")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            text = read_manual_input()
            analyze_text(text)
        elif choice == "2":
            text = read_file_input()

            if text:
                analyze_text(text)
        elif choice == "3":
            print("Exiting Text Analyzer.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
