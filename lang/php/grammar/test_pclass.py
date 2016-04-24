
import unittest
import os
import pprint
from lang.php.grammar.pclass import Extractor

class TestClass(unittest.TestCase):

    def test_extract(self):
        code = '<? \n class MyClass extends MyParentClass {\n }\n'
        classCode = ' class MyClass extends MyParentClass {\n }\n'
        extractor = Extractor()
        myClass = extractor.getClasses(code)[0]
        self.assertEqual(classCode, myClass.getCode())
        self.assertEqual('MyClass', myClass.getName())
        self.assertEqual('MyParentClass', myClass.getExtendsFromName())
        self.assertEqual(1, myClass.getStartLineNumber())
        self.assertEqual(2, myClass.getLastLineNumber())

    def test_extractAbstract(self):
        code = '<? \n abstract class MyClass extends MyParentClass {\n }\n'
        classCode = ' abstract class MyClass extends MyParentClass {\n }\n'
        extractor = Extractor()
        myClass = extractor.getClasses(code)[0]
        self.assertEqual(classCode, myClass.getCode())
        self.assertEqual('MyClass', myClass.getName())
        self.assertEqual('MyParentClass', myClass.getExtendsFromName())
        self.assertEqual(True, myClass.isAbstract())


if __name__ == '__main__':
        unittest.main()
