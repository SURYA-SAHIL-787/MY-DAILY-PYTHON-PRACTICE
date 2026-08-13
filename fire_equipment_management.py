class Equipment:
    def __init__(self, equipment_id, name, quantity, condition):
        self.equipment_id = equipment_id
        self.name = name
        self.quantity = quantity
        self.condition = condition

    def display_details(self):
        print("Equipment ID:", self.equipment_id)
        print("Equipment Name:", self.name)
        print("Quantity:", self.quantity)
        print("Condition:", self.condition)

    def update_condition(self, new_condition):
        self.condition = new_condition
        print("\nEquipment condition updated successfully.")


equipment1 = Equipment("EQ101", "Fire Hose", 8, "Good")

print("EQUIPMENT DETAILS")
equipment1.display_details()

equipment1.update_condition("Excellent")

print("\nUPDATED EQUIPMENT DETAILS")
equipment1.display_details()
