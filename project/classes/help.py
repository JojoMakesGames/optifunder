from project.classes.command import Command, Object
from project.classes import commands

class HelpCommand(Command):

    example: str = 'HELP'

    def action(self, obj: Object, input: str) -> Object:
        for command in commands:
            print(command.example)
        return obj

    def check_input(self, obj: Object, input: str) -> str:
        return None