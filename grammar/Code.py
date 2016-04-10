
class Code(object):
    def __init__(self, code):
        self.code = code
    def getCode(self):
        return self.code
    def getFirstLine(self):
        pos = self.getCode().find('\n')
        if pos:
            return self.getCode()[0:pos]
        else:
            return self.getCode()

