class TimeMachine:
    def __init__(self):
        self.travellers = {}
        self.journeys = []

    def add_journey(self, name, year):
        if name not in self.travellers:
            self.travellers[name] = []

        self.travellers[name].append(year)
        self.journeys.append((name, year))

    def display(self):
        all_years = set()

        for name, years in self.travellers.items():
            print(name.upper(), "visited:", years)

            for year in years:
                all_years.add(year)

        print("Unique years visited:", all_years)

        print("All journeys:")

        for journey in self.journeys:
            print(journey)


machine = TimeMachine()

machine.add_journey("Arun", 2050)
machine.add_journey("Maya", 1800)
machine.add_journey("Arun", 3000)
machine.add_journey("Ravi", 2050)
machine.add_journey("Maya", 1500)

machine.display()
