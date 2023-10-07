import tkinter as tk
from tkinter import ttk
import database  # Импортируем функции БД


def view_command():
    list1.delete(*list1.get_children())  # Очищаем содержимое Treeview
    for row in database.view():
        list1.insert("", "end", values=row)  # Вставляем записи из БД в Treeview


def search_command():
    list1.delete(*list1.get_children())  # Очищаем содержимое Treeview
    for row in database.search(e_name.get()):
        list1.insert("", "end", values=row)  # Вставляем найденные записи в Treeview


def add_command():
    database.insert(e_name.get(), e_phone.get(), e_email.get(), e_salary.get())
    view_command()  # Обновляем отображение Treeview


def delete_command():
    database.delete(selected_tuple[0])
    view_command()  # Обновляем отображение Treeview


def update_command():
    database.update(selected_tuple[0], e_name.get(), e_phone.get(), e_email.get(), e_salary.get())
    view_command()  # Обновляем отображение Treeview


def get_selected_row(event):
    global selected_tuple
    index = list1.selection()[0]
    selected_tuple = list1.item(index, 'values')  # Получаем выбранную строку


window = tk.Tk()

window.wm_title("Список сотрудников")

l1 = tk.Label(window, text="ФИО")
l1.grid(row=0, column=0)

l2 = tk.Label(window, text="Номер телефона")
l2.grid(row=1, column=0)

l3 = tk.Label(window, text="Email")
l3.grid(row=2, column=0)

l4 = tk.Label(window, text="Заработная плата")
l4.grid(row=3, column=0)

e_name = tk.StringVar()
e1 = tk.Entry(window, textvariable=e_name)
e1.grid(row=0, column=1)

e_phone = tk.StringVar()
e2 = tk.Entry(window, textvariable=e_phone)
e2.grid(row=1, column=1)

e_email = tk.StringVar()
e3 = tk.Entry(window, textvariable=e_email)
e3.grid(row=2, column=1)

e_salary = tk.StringVar()
e4 = tk.Entry(window, textvariable=e_salary)
e4.grid(row=3, column=1)

list1 = ttk.Treeview(window, columns=("ID", "ФИО", "Телефон", "Email", "ЗП"))
list1.grid(row=0, column=3, rowspan=6, columnspan=2)
list1.heading("ID", text="ID")
list1.heading("ФИО", text="ФИО")
list1.heading("Телефон", text="Телефон")
list1.heading("Email", text="Email")
list1.heading("ЗП", text="ЗП")

list1.bind('<<TreeviewSelect>>', get_selected_row)  # Привязываем обработчик к событию выбора строки

b1 = tk.Button(window, text="Просмотреть все", command=view_command)
b1.grid(row=4, column=0, columnspan=2)

b2 = tk.Button(window, text="Поиск", command=search_command)
b2.grid(row=5, column=0, columnspan=2)

b3 = tk.Button(window, text="Добавить", command=add_command)
b3.grid(row=4, column=3)

b4 = tk.Button(window, text="Обновить", command=update_command)
b4.grid(row=5, column=3)

b5 = tk.Button(window, text="Удалить", command=delete_command)
b5.grid(row=4, column=4)

window.mainloop()
