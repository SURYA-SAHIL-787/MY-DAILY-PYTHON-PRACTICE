from collections import deque


class Customer:
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def __str__(self):
        return f"{self.name} - {self.movie}"


class BookingQueue:
    def __init__(self):
        self.queue = deque()

    def add_customer(self, customer):
        self.queue.append(customer)
        print(f"{customer.name} added to booking queue.")

    def process_booking(self):
        if not self.queue:
            print("No customers in queue.")
            return

        customer = self.queue.popleft()
        print(f"Booking processed for {customer.name} - {customer.movie}")

    def display_queue(self):
        if not self.queue:
            print("Booking queue is empty.")
            return

        print("\nCurrent Booking Queue:")
        for customer in self.queue:
            print(customer)


booking_queue = BookingQueue()

booking_queue.add_customer(Customer("Arjun", "Avengers"))
booking_queue.add_customer(Customer("Neha", "Interstellar"))
booking_queue.add_customer(Customer("Rahul", "Inception"))

booking_queue.display_queue()

booking_queue.process_booking()

booking_queue.display_queue()
