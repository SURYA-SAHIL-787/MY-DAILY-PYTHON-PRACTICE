from collections import deque


class SubmarineEmergency:
    def __init__(self):
        self.queue = deque()

    def add_compartment(self, name):
        self.queue.append(name)
        print(f"Added: {name}")

    def evacuate(self):
        if not self.queue:
            print("No compartments remaining.")
        else:
            compartment = self.queue.popleft()
            print("Evacuating:", compartment)

    def show_remaining(self):
        print("\nRemaining compartments:")
        for compartment in self.queue:
            print(compartment)


def emergency_check(fuel, oxygen):
    if fuel < 20:
        raise ValueError("Emergency! Fuel level is below 20%.")

    if oxygen < 30:
        raise ValueError("Emergency! Oxygen level is below 30%.")

    print("Fuel and oxygen levels are safe.")


# Main program
submarine = SubmarineEmergency()

compartments = [
    "Engine Room",
    "Control Room",
    "Battery Room",
    "Crew Quarters"
]

for compartment in compartments:
    submarine.add_compartment(compartment)

print("\n--- Emergency Check ---")

try:
    emergency_check(50, 70)

except ValueError as e:
    print(e)

print("\n--- Evacuation ---")

while submarine.queue:
    submarine.evacuate()

submarine.show_remaining()
