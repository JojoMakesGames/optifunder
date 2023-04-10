from classes.command import Command, Object

class GetCommand(Command):

    example: str = 'GET <param> or GET *'

    def action(self, obj: Object, input: str) -> Object:
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
    
    def check_input(self, obj: Object, input: str) -> str:
        if not input:
            return "Please provide a parameter to fetch. Must be in form GET <param> " 
        return None