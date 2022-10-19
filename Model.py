
from tkinter.filedialog import askopenfilename

from Types.Contact import Contact


contacts_user = []


def open_file():
    types = (("all files", "*.*"),)
    file_name = askopenfilename(title='Открыть базу данных', filetypes=types)
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            user_list = line.replace('\n', '').split(';')
            user = Contact(user_list[0], user_list[1], user_list[2], user_list[3])
            contacts_user.append(user)
