from dataclasses import dataclass
from heapq import heappush, heapreplace


@dataclass(frozen=True)
class Booking:
    booking_id: str
    start: int
    end: int


class RoomScheduler:
    def schedule(self, bookings: list[Booking]) -> tuple[int, dict[str, int]]:
        rooms: list[tuple[int, int]] = []  # (end time, room number)
        assignments: dict[str, int] = {}

        for booking in sorted(bookings, key=lambda item: (item.start, item.booking_id)):
            if booking.end <= booking.start or booking.booking_id in assignments:
                raise ValueError("Bookings need unique IDs and a positive duration")

            if rooms and rooms[0][0] <= booking.start:
                _, room = rooms[0]
                heapreplace(rooms, (booking.end, room))
            else:
                room = len(rooms) + 1
                heappush(rooms, (booking.end, room))

            assignments[booking.booking_id] = room

        return len(rooms), assignments


if __name__ == "__main__":
    bookings = [Booking("A", 9, 11), Booking("B", 10, 12), Booking("C", 11, 13)]
    count, assignments = RoomScheduler().schedule(bookings)

    print(f"Rooms needed: {count}")
    for booking_id, room in assignments.items():
        print(f"{booking_id} -> room {room}")
