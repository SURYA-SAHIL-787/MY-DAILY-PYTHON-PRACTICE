from collections import deque


class ClassSession:
    def __init__(self, subject, faculty):
        self.subject = subject
        self.faculty = faculty


class ClassQueue:
    def __init__(self):
        self.queue = deque()

    def add_class(self, session):
        self.queue.append(session)

        print(
            f"{session.subject} added to schedule."
        )

    def conduct_class(self):
        if not self.queue:
            print("No classes remaining.")
            return

        session = self.queue.popleft()

        print(
            f"Conducting {session.subject} "
            f"by {session.faculty}"
        )

    def display_classes(self):
        print("\nUpcoming Classes:")

        if not self.queue:
            print("No classes scheduled.")
            return

        for session in self.queue:
            print(
                session.subject,
                "-",
                session.faculty
            )


schedule = ClassQueue()

schedule.add_class(
    ClassSession("Python Programming", "Dr. Ravi")
)

schedule.add_class(
    ClassSession("DBMS", "Prof. Meena")
)

schedule.add_class(
    ClassSession("Operating Systems", "Dr. Kumar")
)

schedule.display_classes()

print("\nFirst Class:")
schedule.conduct_class()

schedule.display_classes()
