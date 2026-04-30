import json
import os

TASKFILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKFILE):
        return []
    try:
        with open(TASKFILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks):
    with open(TASKFILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_tasks(tasks):
    title = input("Enter the task title: ")
    category = input("Enter the category of task: ")
    tasks.append({
        "title": title,
        "category": category,
        "done": False
    })
    save_tasks(tasks)
    print("Task added")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return

    for i, t in enumerate(tasks, start=1):
        status = "done" if t['done'] else "not_done"
        title = t.get("title", "no title")
        category = t.get("category", "no category")
        print(f"{i}. [{status}] {title} - {category}")

def list_by_category(tasks):
    category = input("Enter the category to filter: ")
    filtered = [
        t for t in tasks
        if t.get("category", "").lower() == category.lower()
    ]

    if not filtered:
        print("No tasks found in this category")
        return

    list_tasks(filtered)

def mark_done(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        tasks[index]['done'] = True
        save_tasks(tasks)
        print("Task marked as done")
    except (IndexError, ValueError):
        print("Enter a valid index")

def delete_tasks(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task removed: {removed['title']}")
    except (IndexError, ValueError):
        print("Enter a valid index")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager\n")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. List by Category")
        print("5. Mark Done")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_tasks(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            delete_tasks(tasks)
        elif choice == '4':
            list_by_category(tasks)
        elif choice == '5':
            mark_done(tasks)
        elif choice == '6':
            print("Thank you!")
            break
        else:
            print("Enter a valid choice")

if __name__ == "__main__":
    main()