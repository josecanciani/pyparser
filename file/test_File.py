
import unittest
import os
import pprint
from file.File import *

class TestFileConstructor(unittest.TestCase):

    def _getPrinter(self):
        return pprint.PrettyPrinter(indent = 2)

    def test_fromFile(self):
        filePath = os.path.dirname(os.path.realpath(__file__)) + '/../RESOURCE/SimpleClass.php'
        file = fromFile(filePath)
        self.assertEqual(open(filePath, 'r').read(), file.getCode())
        self.assertEqual('php', file.getLang())

    def test_fromCode(self):
        code = '<? \n class HelloWorld {\n }\n'
        file = fromCode(code, 'php')
        self.assertEqual(code, file.getCode())
        self.assertEqual('php', file.getLang())

    def test_fromFileException(self):
        with self.assertRaises(FileDoesNotExists):
            fromFile('notExistanteClass.php')

    def test_fromUnsupportedFile(self):
        with self.assertRaises(LanguageNotSupported):
            filePath = os.path.dirname(os.path.realpath(__file__)) + '/../RESOURCE/code.unsupported'
            fromFile(filePath)

    def test_getClasses(self):
        code = '<? \n class HelloWorld {\n }\n'
        file = fromCode(code, 'php')
        classes = file.getClasses()
        self.assertEqual('Class', classes[0].__class__.__name__)


if __name__ == '__main__':
        unittest.main()