from pyparser.grammar.helper import Helper as BaseHelper

class Helper(BaseHelper):
    def getVariableRegex(self):
        return r"^[a-z][a-zA-Z0-9-_]*$"
    def getClassPropertyCallSymbol(self):
        return '.'
    def getClassStaticCallSymbol(self):
        return '.'
