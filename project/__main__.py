import sys
from functions import commands, Object, Command


if __name__ == '__main__':
    print('Welcome to the object editor. Type HELP for a list of commands.')
    obj: Object = Object()
    while True:
        line: str = sys.stdin.readline()
        input: tuple[str] = [entry.strip() for entry in line.split(' ')]

        if not input:
            print('No input given.')
            continue

        command_name: str = input[0].lower()
        input: str = input[1] if len(input) > 1 else None
        keys: list[str] = list(commands.keys())

        if command_name and command_name in keys:
            try:
                error = commands[command_name].check_input(obj, input)
                if error:
                    print(error)
                    continue
                obj = commands[command_name].function(obj, input)
            except Exception as e:
                print(e)
        else:
            print(command_name, 'is not a valid command. Valid commands are:', ', '.join(keys))



