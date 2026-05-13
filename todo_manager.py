import json
from pathlib import Path

FILE_NAME = "tasks.json"


def load_tasks():
    path = Path(FILE_NAME)

    if not path.exists():
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour Tasks:")

    for index, task in enumerate(tasks, start=1):
        status = "DONE" if task["done"] else "PENDING"
        print(f"{index}. [{status}] {task['title']}")


def add_task(tasks):
    title = input("\nEnter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append({
        "title": title,
        "done": False
    })

    save_tasks(tasks)
    print("Task added successfully.")


def mark_done(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to mark done: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done.")

    except ValueError:
        print("Enter a valid number.")


def delete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['title']}")

    except ValueError:
        print("Enter a valid number.")


def menu():
    tasks = load_tasks()

    while True:
        print("\n===== TODO MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting Todo Manager.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
