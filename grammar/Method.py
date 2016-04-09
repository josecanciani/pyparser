
class Method(object):
    def __init__(self, code):
        self.code = code
    def getCode(self):
        return self.code
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
