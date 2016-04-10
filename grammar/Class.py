
from grammar.Code import Code

class Class(Code):
    def getName(self):
        raise NotImplementedError

class Extractor(object):
    def getClasses(self, code):
        raise NotImplementedError
