class Employee:
    def __init__(self, emp_id, name, role):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def display(self, level=0):
        indent = "  " * level
        print(f"{indent}{self.name} ({self.role})")
        for employee in self.subordinates:
            employee.display(level + 1)

    def search_employee(self, emp_id):
        if self.emp_id == emp_id:
            return self

        for employee in self.subordinates:
            result = employee.search_employee(emp_id)
            if result:
                return result

        return None


def main():
    ceo = Employee(1, "Ananya", "CEO")
    manager1 = Employee(2, "Rahul", "Engineering Manager")
    manager2 = Employee(3, "Meera", "HR Manager")
    dev1 = Employee(4, "Kabir", "Python Developer")
    dev2 = Employee(5, "Isha", "ML Engineer")

    ceo.add_subordinate(manager1)
    ceo.add_subordinate(manager2)

    manager1.add_subordinate(dev1)
    manager1.add_subordinate(dev2)

    print("Company Hierarchy:")
    ceo.display()

    search_id = 5
    found = ceo.search_employee(search_id)

    if found:
        print(f"\nEmployee found: {found.name}, Role: {found.role}")
    else:
        print("\nEmployee not found.")


if __name__ == "__main__":
    main()
