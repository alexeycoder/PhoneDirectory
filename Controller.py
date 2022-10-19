from tkinter.filedialog import askopenfilename
from Types.Contact import Contact
from view import MainWindow
import Model



def run():
    MainWindow.main_window()

def open_file():
    Model.open_file()
    

def show_contacts():
    MainWindow.main_table.delete(*MainWindow.main_table.get_children())
    for i in Model.contacts_user:
        i = [i.contact_id, i.name, i.phone, i.comment]
        MainWindow.main_table.insert('', 0, values=i)
    

def save_contacts():
    pass

def add_contact():
    pass

def change_contact():
    pass

def delete_contact():
    pass

def search_contact():
    pass