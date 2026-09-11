results = [
    ("Neeraj", "Gold"),
    ("Neeraj", "Silver"),
    ("Phelps", "Gold"),
    ("Neeraj", "Bronze"),
    ("Phelps", "Gold"),
    ("Bolt", "Gold"),
    ("Bolt", "Silver"),
    ("Phelps", "Bronze")
]

athletes = {}

for athlete, medal in results:

    if athlete not in athletes:
        athletes[athlete] = {
            "Gold": 0,
            "Silver": 0,
            "Bronze": 0
        }

    athletes[athlete][medal] += 1

for athlete, medals in athletes.items():
    total = sum(medals.values())

    print(athlete)
    print("Gold:", medals["Gold"])
    print("Silver:", medals["Silver"])
    print("Bronze:", medals["Bronze"])
    print("Total:", total)
    print()
