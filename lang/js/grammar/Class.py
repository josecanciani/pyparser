
from lang.php.grammar.Class import Class as PHPClass, Extractor as PHPExtractor
from lang.js.grammar.Method import Extractor as MethodExtractor

class Class(PHPClass):
    def getName(self):
        return super(Class, self).getName()
    def getMethods(self):
        extractor = MethodExtractor()
        return extractor.getMethods(self)

class Extractor(PHPExtractor):
    def createClass(self, code):
        return Class(code)
