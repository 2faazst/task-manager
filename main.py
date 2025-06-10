import os
from task_manager.base import Task, task_generator
from task_manager.utils import deco

TASK_FILE = "tasks.txt"

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
    paths = input("Enter paths of task files to merge (comma-separated): ").split(',')

    valid_paths = [path.strip() for path in paths if os.path.exists(path.strip())]

    if not valid_paths:
        print("\033[91mNo valid files found to merge.\033[0m")
        return

    with open(TASK_FILE, "a") as current:
        for path in valid_paths:
            with open(path, "r") as file:
                for line in file:
                    current.write(line.rstrip('\n') + '\n')  # Ensures clean newlines

    print("\033[95mFiles merged successfully!\033[0m")



def main():
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Merge Another Task File")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            merge_files()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
