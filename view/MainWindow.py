from functools import partial



import Controller
import tkinter as tk
from tkinter import Frame, ttk
from view import AddContactWindow, Geometry


contact_list = []
# search_text = ''

# def get_contact(event):
#     global contact_list
#     items = main_table.selection()[0]
#     contact_list = [i for i in main_table.item(items, option="values")]


def main_window():
    global contact_list
    global first_window
    first_window = tk.Tk()
    first_window.title('Телефонный справочник')
    width = 630
    height = 420
    size_window = f'{width}x{height}+{Geometry.get_width(first_window, width)}+{Geometry.get_height(first_window, height)}'
    first_window.geometry(size_window)
    first_window.wm_attributes('-topmost', 1)
    first_window.focus_set()
    first_window.resizable(False, False)

    button_show = tk.Button(text = 'Показать контакты', command= Controller.show_contacts)
    button_show.grid(column=0, row=1, stick='ew')
    button_open_file = tk.Button(text = 'Открыть файл', command=Controller.open_file)
    button_open_file.grid(column=0, row=2, stick='ew')
    button_save_file = tk.Button(text = 'Сохранить файл', command=Controller.save_contacts)
    button_save_file.grid(column=0, row=3, stick='ew')
    button_add_contact = tk.Button(text = 'Добавить контакт', command=AddContactWindow.open_window_add)
    button_add_contact.grid(column=0, row=4, stick='ew')
    button_change_contact = tk.Button(text = 'Изменить контакт', command=Controller.change_contact)
    button_change_contact.grid(column=0, row=5, stick='ew')
    button_delete_contact = tk.Button(text = 'Удалить контакт', width=20, command=Controller.delete_contact)
    button_delete_contact.grid(column=0, row=6, stick='ew')
    lable = tk.Label(text = 'Для поиска введите имя:')
    lable.place(x = 2, y = 180)

    def search_contact(event):
        search_text = entry.get()
        Controller.search_contact(search_text)

    entry = tk.Entry(width=25)
    entry.bind('<KeyRelease>', search_contact)
    entry.place(x = 2, y = 200)

    # button_search_contact = tk.Button(text = 'Поиск', width=20)
    # button_search_contact.place(x = 2, y = 220)

    frame = Frame(first_window, width=100)
    frame.place(x = 150, y = 0)
    global main_table
    main_table = ttk.Treeview(frame, show='headings', height=20)
    heads = ['id', 'Имя', 'Телефон', 'Комментарий']
    main_table['columns'] = heads
    main_table.column('id', width=30)
    for header in heads:
        main_table.heading(header, text=header, anchor='w')
        if header != 'id':
            main_table.column(header, width=150)
    main_table.pack()
    # main_table.bind("<<TreeviewSelect>>", get_contact)

    tk.mainloop()