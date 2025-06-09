import os
from task_manager.base import Task, task_generator
from task_manager.utils import deco

TASK_FILE = "tasks.txt"

@deco("cyan")

def add_task():
    desc = input("Enter task description: ")
    priority = input("Enter priority (low/medium/high): ")
    status = input("Enter status (pending/done): ")

    with open(TASK_FILE, "a") as f:
        f.write(f"{desc}|{priority}|{status}\n")
    print("\033[92mTask added!\033[0m")

def view_tasks():
    if not os.path.exists(TASK_FILE):
        print("\033[91mNo task file found.\033[0m")
        return

    print("\nYour Tasks:")
    for task in task_generator(TASK_FILE):
        color = {
            "high": "red",
            "medium": "yellow",
            "low": "green"
        }.get(task.priority.lower(), "cyan")

        @deco(color)
        def output():
            return str(task)

        print(output())

def update_task_status():
    tasks = list(task_generator(TASK_FILE))
    if not tasks:
        print("No tasks to update.")
        return

    print("\nTasks:")
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task}")

    try:
        selection = int(input("Enter the task number to update: ")) - 1
        if selection < 0 or selection >= len(tasks):
            print("Invalid task number.")
            return

        new_status = input("Enter new status (pending/done): ").strip().lower()
        if new_status not in ['pending', 'done']:
            print("Invalid status.")
            return

        tasks[selection].status = new_status

        with open(TASK_FILE, "w") as file:
            for t in tasks:
                file.write(f"{t._description}|{t.priority}|{t.status}\n")

        print("Status updated.")
    except ValueError:
        print("Invalid input.")

def delete_task():
    tasks = list(task_generator(TASK_FILE))
    if not tasks:
        print("No tasks to delete.")
        return

    print("\nTasks:")
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task}")

    try:
        selection = int(input("Enter the task number to delete: ")) - 1
        if selection < 0 or selection >= len(tasks):
            print("Invalid task number.")
            return

        removed = tasks.pop(selection)

        with open(TASK_FILE, "w") as file:
            for t in tasks:
                file.write(f"{t._description}|{t.priority}|{t.status}\n")

        print(f"Deleted task: {removed}")
    except ValueError:
        print("Invalid input.")

def merge_files():
    filepath = input("Enter the path of another task file to merge: ")
    if not os.path.exists(filepath):
        print("\033[91mFile not found.\033[0m")
        return

    with open(filepath, "r") as other, open(TASK_FILE, "a") as current:
        current.writelines(other.readlines())

    print("\033[95mFiles merged successfully!\033[0m")

def main():
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Merge Another Task File")
        print("6. Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task_status()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            merge_files()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
