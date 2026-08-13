class Vehicle:
    def __init__(self, vehicle_no, driver_name):
        self.vehicle_no = vehicle_no
        self.driver_name = driver_name

    def display_details(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Driver Name:", self.driver_name)


class RescueVehicle(Vehicle):
    def __init__(self, vehicle_no, driver_name, rescue_capacity):
        super().__init__(vehicle_no, driver_name)
        self.rescue_capacity = rescue_capacity

    def display_details(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Driver Name:", self.driver_name)
        print("Rescue Capacity:", self.rescue_capacity, "people")

    def deploy(self, location):
        print("\nRescue vehicle", self.vehicle_no,
              "has been deployed to", location)


vehicle1 = RescueVehicle("RV202", "Kiran", 10)

print("RESCUE VEHICLE DETAILS")
vehicle1.display_details()

vehicle1.deploy("Central Market")
