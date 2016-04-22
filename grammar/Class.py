
from grammar.Code import Code

class Class(Code):
    def getName(self):
        raise NotImplementedError
    def getExtendsFromName(self):
        raise NotImplementedError
    def getMethods(self):
        raise NotImplementedError

class Extractor(object):
    def createClass(self, code):
        raise NotImplementedError
    def getClasses(self, code):
        raise NotImplementedError
