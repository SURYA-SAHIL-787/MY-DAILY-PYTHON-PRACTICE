class Subject:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __str__(self):
        return f"{self.name} - {self.time}"


class TimeTable:
    def __init__(self):
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def binary_search(self, name):
        self.subjects.sort(
            key=lambda x: x.name.lower()
        )

        low = 0
        high = len(self.subjects) - 1

        while low <= high:
            mid = (low + high) // 2

            current = self.subjects[mid].name.lower()
            target = name.lower()

            if current == target:
                return self.subjects[mid]

            elif current < target:
                low = mid + 1

            else:
                high = mid - 1

        return None


timetable = TimeTable()

timetable.add_subject(
    Subject("DBMS", "10:00 AM")
)

timetable.add_subject(
    Subject("Data Structures", "9:00 AM")
)

timetable.add_subject(
    Subject("Operating Systems", "11:00 AM")
)

timetable.add_subject(
    Subject("Computer Networks", "1:00 PM")
)

search_subject = "Operating Systems"

result = timetable.binary_search(
    search_subject
)

if result:
    print("Subject Found:")
    print(result)
else:
    print("Subject not found.")
