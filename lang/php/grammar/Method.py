
from grammar.Method import Method as BaseMethod, Extractor as BaseExtractor
from grammar.Exception import InvalidSyntax

keywords = ['static', 'protected', 'public', 'private', 'abstract', 'function']

class Method(BaseMethod):
    def getName(self):
        line = self.getFirstLine()
        find = False
        for word in line.lstrip().split(' '):
            if find:
               return word.strip().split('(')[0]
            if word.strip() and word.strip() == 'function':
                find = True
        raise InvalidSyntax('Could not find method name in line: ' + line)
    def isPrivate(self):
        return 'private' in self._getKeywords()
    def isPublic(self):
        return 'public' in self._getKeywords() or (not self.isPrivate() and not self.isProtected())
    def isProtected(self):
        return 'protected' in self._getKeywords()
    def isStatic(self):
        return 'static' in self._getKeywords()
    def isAbstract(self):
        return 'abstract' in self._getKeywords()
    def _getKeywords(self):
        return [word.strip() for word in self.getFirstLine().strip().split('function')[0].split(' ') if word.strip()]

class Extractor(BaseExtractor):
    def getMethods(self):
        methods = []
        findClosure = None
        methodCode = ''
        for line in self.parent.getCode().splitlines(True)[1:]:
            if findClosure == None:
                for keyword in keywords:
                    if line.lstrip().startswith(keyword):
                        if line.find('abstract ') >= 0:
                            methods.append(Method(line, self.parent))
                        else:
                            findClosure = line.find(keyword)
                            methodCode = line

            else:
                methodCode = methodCode + line
                strippedLine = line.lstrip()
                if len(strippedLine) and strippedLine[0] == '}' and line.find('}') == findClosure:
                    methods.append(Method(methodCode, self.parent))
                    findClosure = None
        return methods
