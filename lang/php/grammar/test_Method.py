
import unittest
import os
import pprint
from lang.php.grammar.Class import Class
from lang.php.grammar.Method import Extractor

class TestClass(unittest.TestCase):

    def test_extract(self):
        classCode = 'class HelloWorld {\n   function myFunc() {\n        echo "hola mundo";\n   }\n }'
        myClass = Class(classCode)
        extractor = Extractor()
        methods = extractor.getMethods(myClass)
        self.assertEqual('myFunc', methods[0].getName())


if __name__ == '__main__':
        unittest.main()
