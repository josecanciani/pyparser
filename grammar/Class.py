
class Class(object):
    def __init__(self, code):
        self.code = code
    def getCode(self):
        return self.code
    def getName(self):
        raise NotImplementedError

class Extractor(object):
    def getClasses(self, code):
        raise NotImplementedError
