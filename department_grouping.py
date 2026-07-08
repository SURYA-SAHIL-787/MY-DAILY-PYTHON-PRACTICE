# Program to group students by department

students = (
    ("Sahil", "CSE"),
    ("Ravi", "ECE"),
    ("Anil", "CSE"),
    ("Kiran", "EEE"),
    ("Manoj", "ECE"),
    ("Deepak", "CSE")
)

department_data = {}

for name, department in students:
    if department in department_data:
        department_data[department].append(name)
    else:
        department_data[department] = [name]

print("Students Grouped by Department:")

for department, names in department_data.items():
    print(department, ":", tuple(names))
