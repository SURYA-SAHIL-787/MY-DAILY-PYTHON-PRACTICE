class Flight:
    def __init__(self, flight_number: str, total_seats: int):
        self.flight_number = flight_number
        self.available_seats = set(range(1, total_seats + 1))
        self.bookings = {}

    def book_seat(self, passenger_name: str, seat_number: int) -> bool:
        """Book a seat if it is available."""
        # TODO: Validate and book the requested seat.
        pass

    def cancel_booking(self, seat_number: int) -> bool:
        """Cancel a booking and make the seat available again."""
        # TODO: Remove the booking.
        pass

    def display_bookings(self) -> None:
        """Display passengers in ascending seat order."""
        # TODO: Sort and display the bookings.
        pass


if __name__ == "__main__":
    flight = Flight("AI-202", 5)

    flight.book_seat("Aarav", 2)
    flight.book_seat("Meera", 4)
    flight.cancel_booking(2)
    flight.display_bookings()
