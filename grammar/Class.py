
from grammar.Code import Code

class Class(Code):
    def getName(self):
        raise NotImplementedError
    def getExtendsFromName(self):
        raise NotImplementedError
    def getMethods(self):
        raise NotImplementedError
    def getFile(self):
        return self.parent

class Extractor(object):
    def __init__(self, parent = None):
        self.parent = parent
    def createClass(self, code):
        raise NotImplementedError
    def getClasses(self, code):
        raise NotImplementedError
