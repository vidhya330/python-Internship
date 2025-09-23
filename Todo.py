TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from the file into a list."""
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    """Save the tasks list into the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks found.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()


def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")


def remove_task(tasks):
    """Remove a task by number."""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"Task '{removed}' removed successfully!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")


def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please select 1-4.\n")


if __name__ == "__main__":
    main()
