import sqlite3


# Создание соединения с базой данных и инициализация таблицы
def connect():
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, salary REAL)")
    conn.commit()
    conn.close()


# Добавление нового сотрудника
def insert(name, phone, email, salary):
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO employees (name, phone, email, salary) VALUES (?, ?, ?, ?)", (name, phone, email, salary))
    conn.commit()
    conn.close()


# Просмотр всех сотрудников
def view():
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    conn.close()
    return rows


# Поиск сотрудника по ФИО
def search(name=""):
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE name=?", (name,))
    rows = cur.fetchall()
    conn.close()
    return rows


# Обновление данных сотрудника
def update(id, name, phone, email, salary):
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()
    cur.execute("UPDATE employees SET name=?, phone=?, email=?, salary=? WHERE id=?", (name, phone, email, salary, id))
    conn.commit()
    conn.close()


# Удаление сотрудника
def delete(id):
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id=?", (id,))
    conn.commit()
    conn.close()


connect()
