import tkinter as tk
from functools import partial
import controller
from view import helpers


add_window: tk.Tk
add_entry = []
change_entry = []


def open_window_add(parent):
    global add_window
    global add_entry

    add_window = tk.Toplevel(parent)
    add_window.title('Создать контакт')

    helpers.center_to_parent(add_window, parent)

    add_window.wm_attributes('-topmost', 1)
    add_window.columnconfigure(index=0, weight=50)
    add_window.columnconfigure(index=1, weight=250)

    name_lable = tk.Label(add_window, text='Имя')
    phone_lable = tk.Label(add_window, text='Телефон')
    comment_lable = tk.Label(add_window, text='Коментарий')
    name_lable.grid(column=0, row=0, stick='e')
    phone_lable.grid(column=0, row=1, stick='e')
    comment_lable.grid(column=0, row=2, stick='e')

    add_entry = [tk.Entry(add_window, width=30) for _ in range(3)]
    for i, entry in enumerate(add_entry):
        add_entry[i].grid(column=1, row=i)

    add_button = tk.Button(add_window, text='Создать',
                           command=partial(controller.add_contact, add_entry))
    add_button.grid(column=1, row=3)
