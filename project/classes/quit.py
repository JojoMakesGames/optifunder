from project.classes.command import Command, Object

class QuitCommand(Command):

    example: str = 'QUIT'
    
    def action(self, obj: Object, input: str) -> Object:
        print('Goodbye!')
        exit()

    def check_input(self, obj: Object, input: str) -> str:
        return None