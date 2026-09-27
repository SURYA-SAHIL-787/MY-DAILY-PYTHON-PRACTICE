class DeliveryFee:
    def __init__(self, distance, raining, peak_hour):
        self.distance = distance
        self.raining = raining
        self.peak_hour = peak_hour

        self.__base_charge = 20

    def calculate_fee(self):

        distance_charge = self.distance * 8

        rain_charge = 0
        peak_charge = 0

        if self.raining == "yes":
            rain_charge = 20

        if self.peak_hour == "yes":
            peak_charge = 15

        total = (
            self.__base_charge
            + distance_charge
            + rain_charge
            + peak_charge
        )

        return total


distance = float(input("Enter distance: "))

raining = input("Is it raining? (yes/no): ").lower()

peak = input("Is it peak hour? (yes/no): ").lower()

delivery = DeliveryFee(distance, raining, peak)

print("Delivery Fee: ₹", delivery.calculate_fee())
