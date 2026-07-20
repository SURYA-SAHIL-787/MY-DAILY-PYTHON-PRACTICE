import heapq


class RunningMedian:
    def __init__(self):
        # Python has only a min-heap, so negative values
        # are stored to simulate a max-heap.
        self.lower_half = []
        self.upper_half = []

    def add_number(self, number):
        if not self.lower_half or number <= -self.lower_half[0]:
            heapq.heappush(self.lower_half, -number)
        else:
            heapq.heappush(self.upper_half, number)

        self._balance_heaps()

    def _balance_heaps(self):
        if len(self.lower_half) > len(self.upper_half) + 1:
            value = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, value)

        elif len(self.upper_half) > len(self.lower_half):
            value = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -value)

    def get_median(self):
        if not self.lower_half and not self.upper_half:
            raise ValueError("No numbers have been added.")

        if len(self.lower_half) == len(self.upper_half):
            lower_max = -self.lower_half[0]
            upper_min = self.upper_half[0]

            return (lower_max + upper_min) / 2

        return float(-self.lower_half[0])


def main():
    stream = [10, 20, 5, 15, 30, 25]
    median_tracker = RunningMedian()

    for number in stream:
        median_tracker.add_number(number)

        print(
            f"Added: {number:2} | "
            f"Current median: {median_tracker.get_median()}"
        )


if __name__ == "__main__":
    main()
