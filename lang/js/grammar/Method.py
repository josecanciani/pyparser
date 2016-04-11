
import re
from grammar.Method import Method as BaseMethod, Extractor as BaseExtractor
from grammar.Exception import InvalidSyntax

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
        raise NotImplementedError
    def _getKeywords(self):
        return [word.strip() for word in self.getFirstLine().strip().split('(')[0].split(' ') if word.strip()][:-1]

class Extractor(BaseExtractor):
    def getMethods(self, classObject):
        code = classObject.getCode()
        methods = []
        findClosure = None
        methodCode = ''
        pattern = re.compile(ur'^[a-z_]{1}[a-zA-Z0-9-_\$]*\(')
        for line in code.splitlines(True):
            if findClosure == None:
                strippedLine = line.lstrip()
                if strippedLine.startswith('static ') or re.search(pattern, strippedLine):
                    findClosure = len(line) - len(strippedLine)
                    methodCode = line
            else:
                methodCode = methodCode + line
                if line.lstrip()[0] == '}' and line.find('}') == findClosure:
                    methods.append(Method(methodCode))
                    findClosure = None
        return methods
