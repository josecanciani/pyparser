
from lang.php.grammar.Class import Class as PHPClass, Extractor as PHPExtractor

class Class(PHPClass):
    def getName(self):
        return super(Class, self).getName()

class Extractor(PHPExtractor):
    def createClass(self, code):
        return Class(code)
