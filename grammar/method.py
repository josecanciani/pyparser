
from pyparser.grammar.code import Code

class Method(Code):
    def getName(self):
        raise NotImplementedError
    def isPrivate(self):
        raise NotImplementedError
    def isPublic(self):
        raise NotImplementedError
    def isProtected(self):
        raise NotImplementedError
    def isStatic(self):
        raise NotImplementedError
    def isAbstract(self):
        raise NotImplementedError
    def getClass(self):
        return self.parent

class Extractor(object):
    def __init__(self, parent = None):
        self.parent = parent
    def createMethod(self, code, startLineNumber):
        raise NotImplementedError
    def getMethods(self, code):
        raise NotImplementedError
