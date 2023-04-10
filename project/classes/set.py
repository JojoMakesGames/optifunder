from copy import deepcopy
from project.classes.command import Command, Object

class SetCommand(Command):

    example: str = 'SET name=John'
    
    def action(self, obj: Object, input: str) -> Object:
        split: list[str] = input.split('=')
        param: str = split[0]
        value: str = split[1]

        value: str | int | bool = self._set_type(value)

        copy: Object = deepcopy(obj)

        setattr(copy, param, value)
        return copy

    def check_input(self, obj: Object, input: str) -> str:
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
            new_type: int | bool | str = type(self._set_type(value))
            if param_type != new_type:
                return f"Type mismatch. Expected {param_type} but got {new_type}"
        return None
        
