from asyncio import events
import tkinter as tk
from tkinter import Frame, ttk
from functools import partial
from view import geometry, add_contact_window
from view.contact_context_menu import ContactContextMenu
import controller

contact_list = []
# search_text = ''

# def get_contact(event):
#     global contact_list
#     items = main_table.selection()[0]
#     contact_list = [i for i in main_table.item(items, option="values")]


def main_window():
    global contact_list
    global first_window
    global main_table

    first_window = tk.Tk()
    first_window.title('Телефонный справочник')
    # width = 630
    # height = 420
    # size_window = f'{width}x{height}+{geometry.get_width(first_window, width)}+{geometry.get_height(first_window, height)}'
    # first_window.geometry(size_window)
    # first_window.wm_attributes('-topmost', 1)
    first_window.focus_set()
    # first_window.resizable(False, False)

    button_show = tk.Button(text='Показать контакты',
                            command=controller.show_contacts)
    button_show.grid(column=0, row=1, sticky='we')
    button_open_file = tk.Button(
        text='Открыть файл', command=controller.open_file)
    button_open_file.grid(column=0, row=2, sticky='we')
    button_save_file = tk.Button(
        text='Сохранить файл', command=controller.save_contacts)
    button_save_file.grid(column=0, row=3, sticky='we')
    button_add_contact = tk.Button(
        text='Добавить контакт', command=add_contact_window.open_window_add)
    button_add_contact.grid(column=0, row=4, sticky='we')
    button_change_contact = tk.Button(
        text='Изменить контакт', command=controller.change_contact)
    button_change_contact.grid(column=0, row=5, sticky='we')
    button_delete_contact = tk.Button(
        text='Удалить контакт', command=controller.delete_contact)
    button_delete_contact.grid(column=0, row=6, sticky='we')
    lable = tk.Label(text='Для поиска введите имя:')
    lable.grid(column=0, row=7, pady=(50, 0), sticky='w')

    def search_contact(event=None):
        search_text = entry.get()
        controller.search_contact(search_text)

    entry = tk.Entry(width=25)
    entry.bind('<KeyRelease>', search_contact)
    entry.grid(column=0, row=8)

    empty_label = tk.Label(first_window, text='v1.0')
    empty_label.grid(column=0, row=9, sticky='s')
    first_window.grid_rowconfigure(index=9, minsize=50)

    main_table = ttk.Treeview(first_window, show='headings')
    heads = ['id', 'Имя', 'Телефон', 'Комментарий']
    main_table['columns'] = heads
    main_table.column('id', width=30)
    for header in heads:
        main_table.heading(header, text=header, anchor='w')
        if header != 'id':
            main_table.column(header, width=150)
    main_table.grid(column=1, row=0, rowspan=10, sticky='nswe')
    # main_table.bind("<<TreeviewSelect>>", get_contact)

    def do_before_popup(e: tk.Event = None):
        if e:
            pointed_row_id = main_table.identify_row(e.y)
            if pointed_row_id:
                main_table.selection_set(pointed_row_id)

    context_menu = ContactContextMenu(main_table)
    context_menu.action_before_popup = do_before_popup

    tk.mainloop()
