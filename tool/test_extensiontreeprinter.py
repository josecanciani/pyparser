
import unittest
from os import path
from config import Config
from tool.extensiontreeprinter import ExtensionTreePrinter

class TestClassToolExtensionTreePrinter(unittest.TestCase):

    def _phpClassToFile(self, className, namespace):
        return path.dirname(path.realpath(__file__)) + '/../RESOURCE/' + className + '.php'

    def _getCodeRoot(self):
        return path.dirname(path.realpath(__file__)) + '/../RESOURCE'

    def _getPhpConfig(self):
        return Config(self._phpClassToFile, self._getCodeRoot(), 'php')

    def _getTreePrinter(self, printer):
        self._getTreePrinterResult = printer.get()

    def _dummyCallback(self, exception):
        pass

    def test_getPHPClassExtensions(self):
        self._getTreePrinterResult = ''
        phpConfig = self._getPhpConfig()
        printer = ExtensionTreePrinter(phpConfig, 'ParentClass', self._getTreePrinter, self._dummyCallback)
        printer.join(5)
        self.assertTrue(len(self._getTreePrinterResult) > 0, 'Callback _getPHPClassExtensions was never called')
        self.assertEqual(self._getTreePrinterResult, 'ParentClass\n    SimpleClass\n        SimpleClassExtension\n    ZSimpleClass\n')


if __name__ == '__main__':
    unittest.main()
