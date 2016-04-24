
from grammar.pclass import Class as BaseClass, Extractor as BaseExtractor
from grammar.exception import InvalidSyntax
from lang.php.grammar.method import Extractor as MethodExtractor

keywords = ['abstract', 'class']

class Class(BaseClass):
    def getName(self):
        line = self.getFirstLine()
        find = False
        for word in line.lstrip().split(' '):
            if find:
               return word.strip().split('(')[0]
            if word.strip() and word.strip() == 'class':
                find = True
        raise InvalidSyntax('Could not find class name in line: ' + line)
    def isAbstract(self):
        line = self.getFirstLine()
        for word in line.lstrip().split(' '):
            if word.strip() and word.strip() == 'abstract':
                return True
        return False
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
        extractor = MethodExtractor(self)
        return extractor.getMethods()

class Extractor(BaseExtractor):
    def createClass(self, code, startLineNumber):
        return Class(code, self.parent, startLineNumber)
    def getClasses(self, code):
        findClosure = None
        classCode = ''
        classes = []
        lineNumber = -1
        for line in code.splitlines(True):
            lineNumber += 1
            if findClosure == None:
                for keyword in keywords:
                    if line.lstrip().startswith(keyword):
                        findClosure = line.find(keyword)
                        classCode = line
                        startLineNumber = lineNumber
            else:
                classCode = classCode + line
                strippedLine = line.lstrip()
                if len(strippedLine) and strippedLine[0] == '}' and line.find('}') == findClosure:
                    classes.append(self.createClass(classCode, startLineNumber))
                    findClosure = None
        return classes
