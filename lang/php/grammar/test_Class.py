
import unittest
import os
import pprint
from lang.php.grammar.Class import Extractor

class TestClass(unittest.TestCase):

    def test_extract(self):
        code = '<? \n class HelloWorld {\n }\n'
        extractor = Extractor()
        classes = extractor.getClasses(code)
        self.assertEqual('HelloWorld', classes[0].getName())


if __name__ == '__main__':
        unittest.main()
