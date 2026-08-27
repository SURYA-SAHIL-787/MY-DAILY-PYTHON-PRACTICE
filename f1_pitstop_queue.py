from collections import deque


class Car:
    def __init__(self, driver, team):
        self.driver = driver
        self.team = team


class PitStopQueue:
    def __init__(self):
        self.queue = deque()

    def enter_pit(self, car):
        self.queue.append(car)
        print(f"{car.driver} entered the pit lane.")

    def service_car(self):
        if not self.queue:
            print("No cars waiting.")
            return

        car = self.queue.popleft()
        print(f"Pit stop completed for {car.driver} - {car.team}")

    def display_queue(self):
        print("\nCars waiting for pit stop:")

        if not self.queue:
            print("No cars waiting.")
            return

        for car in self.queue:
            print(car.driver, "-", car.team)


pit_queue = PitStopQueue()

pit_queue.enter_pit(Car("Lewis Hamilton", "Ferrari"))
pit_queue.enter_pit(Car("Oscar Piastri", "McLaren"))
pit_queue.enter_pit(Car("Fernando Alonso", "Aston Martin"))

pit_queue.display_queue()

print("\nProcessing pit stop:")
pit_queue.service_car()

pit_queue.display_queue()
