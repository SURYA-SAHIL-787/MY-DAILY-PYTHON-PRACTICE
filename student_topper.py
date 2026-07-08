# Program to store marks using tuple keys and find the topper

students = {
    ("Sahil", "CSE"): (85, 90, 88),
    ("Ravi", "ECE"): (78, 82, 80),
    ("Anil", "CSE"): (92, 89, 95),
    ("Kiran", "EEE"): (70, 75, 72)
}

topper = None
highest_average = 0

for student, marks in students.items():
    average = sum(marks) / len(marks)

    if average > highest_average:
        highest_average = average
        topper = student

print("Student Marks:")
print(students)

print("\nTopper Details:")
print("Name:", topper[0])
print("Branch:", topper[1])
print("Average Marks:", highest_average)
