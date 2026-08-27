class LapTracker:
    def __init__(self, driver):
        self.driver = driver
        self.laps = []

    def add_lap(self, lap_time):
        self.laps.append(lap_time)
        print(f"Lap time {lap_time}s added.")

    def remove_last_lap(self):
        if not self.laps:
            print("No lap times available.")
            return

        removed = self.laps.pop()
        print(f"Removed last lap: {removed}s")

    def display_laps(self):
        print(f"\nLap Times for {self.driver}")

        for lap_number, time in enumerate(self.laps, start=1):
            print(f"Lap {lap_number}: {time}s")


tracker = LapTracker("Lando Norris")

tracker.add_lap(91.5)
tracker.add_lap(90.8)
tracker.add_lap(90.2)
tracker.add_lap(89.9)

tracker.display_laps()

print("\nRemoving latest lap:")
tracker.remove_last_lap()

tracker.display_laps()
