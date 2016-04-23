
class Code(object):
    def __init__(self, code, parent = None, startLineNumber = None):
        self.code = code
        self.parent = parent
        self.startLineNumber = startLineNumber
    def getCode(self):
        return self.code
    def getFirstLine(self):
        pos = self.getCode().find('\n')
        if pos:
            return self.getCode()[0:pos]
        else:
            return self.getCode()
    def getStartLineNumber(self):
        return self.startLineNumber
    def getLastLineNumber(self):
        return self.startLineNumber + len(self.code.splitlines()) - 1

