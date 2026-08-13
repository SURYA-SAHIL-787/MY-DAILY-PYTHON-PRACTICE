class Firefighter:
    def __init__(self, firefighter_id, name, rank, rescues):
        self.firefighter_id = firefighter_id
        self.name = name
        self.rank = rank
        self.rescues = rescues

    def display_details(self):
        print("Firefighter ID:", self.firefighter_id)
        print("Name:", self.name)
        print("Rank:", self.rank)
        print("Rescue Operations:", self.rescues)

    def complete_rescue(self):
        self.rescues += 1
        print("\nRescue operation recorded successfully.")


firefighter1 = Firefighter(201, "Rahul", "Station Officer", 12)

print("FIREFIGHTER DETAILS")
firefighter1.display_details()

firefighter1.complete_rescue()

print("\nUPDATED DETAILS")
firefighter1.display_details()
