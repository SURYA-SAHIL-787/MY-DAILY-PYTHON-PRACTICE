class Delivery:
    def __init__(self, distance, traffic):
        self.distance = distance
        self.traffic = traffic
        self.preparation_time = 15

    def calculate_speed(self):
        if self.traffic == "low":
            return 35
        elif self.traffic == "medium":
            return 25
        else:
            return 15

    def calculate_eta(self):
        speed = self.calculate_speed()

        travel_time = (self.distance / speed) * 60

        total_time = self.preparation_time + travel_time

        return round(total_time)


distance = float(input("Enter delivery distance in km: "))
traffic = input("Enter traffic (low/medium/high): ").lower()

order = Delivery(distance, traffic)

print("Estimated Delivery Time:", order.calculate_eta(), "minutes")
