class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_marks(self, mark):
        self.marks.append(mark)

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

    def show_result(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {self.average_marks():.2f}")


student = Student("Surya")

student.add_marks(85)
student.add_marks(90)
student.add_marks(78)

student.show_result()
