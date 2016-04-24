
class InvalidSyntax(Exception):
    def __init__(self, msg):
        self.msg = msg
    def getMessage():
        return self.msg
    def __str__(self):
        return repr(self.msg)
