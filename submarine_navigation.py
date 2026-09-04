class Submarine:
    def __init__(self, name, depth, fuel, position):
        self.name = name
        self.depth = depth
        self.fuel = fuel
        self.position = position

    def dive(self, depth):
        self.depth += depth
        print(f"{self.name} dived to {self.depth} meters.")

    def move(self, x, y):
        self.position = (x, y)
        print(f"{self.name} moved to position {self.position}.")

    def status(self):
        print("\n--- Submarine Status ---")
        print("Name:", self.name)
        print("Depth:", self.depth, "meters")
        print("Fuel:", self.fuel, "%")
        print("Position:", self.position)


def check_safety(submarine):
    if submarine.depth > 1000:
        raise ValueError("Danger! Submarine has exceeded 1000 meters.")
    else:
        print("Depth is safe.")


# Main program
sub = Submarine("INS Varuna", 500, 80, (0, 0))

sub.status()

sub.dive(300)
check_safety(sub)

sub.move(10, 20)

sub.status()
