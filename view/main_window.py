import tkinter as tk
from tkinter import ttk
from view import add_contact_window
from view.contact_context_menu import ContactContextMenu
import controller
from view import helpers


class MainWindow:
    def __init__(self):
        root = tk.Tk()
        root.title('Телефонный справочник')

        button_show = tk.Button(root, text='Показать контакты',
                                command=controller.show_contacts)
        button_show.grid(column=0, row=1, sticky='we')
        button_open_file = tk.Button(
            text='Открыть файл', command=controller.open_file)
        button_open_file.grid(column=0, row=2, sticky='we')
        button_save_file = tk.Button(
            text='Сохранить файл', command=controller.save_contacts)
        button_save_file.grid(column=0, row=3, sticky='we')
        button_add_contact = tk.Button(
            text='Добавить контакт', command=lambda: add_contact_window.open_window_add(root))
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

        entry = tk.Entry()
        entry.bind('<KeyRelease>', search_contact)
        entry.grid(column=0, row=8, sticky='we')

        empty_label = tk.Label(root, text='v1.0')
        empty_label.grid(column=0, row=9, sticky='s')
        root.grid_rowconfigure(index=9, minsize=50)

        main_table = ttk.Treeview(root, show='headings')
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

        helpers.center_to_screen(root)

        self.root = root
        self.main_table = main_table

    def run(self):
        self.root.mainloop()
