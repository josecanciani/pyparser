
from grammar.Code import Code

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

class Extractor(object):
    def getMethods(self, code):
        raise NotImplementedError
