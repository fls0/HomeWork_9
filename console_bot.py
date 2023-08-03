
NAME_PHONE_NUMBERS = {}

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except IndexError:
            return 'Give me name and phone'
        except KeyError:
            return 'Enter user name'
        except ValueError:
            return 'Wrong data type'
    return inner


@input_error
def command_parser(command: str):
    command_lst = command.split()
    for k, v in COMMAND_LIST.items():
        if command_lst[0].lower() in v:
            return k, command_lst[1:]
    return 'Unknown command'


def hello_handler(*args):
    return 'How can i help you?'

@input_error
def add_handler(data):
    NAME_PHONE_NUMBERS[data[0].title()] = int(data[1])
    return f'Contact {data[0]} with number {data[1]} is succefully added'

@input_error
def change_handler(data):
    if data[0].title() in NAME_PHONE_NUMBERS:
        NAME_PHONE_NUMBERS[data[0].title()] = data[1]
    return f'Phone was changed'

def phone_handler(name):
    if name[0].title() in NAME_PHONE_NUMBERS:
        return f'{name[0].title()}, {NAME_PHONE_NUMBERS.get(name[0].title())}'
    return 'Phone not found'

def show_all(*args):
    return print(NAME_PHONE_NUMBERS)

def bye_handler(*args):
    return 'Good bye!'

COMMAND_LIST = {
    hello_handler: ['hello'],
    add_handler: ['add'],
    change_handler: ['change'],
    phone_handler: ['phone'],
    show_all: ['show'],
    bye_handler: ["good", "close", "exit"]
    }



def main():
    while True:
        user_input = input('>>>>')
        func, data = command_parser(user_input)
        result = func(data)
        if result:
            print(result)
        if func == bye_handler:
            break

if __name__ == '__main__':
    main()