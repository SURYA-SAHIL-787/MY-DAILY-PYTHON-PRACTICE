class DeliveryPartner:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance


class DeliverySystem:
    def __init__(self):
        self.partners = []

    def add_partner(self, partner):
        self.partners.append(partner)

    def find_nearest_partner(self):
        return min(
            self.partners,
            key=lambda partner: partner.distance
        )


system = DeliverySystem()

system.add_partner(DeliveryPartner("Rahul", 2.5))
system.add_partner(DeliveryPartner("Arjun", 1.2))
system.add_partner(DeliveryPartner("Kiran", 3.8))
system.add_partner(DeliveryPartner("Vijay", 0.9))

nearest = system.find_nearest_partner()

print("Assigned Partner:", nearest.name)
print("Distance:", nearest.distance, "km")
