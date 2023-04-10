class Object (object):
    pass

class Command:
    example: str
    def action(self, obj: Object, input: str) -> Object:
        pass

    def check_input(self, obj: Object, input: str) -> str:
        pass
