class Booking:
    def __init__(self, booking_id, customer, movie):
        self.booking_id = booking_id
        self.customer = customer
        self.movie = movie

    def __str__(self):
        return f"{self.booking_id} - {self.customer} - {self.movie}"


class BookingSystem:
    def __init__(self):
        self.bookings = []

    def book_ticket(self, booking):
        self.bookings.append(booking)
        print(f"Booking {booking.booking_id} confirmed.")

    def cancel_last_booking(self):
        if not self.bookings:
            print("No bookings available to cancel.")
            return

        cancelled = self.bookings.pop()

        print(
            f"Cancelled booking: "
            f"{cancelled.booking_id} - {cancelled.customer}"
        )

    def display_bookings(self):
        if not self.bookings:
            print("No active bookings.")
            return

        print("\nActive Bookings:")
        for booking in self.bookings:
            print(booking)


system = BookingSystem()

system.book_ticket(Booking(101, "Kiran", "Avatar"))
system.book_ticket(Booking(102, "Meera", "Batman"))
system.book_ticket(Booking(103, "Rohan", "Superman"))

system.display_bookings()

print("\nCancelling most recent booking...")
system.cancel_last_booking()

system.display_bookings()
