class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return {
            "name": self.name,
            "salary": self.salary
        }


class Developer(Employee):
    def __init__(self, name, salary, programming_languages):
        super().__init__(name, salary)
        self.programming_languages = programming_languages

    def get_details(self):
        details = super().get_details()
        details["role"] = "Developer"
        details["languages"] = tuple(self.programming_languages)
        return details


class Manager(Employee):
    def __init__(self, name, salary, team_members):
        super().__init__(name, salary)
        self.team_members = team_members

    def get_details(self):
        details = super().get_details()
        details["role"] = "Manager"
        details["team_members"] = self.team_members
        return details


employees = [
    Developer("Arjun", 60000, ["Python", "Java"]),
    Developer("Neha", 65000, ["Python", "JavaScript"]),
    Manager("Meera", 80000, 5)
]

for employee in employees:
    print(employee.get_details())
