medals = [
    "Gold", "Silver", "Gold", "Bronze",
    "Silver", "Gold", "Bronze", "Bronze"
]

count = {}

for medal in medals:
    count[medal] = count.get(medal, 0) + 1

print("Olympic Medal Count:")

for medal, total in count.items():
    print(medal, ":", total)
