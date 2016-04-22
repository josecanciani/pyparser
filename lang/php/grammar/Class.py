
from grammar.Class import Class as BaseClass, Extractor as BaseExtractor
from grammar.Exception import InvalidSyntax
from lang.php.grammar.Method import Extractor as MethodExtractor

class Class(BaseClass):
    def getName(self):
        line = self.getFirstLine()
        for word in line.lstrip().split(' '):
            if word.strip() and word.strip() != 'class':
                return word.strip()
        raise InvalidSyntax('Could not find class name in line: ' + line)
    def getExtendsFromName(self):
        line = self.getFirstLine()
        next = False
        for word in line.lstrip().split(' '):
            if next:
                return word.strip()
            if word == 'extends':
                next = True
        return None
    def getMethods(self):
        extractor = MethodExtractor()
        return extractor.getMethods(self)

class Extractor(BaseExtractor):
    def createClass(self, code):
        return Class(code)
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
                    classes.append(self.createClass(classCode))
                    findClosure = None
        return classes
