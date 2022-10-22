class Contact:
    FIELDS_COUNT = 4

    contact_id: int
    name: str
    phone: str
    comment: str

    def __init__(self, contact_id: int, name: str, phone: str, comment: str):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.comment = comment

    def items(self):
        return (self.contact_id, self.name, self.phone, self.comment)

    def show(self):
        print(f'{self.contact_id} {self.name} {self.phone} {self.comment}')

    def __str__(self):
        return ';'.join(map(str, (self.contact_id, self.name, self.phone, self.comment)))

    def __copy__(self):
        return Contact(self.contact_id, self.name, self.phone, self.comment)

    @staticmethod
    def create_from_csv(data_str: str):
        data_lst = data_str.strip().split(';')
        if len(data_lst) < Contact.FIELDS_COUNT:
            return
        contact_id = -1
        try:
            contact_id = int(data_lst[0])
            return Contact(contact_id, data_lst[1], data_lst[2], data_lst[3])
        except ValueError:
            return
