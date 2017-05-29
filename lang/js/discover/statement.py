from pyparser.discover.statement import Statement as BaseStatement
from pyparser.lang.js.grammar.prop import Prop

class Statement(BaseStatement):
    def getStopChars(self, isBefore):
        if isBefore:
            return ['(', '{', '}', ';', ',', '=']
        else:
            return [';', ',', ')', '}', ';', '=']

    def isCurrentPositionAVariable(self):
        prop = Prop('')
        return prop.checkStatement(self)
