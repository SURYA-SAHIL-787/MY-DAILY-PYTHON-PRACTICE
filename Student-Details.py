class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"
students = []
def add_student():
    roll = input("Roll: ")
    name = input("Name: ")
    marks = float(input("Marks: "))
    students.append(Student(roll, name, marks))
    print("Student added.\n")
def display_students():
    if not students:
        print("No records.\n")
        return
    for s in students:
        print(s.roll, s.name, s.marks, s.grade())
    print()
while True:
    print("1.Add 2.Display 3.Exit")
    choice = input("Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        break
    else:
        print("Invalid\n")
print("Program Ended")
