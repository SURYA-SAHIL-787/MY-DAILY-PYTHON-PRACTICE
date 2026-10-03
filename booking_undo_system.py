class Booking:
    def __init__(self, booking_id: str, passenger_name: str, flight_number: str):
        self.booking_id = booking_id
        self.passenger_name = passenger_name
        self.flight_number = flight_number

    def __repr__(self):
        return (
            f"Booking({self.booking_id}, "
            f"{self.passenger_name}, {self.flight_number})"
        )


class BookingManager:
    def __init__(self):
        self.active_bookings = {}
        self.cancelled_stack = []

    def add_booking(self, booking: Booking) -> None:
        """Add a new booking."""
        # TODO: Store the booking using its ID.
        pass

    def cancel_booking(self, booking_id: str) -> bool:
        """Cancel a booking and push it onto the cancellation stack."""
        # TODO: Remove it from active bookings and push it onto the stack.
        pass

    def undo_last_cancellation(self):
        """Restore the most recently cancelled booking."""
        # TODO: Pop the latest cancellation and restore it.
        pass


if __name__ == "__main__":
    manager = BookingManager()

    manager.add_booking(Booking("B101", "Ishaan", "UK-911"))
    manager.add_booking(Booking("B102", "Diya", "AI-404"))

    manager.cancel_booking("B101")
    restored = manager.undo_last_cancellation()

    print("Restored:", restored)
    print("Active bookings:", manager.active_bookings)
