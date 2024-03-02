"""This module creates a contact booke"""

from collections import UserDict


class Field:
    """This class contains a generic field"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """This class stands for name field"""

    pass


class Phone(Field):
    """This class validates user's number"""

    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            raise Exception("Phone number has to be 10 digits")


class Record:
    """This class contains name and phone numbers"""

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """This func adds phone number"""

        validated_phone = Phone(phone)
        self.phones.append(validated_phone)

    def remove_phone(self, phone):
        """This func removes phone number"""

        for user_phone in self.phones:
            if user_phone.value == phone:
                self.phones.remove(user_phone)

    def edit_phone(self, old_phone, new_phone):
        """This func edits phone number"""

        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        """This func finds phone number and reutns Phone class"""

        for user_phone in self.phones:
            if user_phone.value == phone:
                return user_phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """This class contains user records"""

    def add_record(self, record: Record):
        """This func adds user record"""
        self.data[record.name.value] = record

    def find(self, n):
        """This func finds and returns user record"""

        res = self.data[n]
        return res

    def delete(self, n):
        """This func deletes user record"""

        del self.data[n]
