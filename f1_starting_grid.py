class Driver:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def __str__(self):
        return f"{self.name} - {self.team}"


class StartingGrid:
    def __init__(self):
        self.drivers = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def display_grid(self):
        print("\nF1 Starting Grid")
        for position, driver in enumerate(self.drivers, start=1):
            print(f"P{position}: {driver}")


grid = StartingGrid()

grid.add_driver(Driver("Max Verstappen", "Red Bull"))
grid.add_driver(Driver("Lando Norris", "McLaren"))
grid.add_driver(Driver("Charles Leclerc", "Ferrari"))
grid.add_driver(Driver("George Russell", "Mercedes"))

grid.display_grid()
