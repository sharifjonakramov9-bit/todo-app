import sys

from .commands import (
    add_task,
    show_tasks,
    update_file,
    delete_tasks,
    mark_completed
)


def main():
    while True:
        print("---menu----")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Completed")
        print("6. Exit")
        
        choice = input("Select option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            update_file()
        elif choice == "4":
            delete_tasks()
        elif choice == "5":
            mark_completed()
        elif choice == "6":
            x = input("Do you want to exit?(Yes/No) ").strip().lower()
            if x == "yes":
                sys.exit()
            elif x == "no":
                continue
            else:
                print("You can answer only yes or no! please choose 1-6 around number")

            