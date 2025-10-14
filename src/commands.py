from datetime import datetime
from .storage import create_task


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
    print("✅ Vazifa muvaffaqiyatli qo'shildi!")
