
from pyparser.grammar.classprop import ClassProp as BaseProp, Extractor as BaseExtractor
from pyparser.grammar.exception import InvalidSyntax

keywords = ['static', 'protected', 'public', 'private', 'const', '$']

class Prop(BaseProp):
    def getName(self):
        line = self.getFirstLine()
        separator = '=' if line.find('=') > 0 else ';'
        word = line.split(separator)[0].strip().split(' ')[-1]
        if not word or not len(word):
            raise InvalidSyntax('Could not find property name in line: ' + line)
        return word[1:] if word[0] == '$' else word
    def isPrivate(self):
        return 'private' in self._getKeywords()
    def isPublic(self):
        return 'public' in self._getKeywords() or (not self.isPrivate() and not self.isProtected())
    def isProtected(self):
        return 'protected' in self._getKeywords()
    def isStatic(self):
        return 'static' in self._getKeywords()
    def isConstant(self):
        return 'const' in self._getKeywords()
    def _getKeywords(self):
        separator = self.getName()
        if self.getFirstLine().find('$') >= 0:
            separator = '$' + separator
        return [word.strip() for word in self.getFirstLine().strip().split(separator)[0].split(' ') if word.strip()]

class Extractor(BaseExtractor):
    def createProperty(self, code, startLineNumber):
        return Prop(code, self.parent, startLineNumber)
    def getProperties(self):
        properties = []
        methods = self.parent.getMethods()
        lineNumber = 0
        endLine = None
        for line in self.parent.getCode().splitlines(True)[1:]:
            lineNumber += 1
            if endLine:
                if lineNumber > endLine:
                    endLine = None
                else:
                    continue
            for method in methods:
                if method.getStartLineNumber() == lineNumber:
                    endLine = method.getLastLineNumber()
                    continue
            for keyword in keywords:
                if line.lstrip().startswith(keyword):
                    properties.append(self.createProperty(line, lineNumber))
        return properties
