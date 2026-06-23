# Question Name: Store Employee Records Using Dictionary, Tuple, and Set
# Concept: Dictionaries + Tuples + Sets

# Dictionary:
# key = employee ID
# value = tuple containing name, department, salary

employees = {
    101: ("Ravi", "HR", 30000),
    102: ("Meena", "IT", 45000),
    103: ("Kumar", "Finance", 40000),
    104: ("Priya", "IT", 50000),
    105: ("Sita", "HR", 35000)
}

departments = set()

for emp in employees.values():
    departments.add(emp[1])

print("Employee Records:")
for emp_id, details in employees.items():
    print("ID:", emp_id)
    print("Name:", details[0])
    print("Department:", details[1])
    print("Salary:", details[2])
    print()

print("Unique Departments:")
print(departments)

search_dept = input("Enter department to display employees: ")

print("\nEmployees in", search_dept, "department:")
found = False

for emp_id, details in employees.items():
    if details[1].lower() == search_dept.lower():
        print(emp_id, "-", details[0])
        found = True

if not found:
    print("No employees found in this department")
