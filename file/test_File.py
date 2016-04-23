
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
        file = fromCode(code, 'php', 1)
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
        file = fromCode(code, 'php', 1)
        classes = file.getClasses()
        self.assertEqual('Class', classes[0].__class__.__name__)
        self.assertEqual('HelloWorld', classes[0].getName())
        self.assertEqual(code, classes[0].getFile().getCode())

    def test_getCurrentClass(self):
        code = '<? \n class HelloWorld {\n }\n'
        file = fromCode(code, 'php', 0)
        try:
            file.getCurrentClass()
            self.assertTrue(false, 'Expecting NoClassInCurrentLine exception, should not be here')
        except NoClassInCurrentLine as e:
            self.assertEqual('0', str(e))
        file = fromCode(code, 'php', 1)
        self.assertEqual('HelloWorld', file.getCurrentClass().getName())
        file = fromCode(code, 'php', 2)
        self.assertEqual('HelloWorld', file.getCurrentClass().getName())
        file = fromCode(code, 'php', 3)
        try:
            file.getCurrentClass()
            self.assertTrue(false, 'Expecting NoClassInCurrentLine exception, should not be here')
        except NoClassInCurrentLine as e:
            self.assertEqual('3', str(e))


if __name__ == '__main__':
        unittest.main()
