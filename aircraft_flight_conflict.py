from dataclasses import dataclass
from datetime import datetime


@dataclass
class Flight:
    flight_id: str
    aircraft_id: str
    start: datetime
    end: datetime


def flights_clash(first: Flight, second: Flight) -> bool:
    """Return True if the same aircraft has overlapping flights."""
    if first.aircraft_id != second.aircraft_id:
        return False

    return first.start < second.end and second.start < first.end


def find_conflicts(flights: list[Flight]) -> list[tuple[str, str]]:
    """Return pairs of flight IDs that use the same aircraft at overlapping times."""
    conflicts = []

    flights_by_aircraft = {}
    for flight in flights:
        flights_by_aircraft.setdefault(flight.aircraft_id, []).append(flight)

    for aircraft_flights in flights_by_aircraft.values():
        aircraft_flights.sort(key=lambda flight: flight.start)

        for i, first in enumerate(aircraft_flights):
            for second in aircraft_flights[i + 1:]:
                if second.start >= first.end:
                    break
                if flights_clash(first, second):
                    conflicts.append((first.flight_id, second.flight_id))

    return conflicts


flights = [
    Flight("AF101", "JET-7", datetime(2026, 5, 1, 9), datetime(2026, 5, 1, 11)),
    Flight("AF202", "JET-7", datetime(2026, 5, 1, 10, 30), datetime(2026, 5, 1, 12)),
    Flight("AF303", "JET-8", datetime(2026, 5, 1, 10), datetime(2026, 5, 1, 12)),
]

print(find_conflicts(flights))  # [('AF101', 'AF202')]
