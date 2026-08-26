import heapq


class Customer:
    def __init__(self, name, movie, priority):
        self.name = name
        self.movie = movie
        self.priority = priority

    def __str__(self):
        return f"{self.name} - {self.movie}"


class PriorityBookingSystem:
    def __init__(self):
        self.queue = []
        self.counter = 0

    def add_customer(self, customer):
        self.counter += 1

        heapq.heappush(
            self.queue,
            (customer.priority, self.counter, customer)
        )

        print(
            f"{customer.name} added with "
            f"priority {customer.priority}."
        )

    def process_customer(self):
        if not self.queue:
            print("No customers waiting.")
            return

        priority, _, customer = heapq.heappop(self.queue)

        print(
            f"Processing: {customer.name} | "
            f"Movie: {customer.movie} | "
            f"Priority: {priority}"
        )

    def display_queue(self):
        if not self.queue:
            print("Queue is empty.")
            return

        print("\nPriority Booking Queue:")

        for priority, _, customer in sorted(self.queue):
            print(
                f"{customer.name} - "
                f"{customer.movie} - "
                f"Priority {priority}"
            )


system = PriorityBookingSystem()

system.add_customer(Customer("Aman", "Avatar", 3))
system.add_customer(Customer("Priya", "Inception", 1))
system.add_customer(Customer("Vijay", "Batman", 2))
system.add_customer(Customer("Anjali", "Interstellar", 1))

system.display_queue()

print("\nProcessing bookings:")
system.process_customer()
system.process_customer()
system.process_customer()
system.process_customer()
