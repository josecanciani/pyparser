
from grammar.Code import Code

class Class(Code):
    def getName(self):
        raise NotImplementedError
    def getExtendsFromName(self):
        raise NotImplementedError
    def isAbstract(self):
        raise NotImplementedError
    def getMethods(self):
        """Return all methods in class"""
        raise NotImplementedError
    def getInstanceMethods(self):
        """Return only public and protected methods in class"""
        methods = []
        for method in self.getMethods():
            if not method.isPrivate() and not method.isAbstract():
                methods.append(method)
        return methods
    def getFile(self):
        return self.parent

class Extractor(object):
    def __init__(self, parent = None):
        self.parent = parent
    def createClass(self, code, startLineNumber):
        raise NotImplementedError
    def getClasses(self, code):
        raise NotImplementedError
