from pyparser.grammar.helper import Helper as BaseHelper

class Helper(BaseHelper):
    def getVariableRegex(self):
        return r"^\$[a-z-A-Z][a-zA-Z0-9-_]*$"
