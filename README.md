## 📝 Todo App (CLI)

Oddiy, ammo foydali **Todo CLI dasturi** — u sizga vazifalarni (`todo`) qo‘shish, ko‘rish, tahrirlash va o‘chirish imkonini beradi.
Barcha ma’lumotlar **`JSON` faylda** saqlanadi.

---

## 📁 Loyihaning tuzilishi

```text
todo-app/
    ├── src/
    │   ├── __init__.py
    │   ├── main.py          # Asosiy CLI logika (menu va amallar)
    │   ├── storage.py       # JSON bilan ishlash (saqlash, o‘qish)
    │   ├── commands.py      # CRUD amallari (add, list, update, delete)
    ├── run.py               # Dastur ishga tushirish fayli
```

---

## 💾 Ma’lumotlar tuzilmasi (`database.json`)

Barcha todo ma’lumotlar **JSON** formatda saqlanadi:

```json
[
    {
        "id": 1,
        "name": "kitob oqish",
        "description": "nfdisnffjhdfibsdifbsdibf",
        "date": "2025-10-11",
        "category": "work",
        "completed": false
    }
]
```

---

## ⚙️ O‘rnatish

1. Reponi klon qiling yoki fayllarni yuklab oling:

   ```bash
   git clone https://github.com/username/todo-app.git
   cd todo-app
   ```

2. Dastur ishga tushiring:

   ```bash
   python run.py
   ```

---

## 🧠 Asosiy buyruqlar

| Amal       | Tavsif                            |
| ---------- | --------------------------------- |
| `add`      | Yangi vazifa qo‘shish             |
| `list`     | Barcha vazifalarni ko‘rish        |
| `update`   | Mavjud vazifani o‘zgartirish      |
| `delete`   | Vazifani o‘chirish                |
| `complete` | Vazifani bajarilgan deb belgilash |

---

## 🧩 Modullar haqida

### `storage.py`

* Faylga yozish va o‘qish funksiyalari mavjud.
* JSON faylni avtomatik yaratadi agar mavjud bo‘lmasa.

### `commands.py`

* CRUD funksiyalari (`add_task`, `get_tasks`, `update_task`, `delete_task`).
* Har bir vazifa unikal `id` ga ega.

### `main.py`

* CLI menyu.
* Foydalanuvchi buyruqlarini o‘qib, tegishli funksiyalarni chaqiradi.

---

## 🧑‍💻 Ishga tushirish namunasi

```bash
$ python run.py
--- TODO CLI ---
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Completed
6. Exit
Select option: 1

Task name: Kitob o‘qish
Description: Python haqida kitob
Category: Study
Date: 2025-10-11
✅ Vazifa muvaffaqiyatli qo‘shildi!
```

---

## 📚 Kelajakdagi rejalashtirilgan funksiyalar

* 🔍 Qidiruv (`search by category/date`)
* 📅 Filtrlash
* 🌐 JSON o‘rniga SQLite versiya

---
