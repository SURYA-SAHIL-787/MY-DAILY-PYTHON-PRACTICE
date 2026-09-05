import heapq


class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __repr__(self):
        return f"{self.name} (Priority {self.priority})"


def add_task(task_queue, task):
    if task.priority < 1 or task.priority > 5:
        raise ValueError("Priority must be between 1 and 5.")

    heapq.heappush(task_queue, (task.priority, task.name))


def ai_automation(task_queue):
    print("\nAI Task Execution:")

    while task_queue:
        priority, task = heapq.heappop(task_queue)
        print("Executing:", task, "| Priority:", priority)


tasks = [
    Task("Send report", 3),
    Task("Fix server error", 1),
    Task("Reply to emails", 4),
    Task("Backup database", 2)
]

task_queue = []

try:
    for task in tasks:
        add_task(task_queue, task)

    ai_automation(task_queue)

except ValueError as e:
    print("Error:", e)
