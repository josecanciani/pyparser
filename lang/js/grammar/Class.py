
from lang.php.grammar.Class import Class as PHPClass, Extractor as PHPExtractor
from lang.js.grammar.Method import Extractor as MethodExtractor

class Class(PHPClass):
    def getMethods(self):
        extractor = MethodExtractor(self)
        return extractor.getMethods()

class Extractor(PHPExtractor):
    def createClass(self, code):
        return Class(code, self.parent)
