from tkinter.filedialog import askopenfilename, asksaveasfilename
from entities.contact import Contact


contacts: list[Contact] = []
max_contact_id: int = -1


def next_id():
    global max_contact_id
    max_contact_id += 1
    return max_contact_id


def get_contact_by_id(contact_id: int):
    if contact_id < 0:
        return
    try:
        return next(con for con in contacts if con.contact_id == contact_id)
    except StopIteration:
        return


def open_file(file_path):
    global max_contact_id

    if file_path == '':
        return

    contacts.clear()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            contact = Contact.create_from_csv(line)
            if contact.contact_id >= max_contact_id:
                max_contact_id = contact.contact_id

            contacts.append(contact)


def save_contacts(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        data = ''
        for contact in contacts:
            data += str(contact) + '\n'
        file.write(data)
