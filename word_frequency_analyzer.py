# word_frequency_analyzer.py

paragraph = """
Python is powerful and Python is easy to learn.
Dictionaries in Python are powerful because dictionaries store data in key value pairs.
"""

paragraph = paragraph.lower()

for symbol in [".", ",", "!", "?", "\n"]:
    paragraph = paragraph.replace(symbol, " ")

words = paragraph.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

longest_word = max(frequency.keys(), key=len)

most_repeated_word = max(frequency, key=frequency.get)

group_by_length = {}

for word in frequency.keys():
    length = len(word)

    if length not in group_by_length:
        group_by_length[length] = []

    group_by_length[length].append(word)

unique_words = []

for word, count in frequency.items():
    if count == 1:
        unique_words.append(word)

print("Word Frequency")
print("-" * 40)

for word, count in frequency.items():
    print(word, ":", count)

print("\nLongest Word:")
print(longest_word)

print("\nMost Repeated Word:")
print(most_repeated_word, ":", frequency[most_repeated_word])

print("\nWords Grouped By Length:")
for length, word_list in group_by_length.items():
    print(length, ":", word_list)

print("\nWords Appearing Only Once:")
print(unique_words)
