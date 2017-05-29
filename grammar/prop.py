import re
from pyparser.grammar.code import Code

class Prop(Code):
    def getRegex(self):
        raise NotImplementedError
    def checkStatement(self, statement):
        return True if re.match(self.getRegex(), statement.get(), re.MULTILINE) else False
