
import re
from grammar.method import Method as BaseMethod, Extractor as BaseExtractor
from grammar.exception import InvalidSyntax

class Method(BaseMethod):
    def getName(self):
        return self.getFirstLine().strip().split('(')[0].split(' ')[-1]
    def isPrivate(self):
        return self.getName()[0] == '_'
    def isPublic(self):
        return self.getName()[0] != '_'
    def isProtected(self):
        return False
    def isStatic(self):
        return 'static' in self._getKeywords()
    def isAbstract(self):
        return False
    def _getKeywords(self):
        return [word.strip() for word in self.getFirstLine().strip().split('(')[0].split(' ') if word.strip()][:-1]

class Extractor(BaseExtractor):
    def createMethod(self, code, startLineNumber):
        return Method(code, self.parent, startLineNumber)
    def getMethods(self):
        methods = []
        findClosure = None
        methodCode = ''
        lineNumber = 0
        pattern = re.compile(ur'^[a-z_]{1}[a-zA-Z0-9-_\$]*\(')
        for line in self.parent.getCode().splitlines(True)[1:]:
            lineNumber += 1
            if findClosure == None:
                strippedLine = line.lstrip()
                if strippedLine.startswith('static ') or re.search(pattern, strippedLine):
                    findClosure = len(line) - len(strippedLine)
                    methodCode = line
                    startLineNumber = lineNumber
            else:
                methodCode = methodCode + line
                if line.lstrip()[0] == '}' and line.find('}') == findClosure:
                    methods.append(self.createMethod(methodCode, startLineNumber))
                    findClosure = None
        return methods
