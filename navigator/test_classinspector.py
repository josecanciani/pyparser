
import unittest
import os
import pprint
from config import Config
from navigator.classinspector import *

class TestClassInspectorConstructor(unittest.TestCase):

    def _getPrinter(self):
        return pprint.PrettyPrinter(indent = 2)

    def _phpClassToFile(self, className, namespace):
        return os.path.dirname(os.path.realpath(__file__)) + '/../RESOURCE/' + className + '.php'

    def _jsClassToFile(self, className, namespace):
        return os.path.dirname(os.path.realpath(__file__)) + '/../RESOURCE/' + className + '.js'

    def _getJsConfig(self):
        return Config(self._jsClassToFile)

    def _getPhpConfig(self):
        return Config(self._phpClassToFile)

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
