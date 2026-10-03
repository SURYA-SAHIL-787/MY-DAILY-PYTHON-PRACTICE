import heapq


class Passenger:
    def __init__(
        self,
        passenger_id: str,
        name: str,
        ticket_class: str,
        medical_priority: bool = False,
    ):
        self.passenger_id = passenger_id
        self.name = name
        self.ticket_class = ticket_class
        self.medical_priority = medical_priority

    def __repr__(self):
        return f"{self.passenger_id} - {self.name}"


class CheckInSystem:
    def __init__(self):
        self.queue = []
        self.arrival_number = 0

    def calculate_priority(self, passenger: Passenger) -> int:
        """Calculate the passenger's check-in priority."""
        # TODO: Return 1, 2, or 3 according to the priority rules.
        pass

    def add_passenger(self, passenger: Passenger) -> None:
        """Add a passenger to the priority queue."""
        # TODO:
        # Use (priority, arrival_number, passenger) as the heap entry.
        pass

    def check_in_next(self):
        """Remove and return the highest-priority passenger."""
        # TODO: Return None when the queue is empty.
        pass


if __name__ == "__main__":
    system = CheckInSystem()

    system.add_passenger(Passenger("P101", "Arjun", "Economy"))
    system.add_passenger(Passenger("P102", "Sara", "Business"))
    system.add_passenger(
        Passenger("P103", "Vikram", "Economy", medical_priority=True)
    )

    while system.queue:
        print("Checking in:", system.check_in_next())
