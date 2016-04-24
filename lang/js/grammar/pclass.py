
from lang.php.grammar.pclass import Class as PHPClass, Extractor as PHPExtractor
from lang.js.grammar.method import Extractor as MethodExtractor

class Class(PHPClass):
    def getMethods(self):
        extractor = MethodExtractor(self)
        return extractor.getMethods()
    def isAbstract(self):
        return False

class Extractor(PHPExtractor):
    def createClass(self, code, startLineNumber):
        return Class(code, self.parent, startLineNumber)
