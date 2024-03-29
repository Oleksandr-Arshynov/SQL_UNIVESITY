import sqlite3
from faker import Faker
import random
from datetime import datetime

fake = Faker()

# Підключаємо базу даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створюємо таблицю студентів
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER
                )''')

# Створюємо таблицю групи
cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

# Створюємо таблицю викладачів
cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

# Створюємо таблицю предметів
cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER
                )''')

# Створюємо таблицю оцінок
cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date TIMESTAMP
                )''')

# Створення груп
for _ in range(3):
    group_name = fake.company()
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))

# Створення викладачів
for _ in range(random.randint(5, 5)):
    teacher_name = fake.name()
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (teacher_name,))

# Створення предметів
for _ in range(random.randint(3, 8)):
    subject_name = fake.word()
    teacher_id = random.randint(1, 5)
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject_name, teacher_id))

# Створення студентів
for _ in range(random.randint(30, 50)):
    student_name = fake.name()
    group_id = random.randint(1, 3)
    cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (student_name, group_id))
    student_id = cursor.lastrowid
    
# Додавання оцінок для студентів
subjects = cursor.execute("SELECT id FROM subjects").fetchall()
students = cursor.execute("SELECT id FROM students").fetchall()
# Додавання оцінок для кожного студента та предмета
for student_id_tuple in students:
    student_id = student_id_tuple[0]
    for subject_id_tuple in subjects:
        subject_id = subject_id_tuple[0]
        # Генерація випадкової кількості оцінок для кожного предмету
        for _ in range(random.randint(0, 2)):
            grade = random.randint(1, 100)
            # Генерація випадкової дати
            date = fake.date_time_between(start_date="-2y", end_date="now")
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                           (student_id, subject_id, grade, date))
     

conn.commit()
conn.close()
