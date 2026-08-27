import heapq


class Driver:
    def __init__(self, name, team, race_time):
        self.name = name
        self.team = team
        self.race_time = race_time


class RaceLeaderboard:
    def __init__(self):
        self.leaderboard = []

    def add_driver(self, driver):
        heapq.heappush(
            self.leaderboard,
            (driver.race_time, driver.name, driver)
        )

    def show_results(self):
        print("\nF1 Race Results")

        position = 1

        while self.leaderboard:
            race_time, _, driver = heapq.heappop(self.leaderboard)

            print(
                f"P{position}: {driver.name} - "
                f"{driver.team} - {race_time}s"
            )

            position += 1


race = RaceLeaderboard()

race.add_driver(Driver("Max Verstappen", "Red Bull", 5420.5))
race.add_driver(Driver("Lando Norris", "McLaren", 5418.2))
race.add_driver(Driver("Charles Leclerc", "Ferrari", 5425.8))
race.add_driver(Driver("George Russell", "Mercedes", 5422.1))

race.show_results()
