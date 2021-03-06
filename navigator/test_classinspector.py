
import unittest
from os import path
from pyparser.config import Config
from pyparser.navigator.classinspector import *

class TestClassInspectorConstructor(unittest.TestCase):

    def _classToFile(self, className, lang, namespace):
        return path.dirname(path.realpath(__file__)) + '/../RESOURCE/' + className + '.' + lang

    def _getCodeRoot(self):
        return path.dirname(path.realpath(__file__)) + '/../RESOURCE'

    def _getJsConfig(self):
        return Config(self._classToFile, self._getCodeRoot(), 'js')

    def _getPhpConfig(self):
        return Config(self._classToFile, self._getCodeRoot(), 'php')

    def test_getClass(self):
        # PHP
        inspector = ClassInspector(self._getPhpConfig(), 'SimpleClass', None)
        mySimpleClass = inspector.getClass()
        self.assertEqual('SimpleClass', mySimpleClass.getName())
        # JS
        inspector = ClassInspector(self._getJsConfig(), 'SimpleClass', None)
        mySimpleClass = inspector.getClass()
        self.assertEqual('SimpleClass', mySimpleClass.getName())

    def test_getInstanceMethods(self):
        # PHP
        inspector = ClassInspector(self._getPhpConfig(), 'SimpleClass', None)
        methods = inspector.getInstanceMethods()
        for method in methods:
            if method.getClass().getName() != 'SimpleClass':
                self.assertFalse(method.isPrivate())
        self.assertEqual(2, len(methods))
        self.assertEqual('myFirstMethod', methods[0].getName())
        self.assertEqual('myProtectedMethod', methods[1].getName())
        # JS
        inspector = ClassInspector(self._getJsConfig(), 'SimpleClass', None)
        methods = inspector.getInstanceMethods()
        for method in methods:
            if method.getClass().getName() != 'SimpleClass':
                self.assertFalse(method.isPrivate())
        self.assertEqual(2, len(methods))
        self.assertEqual('myFirstMethod', methods[0].getName())
        self.assertEqual('myProtectedMethod', methods[1].getName())


if __name__ == '__main__':
    unittest.main()
