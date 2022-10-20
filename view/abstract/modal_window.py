import tkinter as tk




class ModalWindow(tk.Toplevel):
    def __init__(self, parent: tk.BaseWidget, title):
        tk.Toplevel.__init__(self, parent)
        self.transient(parent)


        if title:
            self.title(title)

        self.parent = parent
        self._compose()
        self.__make_modal()


    def _compose(self):
        pass

    def __make_modal(self):
        self.parent.update_idletasks()
        self.protocol('WM_DELETE_WINDOW', self._dispose)
        self.bind('<Escape>', lambda e: self._dispose())
        self.focus_set()
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def _dispose(self):
        self.parent.focus_set()
        self.destroy()
