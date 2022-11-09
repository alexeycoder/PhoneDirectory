import abc
import tkinter as tk

from view import helpers


class ModalWindow(tk.Toplevel, metaclass=abc.ABCMeta):
    def __init__(self, parent: tk.BaseWidget, title):
        tk.Toplevel.__init__(self, parent)
        if title:
            self.title(title)

        self.parent = parent

        self._compose()
        helpers.center_to_parent(self, self.parent)
        self.__make_modal()

    @abc.abstractmethod
    def _compose(self):
        pass

    def __make_modal(self):
        self.parent.update_idletasks()
        self.transient(self.parent)
        self.protocol('WM_DELETE_WINDOW', self._dispose)
        self.bind('<Escape>', lambda e: self._dispose())
        self.focus_set()
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def _dispose(self):
        self.parent.focus_set()
        self.destroy()
