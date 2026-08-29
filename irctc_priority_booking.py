import heapq


class Passenger:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


class BookingSystem:
    def __init__(self):
        self.queue = []

    def add_passenger(self, passenger):
        heapq.heappush(
            self.queue,
            (passenger.priority, passenger.name)
        )

    def confirm_ticket(self):
        if self.queue:
            priority, name = heapq.heappop(self.queue)

            print(
                "Ticket confirmed for",
                name,
                "| Priority:",
                priority
            )


system = BookingSystem()

system.add_passenger(Passenger("Rahul", 3))
system.add_passenger(Passenger("Priya", 1))
system.add_passenger(Passenger("Arun", 2))

system.confirm_ticket()
system.confirm_ticket()
system.confirm_ticket()
