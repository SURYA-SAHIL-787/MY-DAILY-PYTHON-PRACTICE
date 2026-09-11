medals = [
    ("India", "Gold"),
    ("USA", "Gold"),
    ("India", "Silver"),
    ("USA", "Gold"),
    ("Japan", "Bronze"),
    ("India", "Gold"),
    ("USA", "Silver"),
    ("Japan", "Gold")
]

gold_count = {}

for country, medal in medals:
    if medal == "Gold":
        gold_count[country] = gold_count.get(country, 0) + 1

winner = max(gold_count, key=gold_count.get)

print("Gold Medal Counts:")
for country, count in gold_count.items():
    print(country, ":", count)

print("Country with most gold medals:", winner)
