
from grammar.Class import Class as BaseClass, Extractor as BaseExtractor
from grammar.Exception import InvalidSyntax

class Class(BaseClass):
    def getName(self):
        line = self.getFirstLine()
        for word in line.lstrip().split(' '):
            if word.strip() and word.strip() != 'class':
                return word.strip()
        raise InvalidSyntax('Could not find class name in line: ' + line)

class Extractor(BaseExtractor):
    def getClasses(self, code):
        findClosure = None
        classCode = ''
        classes = []
        for line in code.splitlines(True):
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
