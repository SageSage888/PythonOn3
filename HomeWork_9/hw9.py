<<<<<<< HEAD

contacts = {}


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
            add(name, num)
        elif statement.startswith('change'):
            _, name, num = statement.split()
            change(name, num)
        elif statement.startswith('phone'):
            _, name = statement.split()
            phone(name)
        elif statement.startswith('show all'):
            show_all()
        elif statement in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif statement == ".":
            break


def add(name, num):
    contacts[name] = num


def change(name, num):
    contacts[name] = num


def phone(name):
    print(contacts[name])


def show_all():
    print(contacts)


if __name__ == "__main__":
    main()
=======

contacts = {}


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
            add(name, num)
        elif statement.startswith('change'):
            _, name, num = statement.split()
            change(name, num)
        elif statement.startswith('phone'):
            _, name = statement.split()
            phone(name)
        elif statement.startswith('show all'):
            show_all()
        elif statement in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif statement == ".":
            break


def add(name, num):
    contacts[name] = num


def change(name, num):
    contacts[name] = num


def phone(name):
    print(contacts[name])


def show_all():
    print(contacts)


if __name__ == "__main__":
    main()
>>>>>>> 037c4d88185f51b915bb3be8f3da35867d0a1dae
