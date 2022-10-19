class Contact:
    contact_id:str
    name:str
    phone:str
    comment:str

    def __init__(self, contact_id: str, name: str, phone: str, comment: str):
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