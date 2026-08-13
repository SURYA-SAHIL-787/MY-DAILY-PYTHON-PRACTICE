class FireEngine:
    def __init__(self, engine_no, driver_name, water_capacity):
        self.engine_no = engine_no
        self.driver_name = driver_name
        self.water_capacity = water_capacity
        self.available = True

    def display_details(self):
        print("Engine Number:", self.engine_no)
        print("Driver Name:", self.driver_name)
        print("Water Capacity:", self.water_capacity, "litres")
        print("Status:", "Available" if self.available else "Dispatched")

    def dispatch(self):
        if self.available:
            self.available = False
            print("\nFire Engine", self.engine_no, "has been dispatched.")
        else:
            print("\nFire Engine is already on duty.")


engine1 = FireEngine("FE101", "Arjun", 5000)

print("FIRE ENGINE DETAILS")
engine1.display_details()

engine1.dispatch()

print("\nUPDATED DETAILS")
engine1.display_details()
