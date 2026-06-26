class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found")

    def show_tasks(self):
        print("\nYour Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")


todo = TodoList()

todo.add_task("Complete Python homework")
todo.add_task("Practice DSA")
todo.add_task("Read AI notes")

todo.show_tasks()

todo.remove_task("Practice DSA")

todo.show_tasks()
