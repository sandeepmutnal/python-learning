import json
import os

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as file:
            json.dump([], file)
        return []

    with open(TASKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Your Tasks ---")
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        priority = task.get("priority", "Medium")
        print(f"{idx}. [{status}] ({priority}) {task['title']}")
    print("------------------\n")


def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty!")
        return

    priority = input("Priority (Low/Medium/High): ").capitalize()
    if priority not in ["Low", "Medium", "High"]:
        priority = "Medium"

    tasks.append({
        "title": title,
        "done": False,
        "priority": priority
    })

    save_tasks(tasks)
    print("Task added successfully!")


def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def edit_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to edit: "))
        if 1 <= task_num <= len(tasks):
            new_title = input("Enter new title: ").strip()
            if new_title:
                tasks[task_num - 1]["title"] = new_title
                save_tasks(tasks)
                print("Task updated!")
            else:
                print("Title cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")


def clear_completed(tasks):
    tasks[:] = [task for task in tasks if not task["done"]]
    save_tasks(tasks)
    print("Completed tasks cleared!")


def main():
    while True:
        tasks = load_tasks()

        print("\n--- To-Do App ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Clear Completed Tasks")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            clear_completed(tasks)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
