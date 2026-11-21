import heapq


class Train:
    def __init__(self, name, arrival, departure):
        self.name = name
        self.arrival = arrival
        self.departure = departure


class PlatformScheduler:
    def assign_platforms(self, trains):
        trains.sort(key=lambda train: train.arrival)

        # Stores (departure_time, platform_number) for occupied platforms.
        occupied = []

        # Stores platform numbers available for reuse.
        available = []

        assignments = {}
        next_platform = 1

        for train in trains:
            while occupied and occupied[0][0] <= train.arrival:
                _, platform_number = heapq.heappop(occupied)
                heapq.heappush(available, platform_number)

            if available:
                platform_number = heapq.heappop(available)
            else:
                platform_number = next_platform
                next_platform += 1

            assignments[train.name] = platform_number
            heapq.heappush(
                occupied,
                (train.departure, platform_number),
            )

        return next_platform - 1, assignments


trains = [
    Train("Express A", 900, 1030),
    Train("Express B", 915, 1000),
    Train("Express C", 1030, 1100),
]

count, assignments = PlatformScheduler().assign_platforms(trains)

print("Minimum platforms:", count)
print("Train assignments:", assignments)
