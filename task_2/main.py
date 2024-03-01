from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass
    """@property
    def value(self):
        return self.value

    @value.setter
    def value(self, v):
        if len(v) == 10:
            raise Exception("Phone number has to be 10 digits")
        else:
            self.value = v"""


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        validated_phone = Phone(phone)
        self.phones.append(validated_phone.value)

    def remove_phone(self, phone):
        validated_phone = Phone(phone)
        self.phones.remove(validated_phone.value)

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)
        print(self.phones, "self.phones edit")

    def find_phone(self, phone):
        return print(f"{self.name}: {phone}")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, n):
        res = self.data[n]
        return res

    def delete(self, n):
        del self.data[n]
        print(self.data, "book deleted")

    # Створення нової адресної книги


book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1111111111")
john_record.add_phone("55555555559")
john_record.edit_phone("55555555559", "1112223333")
# john_record.remove_phone("55555555559")


# Додавання запису John до адресної книги
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
print(john, "trying to print john")
john.edit_phone("1112223333", "1234567890")
found_phone = john.find_phone("1234567890")
print(f"{john.name}: {found_phone} --- found phone")
book.delete("Jane")
