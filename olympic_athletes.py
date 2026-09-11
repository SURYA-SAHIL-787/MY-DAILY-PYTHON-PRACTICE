results = [
    ("Neeraj", "Gold"),
    ("Usain", "Gold"),
    ("Neeraj", "Silver"),
    ("Usain", "Gold"),
    ("Michael", "Gold"),
    ("Neeraj", "Bronze"),
    ("Michael", "Silver")
]

athlete_medals = {}

for athlete, medal in results:
    athlete_medals[athlete] = athlete_medals.get(athlete, 0) + 1

best_athlete = max(athlete_medals, key=athlete_medals.get)

print("Athlete Medal Count:")

for athlete, count in athlete_medals.items():
    print(athlete, ":", count)

print("Most successful athlete:", best_athlete)
