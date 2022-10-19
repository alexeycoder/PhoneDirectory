from tkinter.filedialog import askopenfilename
from Types.Contact import Contact
from view import MainWindow, AddContactWindow, basic_dialog_windows
from view.change_contact_window import ChangeContactDialog
import Model



def run():
    MainWindow.main_window()

def open_file():
    Model.open_file()
    

def show_contacts(contacts_user = Model.contacts_user):
    MainWindow.main_table.delete(*MainWindow.main_table.get_children())
    for i in contacts_user:
        i = [i.contact_id, i.name, i.phone, i.comment]
        MainWindow.main_table.insert('', 'end', values=i)
    

def save_contacts():
    Model.save_contacts()

def add_contact(add_entry: list):
    temp = Contact(Model.next_id(), add_entry[0].get(), add_entry[1].get(), add_entry[2].get())
    Model.contacts_user.append(temp)
    AddContactWindow.add_window.destroy()
    show_contacts()

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
        MainWindow.first_window, 'Редактирование контакта', contact)

    show_contacts()


def delete_contact():
    contact = _get_selection_as_contact()
    if contact is None:
        basic_dialog_windows.show_warning_dialog('Внимание',
                                                 'Пожалуйста предварительно выбирите контакт для удаления! \U0001F62E')
    Model.contacts_user.remove(contact)
    show_contacts()


def search_contact(search_text):
    temp_list = [i for i in Model.contacts_user if search_text in i.name.lower() or search_text in i.name]
    show_contacts(temp_list)

