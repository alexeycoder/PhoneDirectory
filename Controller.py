from tkinter.filedialog import askopenfilename
from Types.Contact import Contact
from view import MainWindow
import Model
import copy
from view import basic_dialog_windows
from view.change_contact_window import ChangeContactDialog


def run():
    MainWindow.main_window()


def open_file():
    Model.open_file()


def show_contacts(contacts_user=Model.contacts_user):
    MainWindow.main_table.delete(*MainWindow.main_table.get_children())
    for i in contacts_user:
        i = [i.contact_id, i.name, i.phone, i.comment]
        MainWindow.main_table.insert('', 'end', values=i)


def save_contacts():
    Model.save_contacts()


def add_contact():
    pass


def _get_selection_as_contact() -> Contact:
    table = MainWindow.main_table
    selection_id = table.focus()
    if selection_id is None or selection_id == '':
        return

    selected_item = table.item(selection_id)

    contact_id = str(selected_item['values'][0])
    return Model.get_contact_by_id(contact_id)


def change_contact():

    contact = _get_selection_as_contact()
    if contact is None:
        basic_dialog_windows.show_warning_dialog('Внимание',
                                                 'Пожалуйста предварительно выбирите контакт для изменения! \U0001F62E')
        return

    resul = ChangeContactDialog(
        MainWindow.root, 'Редактирование контакта', contact)

    show_contacts()


def delete_contact():
    contact = _get_selection_as_contact()
    if contact is None:
        basic_dialog_windows.show_warning_dialog('Внимание',
                                                 'Пожалуйста предварительно выбирите контакт для удаления! \U0001F62E')
    Model.contacts_user.remove(contact)
    show_contacts()

def search_contact(search_text):
    temp_list = [
        i for i in Model.contacts_user if search_text in i.name.lower()]
    show_contacts(temp_list)


def _do_tests():
    temp_contact = Contact(10, 'Вася Пупкин', '123-456', 'Хороший человек')
    clone_contact = copy.copy(temp_contact)
    print(clone_contact)
