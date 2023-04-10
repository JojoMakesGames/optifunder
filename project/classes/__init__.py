
from project.classes.get import GetCommand
from project.classes.quit import QuitCommand
from project.classes.set import SetCommand


commands = {
    'get': GetCommand(),
    'set': SetCommand(),
    'quit': QuitCommand(),
}