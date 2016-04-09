
from grammar.Method import Method as BaseMethod, Extractor as BaseExtractor

keywords = ['static', 'protected', 'public', 'private', 'abstract', 'function']

class Method(BaseMethod):
    def getName(self):
        line = self.getCode().splitlines()[0]
        find = False
        for word in line.lstrip().split(' '):
            if find:
               return word.strip().split('(')[0]
            if word.strip() and word.strip() == 'function':
                find = True
        raise InvalidSyntax('Could not find class name in line: ' + line)
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

class Extractor(BaseExtractor):
    def getMethods(self, classObject):
        code = classObject.getCode()
        methods = []
        findClosure = None
        methodCode = ''
        for line in code.splitlines():
            if findClosure == None:
                for keyword in keywords:
                    if line.lstrip().startswith(keyword):
                        findClosure = line.find(keyword)
                        methodCode = line
            else:
                methodCode = methodCode + line
                if line.lstrip()[0] == '}' and line.find('}') == findClosure:
                    methods.append(Method(methodCode))
                    findClosure = None
        return methods

class InvalidSyntax(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)
