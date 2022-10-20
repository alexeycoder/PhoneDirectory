import tkinter as tk
from view.abstract.modal_window import ModalWindow
from Types.Contact import Contact


class ChangeContactDialog(ModalWindow):
    def __init__(self, parent: tk.BaseWidget, title, contact: Contact):
        self.contact = contact
        super().__init__(parent, title)

    def _compose(self):
        # local methods:
        def set_text(entry: tk.Entry, text):
            entry.delete(0, tk.END)
            entry.insert(0, text)

        def apply_changes_and_close(event=None):
            nonlocal txtbox_name
            nonlocal txtbox_phone
            nonlocal txtbox_comment
            self.contact.name = txtbox_name.get()
            self.contact.phone = txtbox_phone.get()
            self.contact.comment = txtbox_comment.get()
            self._dispose()

        contact = self.contact
        text_header = f'Редактирование контакта ID: {contact.contact_id}'

        # labels - left column:

        lbl_header = tk.Label(self, text=text_header, font='Arial 14')
        lbl_header.grid(column=0, columnspan=2, row=0, pady=20)

        lbl_name = tk.Label(self, text='Имя:')
        lbl_name.grid(column=0, row=1, padx=5, pady=5, sticky='e')

        lbl_phone = tk.Label(self, text='Тел.:')
        lbl_phone.grid(column=0, row=2, padx=5, pady=5, sticky='e')

        lbl_comment = tk.Label(self, text='Комментарий:')
        lbl_comment.grid(column=0, row=3, padx=5, pady=5, sticky='e')

        # text boxes - right column:

        txtbox_name = tk.Entry(self)
        set_text(txtbox_name, contact.name)
        txtbox_name.grid(column=1, row=1, padx=10, pady=5, sticky='we')

        txtbox_phone = tk.Entry(self)
        set_text(txtbox_phone, contact.phone)
        txtbox_phone.grid(column=1, row=2, padx=10, pady=5, sticky='we')

        txtbox_comment = tk.Entry(self, textvariable=contact.comment)
        set_text(txtbox_comment, contact.comment)
        txtbox_comment.grid(column=1, row=3, padx=10, pady=5, sticky='we')

        # OK Cancel:

        btn_ok = tk.Button(self, text='Сохранить',
                           command=apply_changes_and_close)
        btn_ok.grid(column=0, row=4, padx=10, pady=(30, 10), sticky='e')
        self.bind('<Return>', apply_changes_and_close)
        self.bind('<KP_Enter>', apply_changes_and_close)

        btn_cancel = tk.Button(self, text='Отменить',
                               command=lambda: self._dispose)
        btn_cancel.grid(column=1, row=4, padx=10, pady=(30, 10), sticky='w')
