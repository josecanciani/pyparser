
import unittest
from os import path
from config import Config
from navigator.extensionfinder import ExtensionFinder
from navigator.classinspector import ClassInspector

class TestClassExtensionFinder(unittest.TestCase):

    def _phpClassToFile(self, className, namespace):
        return path.dirname(path.realpath(__file__)) + '/../RESOURCE/' + className + '.php'

    def _jsClassToFile(self, className, namespace):
        return path.dirname(path.realpath(__file__)) + '/../RESOURCE/' + className + '.js'

    def _getCodeRoot(self):
        return path.dirname(path.realpath(__file__)) + '/../RESOURCE'

    def _getJsConfig(self):
        return Config(self._jsClassToFile, self._getCodeRoot(), 'js')

    def _getPhpConfig(self):
        return Config(self._phpClassToFile, self._getCodeRoot(), 'php')

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
        finder = ExtensionFinder(phpConfig, pclass, self._getPHPClassExtensions, self._dummyCallback)
        finder.join(5)
        self.assertTrue(len(self._getPHPClassExtensionsResults) > 0, 'Callback _getPHPClassExtensions was never called')
        self.assertEqual(len(self._getPHPClassExtensionsResults), 1)
        self.assertEqual(self._getPHPClassExtensionsResults[0].getName(), 'SimpleClass')

if __name__ == '__main__':
    unittest.main()
