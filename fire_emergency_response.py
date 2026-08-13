class Emergency:
    def __init__(self, location, emergency_level):
        self.location = location
        self.emergency_level = emergency_level

    def display_emergency(self):
        print("Location:", self.location)
        print("Emergency Level:", self.emergency_level)


class FireEmergency(Emergency):
    def __init__(self, location, emergency_level, engines_required):
        super().__init__(location, emergency_level)
        self.engines_required = engines_required

    def display_details(self):
        self.display_emergency()
        print("Fire Engines Required:", self.engines_required)

    def respond(self):
        print(
            "\nDispatching",
            self.engines_required,
            "fire engine(s) to",
            self.location
        )


emergency1 = FireEmergency("City Mall", "High", 3)

print("FIRE EMERGENCY DETAILS")
emergency1.display_details()

emergency1.respond()
