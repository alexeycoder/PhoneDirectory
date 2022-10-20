import tkinter as tk
from tkinter import ttk
import Controller


class ContactContextMenu:
    def __init__(self, parent: tk.BaseWidget):
        self.parent = parent
        self.menu = tk.Menu(parent, tearoff=0)
        self.menu.add_command(label='Изменить',
                              command=Controller.change_contact)
        self.menu.add_command(
            label='Удалить', command=Controller.delete_contact)
        parent.bind('<Button-3>', self.show)
        parent.bind('<FocusOut>', self.hide)

    def show(self, event: tk.Event = None):
        if event is None:
            return
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def hide(self, event=None):
        #self.menu.grab_release()
        #self.menu.unpost()
        pass
        
