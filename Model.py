
from tkinter.filedialog import askopenfilename, asksaveasfilename

from Types.Contact import Contact


contacts_user: list[Contact] = []


def get_contact_by_id(contact_id):
    contact_id = str(contact_id)
    if int(contact_id) < 0:
        return
    try:
        return next(con for con in contacts_user if con.contact_id == contact_id)
    except StopIteration:
        return

def change_contact(contact: Contact) -> bool:
    pass



def open_file():
    types = (("all files", "*.*"), ("all files", "*.*"))
    file_name = askopenfilename(title='Открыть базу данных', filetypes=types)
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            user_list = line.replace('\n', '').split(';')
            user = Contact(user_list[0], user_list[1],
                           user_list[2], user_list[3])
            contacts_user.append(user)


def save_contacts():
    types = (("Текстовый файл", "*.txt"), ("all files", "*.*"))
    full_name = asksaveasfilename(
        title='Сохранить как...', filetypes=types, initialfile='phonebook.txt')
    with open(full_name, 'w', encoding='UTF-8') as file:
        data = ''
        for contact in contacts_user:
            data += contact.__str__() + '\n'
        print(data)
        file.write(data)
