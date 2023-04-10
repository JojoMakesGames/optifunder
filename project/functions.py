import sys

from copy import deepcopy

from collections import namedtuple

Command = namedtuple('Command', ['check_input', 'function', 'example'])

class Object(object):
    pass

# region fetch
example_get: str = 'GET <param> or GET *'
def fetch_param(obj: Object, input: str) -> Object:
    param: str = input
    if param == '*':
        value: str = obj.__dict__
        for key, value in value.items():
            print(key, value)
    elif hasattr(obj, param):
        value: str = getattr(obj, param)
        print(value)
    else:
        print(f'Parameter {param} not found.')
    return obj

def check_fetch_input(obj: Object, input: str) -> str:
    if not input:
        return "Please provide a parameter to fetch. Must be in form GET <param> " 
    return None
# endregion

#region set
example_set: str = 'SET <param>=<value>'
def set_param(obj: Object, input: str) -> Object:
    split: list[str] = input.split('=')
    param: str = split[0]
    value: str = split[1]

    value: str | int | bool = _set_type(value)

    copy: Object = deepcopy(obj)

    setattr(copy, param, value)
    return copy

def check_set_input(obj: Object, input: str) -> str:
    if not input:
        return "Input param not provided. Must be in the form SET <param>=<value>"

    split: list[str] = input.split('=')
    if len(split) != 2:
        return "Number of values passed is wrong. Must be in the form SET <param>=<value>"
    
    param: str = split[0]
    value: str = split[1]

    if not param:
        return "Left side of equation unset. Must be in the form SET <param>=<value>"
    if not value:
        return "Right side of equation unset. Must be in the form SET <param>=<value>"
    
    if hasattr(obj, param):
        param_type: int | bool | str = type(getattr(obj, param))
        new_type: int | bool | str = type(_set_type(value))
        if param_type != new_type:
            return f"Cannot set {param} to {value}. Type mismatch. Expected {param_type} but got {new_type}"

    return None

def _set_type(input: str) -> str | int | bool:
    if input.isdigit():
        return int(input)
    elif input == 'True' or input == 'False':
        return bool(input)
    else:
        return str(input)
# endregion

# region quit
def quit(obj: Object, input: str) -> None:
    print('Goodbye!')
    sys.exit()
# endregion

# region help
def help(obj: Object, input: str) -> None:
    print('Valid commands are:', ', '.join(list(commands.keys())))
# endregion

def no_check(obj: Object, input: str) -> None:
    return None

commands: dict[Command] = {
    'get': Command(check_fetch_input, fetch_param, example_get),
    'set': Command(check_set_input, set_param, example_set),
    'exit': Command(no_check, quit, 'EXIT'),
    'help': Command(no_check, help, 'HELP'),
}


