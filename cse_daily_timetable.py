class Subject:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty


class TimeTable:
    def __init__(self):
        self.schedule = []

    def add_class(self, time, subject):
        self.schedule.append((time, subject))

    def display_timetable(self):
        print("\nCSE Daily Time Table")
        print("----------------------------")

        for time, subject in self.schedule:
            print(
                f"{time} : {subject.name} "
                f"- {subject.faculty}"
            )


timetable = TimeTable()

timetable.add_class(
    "9:00 AM",
    Subject("Data Structures", "Dr. Rao")
)

timetable.add_class(
    "10:00 AM",
    Subject("Operating Systems", "Prof. Kumar")
)

timetable.add_class(
    "11:00 AM",
    Subject("DBMS", "Dr. Priya")
)

timetable.add_class(
    "1:00 PM",
    Subject("Computer Networks", "Prof. Arun")
)

timetable.display_timetable()
