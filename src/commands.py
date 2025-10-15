from datetime import datetime

from rich.console import Console
from rich.table import Table

from .storage import (
    create_task,
    get_tasks,
)


def add_task():
    name = input("Task name: ").strip().capitalize()
    description = input("Description: ").strip().capitalize()
    category = input("Category: ").strip().title()
    due_date = input("Date (example: 2025-10-11): ")

    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    if due_date < datetime.now():
        print("Date shoulde be greater than or equal to now.")
        return

    create_task(name, description, category, due_date)
    print("Vazifa muvaffaqiyatli qo'shildi!")


def show_tasks():
    tasks = get_tasks()

    console = Console()

    table = Table(title="All Tasks")
    table.add_column("Number")
    table.add_column("Name")
    table.add_column("Category")
    table.add_column("Due Date")

    for num, task in enumerate(tasks, start=1):
        du_date = task["due_date"].strftime("%d/%m/%Y")
        table.add_row(str(num), task["name"], task["category"], du_date)
    
    console.print(table)

    num_str = input("Task detail: ")

    if not num_str.isdigit():
        print("Faqat raqam kiriting!")
        return

    num = int(num_str)

    if num < 1 or num > len(tasks):
        print("Bunday raqamli task mavjud emas.")
        return

    task = tasks[num - 1]
    
    status = "Incompleted"
    if task["status"]:
        status = "Completed"
    du_date = task["due_date"].strftime("%d/%m/%Y")
    created_date = task["created_date"].strftime("%d/%m/%Y, %H:%M:%S")

    print(f"Task name: {task['name']}")
    print(f"Description: {task['description']}")
    print(f"Category: {task['category']}")
    print(f"Status: {status}")
    print(f"Due Date: {du_date}")
    print(f"Created Date: {created_date}")
    
    print()


def update_file():
    show_tasks()

    idk = int(input("Wich id will we change: "))
    for i in tasks:
        if int(i["id"]) == idk:
            new_name = input("New task name: ").strip().capitalize()
            new_description = input("New description: ").strip().capitalize()
            new_category = input("New category: ").strip().title()
            new_due_date = input("New date (example: 2025-10-11): ")

            new_due_date = datetime.strptime(new_due_date, "%Y-%m-%d")
            if new_due_date < datetime.now():
                print("Date shoulde be greater than or equal to now.")
                return

            if new_name != '':
                i["name"] == new_name
            if new_description != '':
                i["description"] != ''
            if new_category != '':
                i["category"] == new_category
            if new_due_date != '':
                i["due date"] == new_due_date

            save_database(tasks)
            return


def delete_tasks():
    show_tasks()

    idk = int(input("Which id will we delete: "))
    n = []
    op = False
    for i in tasks:
        if int(i["id"]) == idk:
            op = True
            print("Taak deleted")
        else:
            n.append(i)
        
    save_database(n)
    return

def mark_completed():
    show_tasks()

    idk = int(input("Which id will we mark complete: "))
    for i in tasks:
        if int(i["id"]) == idk:
            if i["status"] == False:
                i["status"] == True
                print("Satus changed!")
            else:
                i["status"] == False
            print("Status changed!")
    save_database(tasks)
    return

