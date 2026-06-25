import heapq


class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __repr__(self):
        return f"{self.name}({self.marks})"


class RankSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def top_k_students(self, k):
        return heapq.nlargest(k, self.students)

    def lowest_student(self):
        if not self.students:
            return None
        return min(self.students, key=lambda student: student.marks)


def main():
    rank_system = RankSystem()

    rank_system.add_student(Student(101, "Aarav", 89))
    rank_system.add_student(Student(102, "Diya", 95))
    rank_system.add_student(Student(103, "Vivaan", 76))
    rank_system.add_student(Student(104, "Tara", 92))
    rank_system.add_student(Student(105, "Kunal", 84))

    print("Top 3 Students:")
    for student in rank_system.top_k_students(3):
        print(student.name, "-", student.marks)

    lowest = rank_system.lowest_student()
    print("\nLowest Student:", lowest.name, "-", lowest.marks)


if __name__ == "__main__":
    main()
