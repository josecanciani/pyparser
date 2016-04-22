
import unittest
import os
import pprint
from Config import Config
from navigator.ClassInspector import *

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

    def test_getMethods(self):
        # PHP
        inspector = ClassInspector(self._getPhpConfig(), 'SimpleClass', None)
        methods = inspector.getInstanceMethods()
        self.assertNotEqual(0, len(methods))
        self.assertEqual('myFirstMethod', methods[0].getName())
        # JS
        inspector = ClassInspector(self._getJsConfig(), 'SimpleClass', None)
        methods = inspector.getInstanceMethods()
        self.assertNotEqual(0, len(methods))
        self.assertEqual('myFirstMethod', methods[0].getName())


if __name__ == '__main__':
        unittest.main()
