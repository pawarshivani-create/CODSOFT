# to do list
my_tasks = []

def add_new_task():
    task = input("Enter your task: ")
    my_tasks.append(task)
    print("Task saved!")

def show_tasks():
    if not my_tasks:
        print("No tasks yet.")
    else:
        for i, t in enumerate(my_tasks, 1):
            print(i, "-", t)

def remove_task():
    show_tasks()
    num = int(input("Enter task number to delete: "))
    my_tasks.pop(num - 1)
    print("Task removed!")

while True:
    print("\n--- My Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    ch = input("Choose: ")

    if ch == "1":
        add_new_task()
    elif ch == "2":
        show_tasks()
    elif ch == "3":
        remove_task()
    elif ch == "4":
        break
    else:
        print("Invalid choice")
