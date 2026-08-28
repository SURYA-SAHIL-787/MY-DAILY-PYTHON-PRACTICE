import heapq


class ClassSession:
    def __init__(self, subject, faculty, priority):
        self.subject = subject
        self.faculty = faculty
        self.priority = priority


class TimeTableScheduler:
    def __init__(self):
        self.schedule = []
        self.count = 0

    def add_class(self, session):
        self.count += 1

        heapq.heappush(
            self.schedule,
            (
                session.priority,
                self.count,
                session
            )
        )

        print(
            session.subject,
            "added with priority",
            session.priority
        )

    def get_next_class(self):
        if not self.schedule:
            print("No classes scheduled.")
            return

        priority, _, session = heapq.heappop(
            self.schedule
        )

        print(
            f"Next Class: {session.subject}"
        )
        print(
            f"Faculty: {session.faculty}"
        )
        print(
            f"Priority: {priority}"
        )


scheduler = TimeTableScheduler()

scheduler.add_class(
    ClassSession(
        "DBMS",
        "Dr. Priya",
        2
    )
)

scheduler.add_class(
    ClassSession(
        "Data Structures",
        "Dr. Ravi",
        1
    )
)

scheduler.add_class(
    ClassSession(
        "Operating Systems",
        "Prof. Kumar",
        3
    )
)

print("\nClass Order:")

scheduler.get_next_class()
scheduler.get_next_class()
scheduler.get_next_class()
