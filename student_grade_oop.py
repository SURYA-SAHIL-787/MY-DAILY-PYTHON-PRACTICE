class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def find_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 40:
            return "D"
        else:
            return "Fail"

    def display_details(self):
        print("Student:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Average:", round(self.calculate_average(), 2))
        print("Grade:", self.find_grade())


student = Student(
    "Sahil",
    {
        "Python": 85,
        "Maths": 78,
        "English": 92
    }
)

student.display_details()
