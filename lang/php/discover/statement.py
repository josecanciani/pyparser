from pyparser.discover.statement import Statement as BaseStatement
from pyparser.lang.php.grammar.helper import Helper

class Statement(BaseStatement):
    def getStopChars(self, isBefore):
        if isBefore:
            return [';', '=', '{']
        else:
            return [';', '[', '(']

    def getHelper(self):
        return Helper()
