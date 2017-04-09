
from pyparser.grammar.code import Code

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
    def getExtension(self):
        """Get file extension for this language"""
        raise NotImplementedError
    def getInstanceMethods(self):
        """Return only public and protected methods in class"""
        methods = []
        for method in self.getMethods():
            if not method.isPrivate() and not method.isAbstract():
                methods.append(method)
        return methods
    def getProperties(self):
        """Return all variables and constants in class"""
        raise NotImplementedError
    def getInstanceProperties(self):
        """Return only public and protected properties in class"""
        props = []
        for method in self.getProperties():
            if not prop.isPrivate() and not prop.isConstant():
                props.append(prop)
        return props
    def getFile(self):
        return self.parent
    def getCurrentMethod(self):
        for parsedMethod in self.getMethods():
            if self.getCurrentLineNumber() >= parsedMethod.getStartLineNumber() and self.getCurrentLineNumber() <= parsedMethod.getLastLineNumber():
                return parsedMethod
        raise NoMethodInCurrentLine(self.getCurrentLineNumber())
    def getRegexForValidCharactersInName(self):
        return 'a-zA-Z0-9_-'

class Extractor(object):
    def __init__(self, parent = None):
        self.parent = parent
    def createClass(self, code, startLineNumber):
        raise NotImplementedError
    def getClasses(self, code):
        raise NotImplementedError

class NoMethodInCurrentLine(Exception):
    def __init__(self, lineNumber):
        self.lineNumber = lineNumber
    def __str__(self):
        return repr(self.lineNumber)
