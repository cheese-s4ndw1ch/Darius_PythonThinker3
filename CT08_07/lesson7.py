# import os

# FILENAME = "tasks.txt"


# def display_menu():
#     print("\n===== TASK LIST MENU =====")
#     print("1. Create a new task file")
#     print("2. View all tasks")
#     print("3. Add a new task")
#     print("4. Delete a task")
#     print("5. Mark a task as done")
#     print("6. Exit")



# def create_file():
#     if os.path.exists(FILENAME):
#         choice = input("File already exists. Overwrite? (y/n): ").lower()
#         if choice != 'y':
#             print("File not overwritten.")
#             return
    
#     with open(FILENAME, "w") as file:
#         file.write("My Task List\n")
    
#     print("Task file created successfully!")


# def view_tasks():
#     if not os.path.exists(FILENAME):
#         print("No task file found. Please create one first.")
#         return
    
#     with open(FILENAME, "r") as file:
#         tasks = file.readlines()
    
#     print("\n===== TASK LIST =====")
#     for idx, task in enumerate(tasks[1:], start=1):  # Skip the header
#         print(f"{idx}. {task.strip()}")



import json
import os

FILENAME = "tasks.json"
PRIORITY_ORDER = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("\nMy Task List\n(no tasks)\n")
        return
    # sort by priority descending then by index
    sorted_tasks = sorted(tasks, key=lambda t: (-PRIORITY_ORDER[t["priority"]], t["id"]))
    print("\nMy Task List")
    for i, t in enumerate(sorted_tasks, 1):
        done = " (Done)" if t["done"] else ""
        print(f"{i}. {t['title']} [{t['priority']}]"+done)
    print()

def input_priority():
    while True:
        p = input("Enter priority (low/medium/high): ").strip().lower()
        if p in ("low","medium","high"):
            return p.upper()
        print("Invalid. Choose low, medium, or high.")

def create_file():
    if os.path.exists(FILENAME):
        print("Task file already exists.")
    else:
        save_tasks([])
        print("Created new task file.")

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Empty title, cancelled.")
        return
    priority = input_priority()
    next_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({"id": next_id, "title": title, "priority": priority, "done": False})
    save_tasks(tasks)
    print("Task added.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        n = int(input("Enter the task number to delete: ").strip())
    except:
        print("Invalid input.")
        return
    sorted_tasks = sorted(tasks, key=lambda t: (-PRIORITY_ORDER[t["priority"]], t["id"]))
    if 1 <= n <= len(sorted_tasks):
        task = sorted_tasks[n-1]
        tasks[:] = [t for t in tasks if t["id"] != task["id"]]
        save_tasks(tasks)
        print("Deleted.")
    else:
        print("No such task number.")

def toggle_done(tasks, mark_done=True):
    
    display_tasks(tasks)
    try:
        n = int(input("Enter the task number: ").strip())
    except:
        print("Invalid input.")
        return
    sorted_tasks = sorted(tasks, key=lambda t: (-PRIORITY_ORDER[t["priority"]], t["id"]))
    if 1 <= n <= len(sorted_tasks):
        task = sorted_tasks[n-1]
        task_record = next(t for t in tasks if t["id"] == task["id"])
        if mark_done:
            task_record["done"] = True
            print("Marked done.")
        else:
            
            print("Marked undone.")
        save_tasks(tasks)
    else:
        print("No such task number.")

def main():
    while True:
        print("""Menu:
1. Create a new task file
2. View all tasks
3. Add a new task
4. Delete a task
5. Mark a task as done
6. Toggle undo a done task (undo)
7. Exit
""")
        choice = input("Enter your choice: ").strip()
        tasks = load_tasks()
        if choice == "1":
            create_file()
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            add_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            toggle_done(tasks, mark_done=True)
        elif choice == "6":
            toggle_done(tasks, mark_done=False)
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
