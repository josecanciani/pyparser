from pyparser.discover.statement import Statement as BaseStatement

class Statement(BaseStatement):
    def getStopChars(self, isBefore):
        if isBefore:
            return [';', '=', '{']
        else:
            return [';', '[', '(']
