# main.py
from task_agent import add_task, list_tasks

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        desc = input("Enter a task (e.g., 'Remind me to...'):\n> ")
        add_task(desc)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        break
    else:
        print("❌ Invalid choice. Try again.")
