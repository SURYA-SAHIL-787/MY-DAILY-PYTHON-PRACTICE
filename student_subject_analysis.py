# Question Name: Analyze Student Subjects Using Set, Dictionary, and Tuple
# Concept: Sets + Dictionaries + Tuples

# Dictionary:
# key = student name
# value = tuple of subjects

students = {
    "Arun": ("Math", "Physics", "English"),
    "Bala": ("Math", "Chemistry", "Biology"),
    "Charan": ("Physics", "English", "Computer"),
    "Divya": ("Math", "Computer", "English")
}

all_subjects = set()

for subjects in students.values():
    all_subjects.update(subjects)

print("Students and their subjects:")
for name, subjects in students.items():
    print(name, ":", subjects)

print("\nAll unique subjects:")
print(all_subjects)

print("\nNumber of unique subjects:", len(all_subjects))

search_subject = input("\nEnter subject to search: ")

print("\nStudents who study", search_subject, ":")
found = False

for name, subjects in students.items():
    if search_subject in subjects:
        print(name)
        found = True

if not found:
    print("No student found")
