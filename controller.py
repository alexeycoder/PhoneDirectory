from tkinter.filedialog import askopenfilename, asksaveasfilename
from entities.contact import Contact
from view import add_contact_window, basic_dialog_windows
from view.main_window import MainWindow
from view.change_contact_window import ChangeContactDialog
import model


root_window: MainWindow


def run():
    global root_window
    root_window = MainWindow()
    root_window.run()


def open_file():
    types = (("All files", "*.*"), ("CSV files", ".txt .csv"))
    file_path = askopenfilename(title='Открыть базу данных', filetypes=types)
    if file_path != '':
        model.open_file(file_path)


def show_contacts(contacts_user=model.contacts):
    root_window.main_table.delete(*root_window.main_table.get_children())
    for i in contacts_user:
        i = [i.contact_id, i.name, i.phone, i.comment]
        root_window.main_table.insert('', 'end', values=i)


def save_contacts():
    types = (("All files", "*.*"), ("CSV files", ".txt .csv"))
    file_path = asksaveasfilename(
        title='Сохранить как\u2026', filetypes=types, initialfile='phone_book.txt')
    if file_path != '':
        model.save_contacts(file_path)


def add_contact(add_entry: list):
    temp = Contact(model.next_id(), add_entry[0].get(
    ), add_entry[1].get(), add_entry[2].get())
    model.contacts.append(temp)
    add_contact_window.add_window.destroy()
    show_contacts()


def _get_selection_as_contact() -> Contact:
    table = root_window.main_table
    selected_tids = table.selection()
    if selected_tids is None or len(selected_tids) == 0:
        return

    selected_tid = selected_tids[0]
    selected_item = table.item(selected_tid)

    contact_id = int(selected_item['values'][0])
    return model.get_contact_by_id(contact_id)


def change_contact():

    contact = _get_selection_as_contact()
    if contact is None:
        basic_dialog_windows.show_warning_dialog('Внимание',
                                                 'Пожалуйста предварительно выбирите контакт для изменения! \U0001F62E')
        return

    ChangeContactDialog(
        root_window.root, 'Редактирование контакта', contact)

    show_contacts()


def delete_contact():
    contact = _get_selection_as_contact()
    if contact is None:
        basic_dialog_windows.show_warning_dialog('Внимание',
                                                 'Пожалуйста предварительно выбирите контакт для удаления! \U0001F62E')
        return

    model.contacts.remove(contact)
    show_contacts()


def search_contact(search_text):
    temp_list = [i for i in model.contacts if search_text in i.name.lower(
    ) or search_text in i.name]
    show_contacts(temp_list)
