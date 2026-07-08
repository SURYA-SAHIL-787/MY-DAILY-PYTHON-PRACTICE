# Program to analyze employee salary details using dictionary and tuples

employees = {
    101: ("Sahil", "Developer", 45000),
    102: ("Ravi", "Tester", 35000),
    103: ("Anil", "Developer", 55000),
    104: ("Kiran", "Manager", 70000),
    105: ("Manoj", "Tester", 40000)
}

role_salary = {}

for emp_id, details in employees.items():
    name, role, salary = details

    if role in role_salary:
        role_salary[role].append(salary)
    else:
        role_salary[role] = [salary]

print("Employee Details:")
for emp_id, details in employees.items():
    print(emp_id, ":", details)

print("\nAverage Salary by Role:")

for role, salaries in role_salary.items():
    average_salary = sum(salaries) / len(salaries)
    print(role, ":", average_salary)
