class ScheduleManager:
    def __init__(self):
        self.classes = []

    def add_class(self, subject):
        self.classes.append(subject)

        print(
            subject,
            "added to timetable."
        )

    def remove_last_class(self):
        if not self.classes:
            print("No classes available.")
            return

        removed = self.classes.pop()

        print(
            "Removed:",
            removed
        )

    def display_schedule(self):
        print("\nCurrent CSE Schedule:")

        if not self.classes:
            print("Schedule is empty.")
            return

        for i, subject in enumerate(
            self.classes,
            start=1
        ):
            print(i, subject)


manager = ScheduleManager()

manager.add_class("Data Structures")
manager.add_class("DBMS")
manager.add_class("Operating Systems")
manager.add_class("Computer Networks")

manager.display_schedule()

print("\nRemoving last class...")
manager.remove_last_class()

manager.display_schedule()
