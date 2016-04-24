
class Code(object):
    def __init__(self, code, parent = None, startLineNumber = None):
        self.code = code
        self.parent = parent
        self.startLineNumber = startLineNumber
        if self.parent and self.parent.getCurrentLineNumber() is not None and self.getStartLineNumber() is not None and self.parent.getCurrentLineNumber() >= self.getStartLineNumber() and self.parent.getCurrentLineNumber() <= self.getLastLineNumber():
            self.currentLineNumber = self.parent.getCurrentLineNumber() - self.getStartLineNumber()
        else:
            self.currentLineNumber = None
    def getCode(self):
        return self.code
    def getFirstLine(self):
        pos = self.getCode().find('\n')
        if pos:
            return self.getCode()[0:pos]
        else:
            return self.getCode()
    def getStartLineNumber(self):
        """ Start line ralative to the parent """
        return self.startLineNumber
    def getLastLineNumber(self):
        """ End line ralative to the parent """
        return self.startLineNumber + len(self.code.splitlines()) - 1
    def getCurrentLineNumber(self):
        """ Current line, absolute number for this object """
        return self.currentLineNumber

