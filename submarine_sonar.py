class Sonar:
    def __init__(self, distances):
        self.distances = distances
        self.stack = []

    def scan(self, limit):
        for distance in self.distances:

            if distance < 0:
                raise ValueError("Distance cannot be negative.")

            if distance < limit:
                self.stack.append(distance)

        return self.stack


def find_danger_zones(distances, limit):
    danger_zones = []

    for distance in distances:
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        if distance < limit:
            danger_zones.append(distance)

    return danger_zones


# Main program
distances = [450, 120, 75, 300, 40, 900, 150]

sonar = Sonar(distances)

try:
    danger_zones = sonar.scan(100)

    print("Danger-zone distances:", danger_zones)

    if danger_zones:
        print("Closest obstacle:", min(danger_zones))
    else:
        print("No danger zones detected.")

except ValueError as e:
    print("Error:", e)
