from collections import deque


class RailwayNetwork:
    def __init__(self):
        self.connections = {}

    def add_connection(self, station_a, station_b):
        self.connections.setdefault(station_a, []).append(station_b)
        self.connections.setdefault(station_b, []).append(station_a)

    def find_route(self, start, destination):
        if start not in self.connections or destination not in self.connections:
            return None

        queue = deque([(start, [start])])
        visited = {start}

        while queue:
            station, route = queue.popleft()

            if station == destination:
                return route

            for neighbor in self.connections[station]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, route + [neighbor]))

        return None


network = RailwayNetwork()
network.add_connection("Chennai", "Katpadi")
network.add_connection("Katpadi", "Bengaluru")
network.add_connection("Chennai", "Vellore")

print(network.find_route("Chennai", "Bengaluru"))
