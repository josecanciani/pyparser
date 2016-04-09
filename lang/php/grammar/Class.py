
from grammar.Class import Class as BaseClass, Extractor as BaseExtractor

class Class(BaseClass):
    def getName(self):
        line = self.getCode().splitlines()[0]
        for word in line.lstrip().split(' '):
            if word.strip() and word.strip() != 'class':
                return word.strip()
        raise InvalidSyntax('Could not find class name in line: ' + line)

class Extractor(BaseExtractor):
    def getClasses(self, code):
        findClosure = None
        classCode = ''
        classes = []
        for line in code.splitlines():
            if findClosure == None:
                if line.lstrip()[0:6] == 'class ':
                    findClosure = line.find('class')
                    classCode = line
            else:
                classCode = classCode + line
                if line.lstrip()[0] == '}' and line.find('}') == findClosure:
                    classes.append(Class(classCode))
                    findClosure = None
        return classes

class InvalidSyntax(IOError):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)
