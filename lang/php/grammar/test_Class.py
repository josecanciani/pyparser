
import unittest
import os
import pprint
from lang.php.grammar.Class import Extractor

class TestClass(unittest.TestCase):

    def test_extract(self):
        code = '<? \n class MyClass {\n }\n'
        classCode = ' class MyClass {\n }\n'
        extractor = Extractor()
        myClass = extractor.getClasses(code)[0]
        self.assertEqual(classCode, myClass.getCode())
        self.assertEqual('MyClass', myClass.getName())


if __name__ == '__main__':
        unittest.main()
