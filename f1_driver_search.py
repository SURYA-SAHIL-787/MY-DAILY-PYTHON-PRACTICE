class Driver:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def __str__(self):
        return f"{self.name} - {self.team}"


class DriverDatabase:
    def __init__(self):
        self.drivers = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def sort_drivers(self):
        self.drivers.sort(key=lambda driver: driver.name.lower())

    def binary_search(self, name):
        self.sort_drivers()

        low = 0
        high = len(self.drivers) - 1

        while low <= high:
            mid = (low + high) // 2

            current_name = self.drivers[mid].name.lower()
            target_name = name.lower()

            if current_name == target_name:
                return self.drivers[mid]

            elif current_name < target_name:
                low = mid + 1

            else:
                high = mid - 1

        return None


database = DriverDatabase()

database.add_driver(Driver("Charles Leclerc", "Ferrari"))
database.add_driver(Driver("Max Verstappen", "Red Bull"))
database.add_driver(Driver("Lando Norris", "McLaren"))
database.add_driver(Driver("George Russell", "Mercedes"))
database.add_driver(Driver("Fernando Alonso", "Aston Martin"))

search_name = "Lando Norris"

result = database.binary_search(search_name)

if result:
    print("Driver Found:")
    print(result)
else:
    print("Driver not found.")
