from collections import UserDict


class AddressBook(UserDict):
    data = {}

    def add_record(self, Record):
        self.data[Record.name.value] = Record.phone.value


class Record:
    def __init__(self, name, *phones):
        self.name = name
        self.phones = phones

    def add():
        pass

    def delete():
        pass

    def update():
        pass


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass
