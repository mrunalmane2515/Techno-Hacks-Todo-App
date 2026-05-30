tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour To-Do Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Task removed: {removed}")
    else:
        print("Invalid task number!")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)

    elif choice == '2':
        view_tasks()

    elif choice == '3':
        view_tasks()
        num = int(input("Enter task number to remove: "))
        remove_task(num)

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
