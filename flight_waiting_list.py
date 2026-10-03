from collections import deque


class Flight:
    def __init__(self, flight_number: str, total_seats: int):
        self.flight_number = flight_number
        self.available_seats = deque(range(1, total_seats + 1))
        self.bookings = {}
        self.waiting_list = deque()

    def request_booking(self, passenger_name: str) -> None:
        """Book a seat or add the passenger to the waiting list."""
        # TODO: Assign a seat when available.
        # Otherwise, add the passenger to the waiting list.
        pass

    def cancel_booking(self, passenger_name: str) -> None:
        """Cancel a booking and serve the next waiting passenger."""
        # TODO: Find and release the passenger's seat.
        # Assign it to the first waiting passenger, if one exists.
        pass

    def show_status(self) -> None:
        print("Confirmed bookings:", self.bookings)
        print("Waiting list:", list(self.waiting_list))


if __name__ == "__main__":
    flight = Flight("6E-501", 2)

    flight.request_booking("Riya")
    flight.request_booking("Kabir")
    flight.request_booking("Anaya")
    flight.cancel_booking("Riya")
    flight.show_status()
