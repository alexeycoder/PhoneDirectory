import tkinter as tk
import controller


class ContactContextMenu:
    def __init__(self, parent: tk.BaseWidget):
        self.parent = parent
        self.menu = tk.Menu(parent, tearoff=0)
        self.menu.add_command(label='Изменить',
                              command=controller.change_contact)
        self.menu.add_command(
            label='Удалить', command=controller.delete_contact)
        self.menu.bind('<FocusOut>', self.hide)
        self.is_shown = False
        self.suppress_hiding_cycle = False

        parent.bind('<Button-3>', self.show, add=True)

    def action_before_popup(event: tk.Event = None):
        pass

    def show(self, event: tk.Event = None):
        if event is None:
            return

        if self.is_shown:
            self.suppress_hiding_cycle = True

        self.action_before_popup(event)
        self.menu.update_idletasks()

        try:
            self.menu.tk_popup(event.x_root, event.y_root)
            self.menu.focus_set()
            self.is_shown = True
        finally:
            self.menu.grab_release()

    def hide(self, event=None):
        if self.suppress_hiding_cycle:
            self.suppress_hiding_cycle = False
            return
        self.menu.unpost()
        self.menu.grab_release()
        self.is_shown = False
