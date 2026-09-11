medals = [
    ("India", "Gold"),
    ("USA", "Gold"),
    ("India", "Silver"),
    ("USA", "Silver"),
    ("Japan", "Bronze"),
    ("India", "Bronze"),
    ("USA", "Gold"),
    ("Japan", "Gold"),
    ("India", "Gold")
]

country_count = {}

for country, medal in medals:
    country_count[country] = country_count.get(country, 0) + 1

best_country = max(country_count, key=country_count.get)

print("Total Medals:")

for country, count in country_count.items():
    print(country, ":", count)

print("Country with highest medals:", best_country)
