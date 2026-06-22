# student_result_analyzer.py

students = {
    "Surya": {"Math": 92, "Python": 88, "DBMS": 79},
    "Rahul": {"Math": 85, "Python": 91, "DBMS": 83},
    "Anjali": {"Math": 95, "Python": 89, "DBMS": 90},
    "Meena": {"Math": 78, "Python": 84, "DBMS": 88}
}

result = {}

for student, subjects in students.items():
    total = sum(subjects.values())
    average = total / len(subjects)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "D"

    result[student] = {
        "Total": total,
        "Average": round(average, 2),
        "Grade": grade
    }

topper = max(result, key=lambda name: result[name]["Total"])

subject_toppers = {}

for subject in next(iter(students.values())).keys():
    highest_student = max(students, key=lambda name: students[name][subject])
    subject_toppers[subject] = {
        "Student": highest_student,
        "Marks": students[highest_student][subject]
    }

print("Student Result Analysis")
print("-" * 40)

for student, details in result.items():
    print(student, details)

print("\nOverall Topper:")
print(topper, result[topper])

print("\nSubject-wise Toppers:")
for subject, details in subject_toppers.items():
    print(subject, details)
