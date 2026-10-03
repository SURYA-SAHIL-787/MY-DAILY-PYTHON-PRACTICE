import heapq


class FlightNetwork:
    def __init__(self):
        self.routes = {}

    def add_flight(self, source: str, destination: str, price: int) -> None:
        """Add a directed flight route."""
        self.routes.setdefault(source, []).append((destination, price))
        self.routes.setdefault(destination, [])

    def find_cheapest_route(self, start: str, destination: str):
        """
        Return (minimum_price, route).

        Example:
            (7500, ["Delhi", "Mumbai", "Goa"])
        """
        # Each heap item: (total_price, current_city, route_taken)
        priority_queue = [(0, start, [start])]
        minimum_cost = {start: 0}

        while priority_queue:
            current_price, city, path = heapq.heappop(priority_queue)

            # TODO:
            # 1. Return when the destination is reached.
            # 2. Explore neighbouring cities.
            # 3. Update the cost when a cheaper route is found.
            pass

        return None


if __name__ == "__main__":
    network = FlightNetwork()

    network.add_flight("Delhi", "Mumbai", 5000)
    network.add_flight("Delhi", "Jaipur", 2000)
    network.add_flight("Jaipur", "Mumbai", 2500)
    network.add_flight("Mumbai", "Goa", 3000)
    network.add_flight("Jaipur", "Goa", 6000)

    print(network.find_cheapest_route("Delhi", "Goa"))
