import pickle

from classes import Record, AddressBook, Name, Phone

DEFAULT_ADDRESS_BOOK_PATH = "address_book.txt"


def dump_address_book(path, address_book):
    with open(path, "wb") as f:
        pickle.dump(address_book, f)


def load_address_book(path):
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def input_error(func):
    def inner(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
        except IndexError:
            print('Give me name and phone please')
            main()
        except KeyError:
            print('Enter name of the existing record')
            main()
        except ValueError:
            print(
                'Record with this name already exists. To update record use "update" command')
            main()
        return result
    return inner


@input_error
def main():
    while True:
        statement = input("> ").lower()
        if statement == "hello":
            print("How can I help you?")
        elif statement.startswith('add'):
            _, name, num = statement.split()
            record = Record(Name(name), Phone(num))
            address_book.add(record)
        elif statement.startswith('change'):
            _, name, num = statement.split()
            address_book.edit_record(Name(name), Phone(num))
        elif statement.startswith('phone'):
            _, name = statement.split()
            address_book.phone(Name(name))
        elif statement.startswith('show all'):
            for page in address_book.iterator(5):
                print(page)
        elif statement in ["good bye", "close", "exit"]:
            print("Good bye!")
            dump_address_book(DEFAULT_ADDRESS_BOOK_PATH, address_book)
            break
        elif statement == ".":
            dump_address_book(DEFAULT_ADDRESS_BOOK_PATH, address_book)
            break
        else:
            print('command not found')


if __name__ == "__main__":
    address_book = load_address_book(DEFAULT_ADDRESS_BOOK_PATH)
    main()
