from tkinter.filedialog import askopenfilename
from Types.Contact import Contact
from view import MainWindow
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

def add_contact():
    pass

def change_contact():
    pass

def delete_contact():
    pass

def search_contact(search_text):
    temp_list = [i for i in Model.contacts_user if search_text in i.name.lower()]
    show_contacts(temp_list)

