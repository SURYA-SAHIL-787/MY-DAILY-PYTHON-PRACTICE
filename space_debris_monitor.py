class SpaceDebris:
    def __init__(self, debris_id, size_cm, distance_km):
        self.debris_id = debris_id
        self.size_cm = size_cm
        self.distance_km = distance_km

    def calculate_risk(self):
        if self.distance_km <= 0:
            return float("inf")

        return self.size_cm / self.distance_km


class Satellite:
    def __init__(self, satellite_name):
        self.satellite_name = satellite_name
        self.detected_debris = []

    def add_debris(self, debris):
        self.detected_debris.append(debris)

    def most_dangerous_debris(self):
        if not self.detected_debris:
            return None

        return max(
            self.detected_debris,
            key=lambda debris: debris.calculate_risk()
        )

    def display_report(self):
        print(f"Satellite: {self.satellite_name}")

        for debris in self.detected_debris:
            print(
                f"{debris.debris_id} - "
                f"Risk: {debris.calculate_risk():.3f}"
            )

        dangerous = self.most_dangerous_debris()

        if dangerous:
            print(
                f"Highest risk object: "
                f"{dangerous.debris_id}"
            )


satellite = Satellite("Orbital-Eye-7")

satellite.add_debris(SpaceDebris("DB-101", 15, 50))
satellite.add_debris(SpaceDebris("DB-102", 40, 80))
satellite.add_debris(SpaceDebris("DB-103", 8, 10))

satellite.display_report()
