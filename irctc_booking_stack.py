class BookingManager:
    def __init__(self):
        self.bookings = []

    def book_ticket(self, passenger):
        self.bookings.append(passenger)
        print(passenger, "ticket booked.")

    def cancel_last_booking(self):
        if self.bookings:
            passenger = self.bookings.pop()
            print(passenger, "booking cancelled.")
        else:
            print("No bookings available.")


manager = BookingManager()

manager.book_ticket("Sahil")
manager.book_ticket("Aman")
manager.book_ticket("Neha")

manager.cancel_last_booking()
