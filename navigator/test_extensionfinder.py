
import unittest
from os import path
from pyparser.config import Config
from pyparser.navigator.extensionfinder import ExtensionFinder
from pyparser.navigator.classinspector import ClassInspector

class TestClassExtensionFinder(unittest.TestCase):

    def _classToFile(self, className, lang, namespace):
        return path.dirname(path.realpath(__file__)) + '/../RESOURCE/' + className + '.' + lang

    def _getCodeRoot(self):
        return path.dirname(path.realpath(__file__)) + '/../RESOURCE'

    def _getJsConfig(self):
        return Config(self._classToFile, self._getCodeRoot(), 'js')

    def _getPhpConfig(self):
        return Config(self._classToFile, self._getCodeRoot(), 'php')

    def _getPHPClassExtensions(self, results):
        self._getPHPClassExtensionsResults = results

    def _dummyCallback(self, exception):
        pass

    def test_getPHPClassExtensions(self):
        self._getPHPClassExtensionsRun = []
        className = 'ParentClass'
        phpConfig = self._getPhpConfig()
        inspector = ClassInspector(phpConfig, className)
        pclass = inspector.getClass(className)
        finder = ExtensionFinder(phpConfig, pclass, None, self._getPHPClassExtensions, self._dummyCallback)
        finder.join(5)
        self.assertTrue(len(self._getPHPClassExtensionsResults) > 0, 'Callback _getPHPClassExtensions was never called')
        self.assertEqual(len(self._getPHPClassExtensionsResults), 4)
        self._getPHPClassExtensionsResults.sort(key = lambda x: x.getName())
        self.assertEqual(self._getPHPClassExtensionsResults[0].getName(), 'SimpleClass')
        self.assertEqual(self._getPHPClassExtensionsResults[1].getName(), 'SimpleClass2')
        self.assertEqual(self._getPHPClassExtensionsResults[2].getName(), 'SimpleClassExtension')
        self.assertEqual(self._getPHPClassExtensionsResults[3].getName(), 'ZSimpleClass')

if __name__ == '__main__':
    unittest.main()
