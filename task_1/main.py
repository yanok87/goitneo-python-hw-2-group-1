"""This module contains a CLI"""


def parse_input(user_input):
    """This function parses user input"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    """This function handles user input value error"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name was found."
        except IndexError:
            return "No such name was found."

    return inner


@input_error
def add_contact(args, contacts):
    """This function adds a contact to phone book"""
    name, phone = args
    contacts[name] = phone
    print(contacts)
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """This function changes the contact's phone number"""
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        print(contacts)
        return "Contact changed."
    else:
        print("Name not found")


@input_error
def contact(args, contacts):
    """This function returns contact's phone number"""
    name = args[0]
    return contacts[name]


def all_contacts(contacts):
    """This function returns phone book"""
    phone_book = []
    for name, number in contacts.items():
        phone_book.append(f"{name} {number}")
    return phone_book


def main():
    """This function interacts with user and creates a phone book"""
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "good bye"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(contacts)
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(contact(args, contacts))
        elif command == "all":
            print(contacts, "contacts")
            all = all_contacts(contacts)
            for i in all:
                print(i)
        else:
            print("Invalid command.")


if __name__ == "__main__":

    main()
