
import unittest
from os import path
from config import Config
from file.finder import Finder

class TestClassFinderConstructor(unittest.TestCase):

    def _phpClassToFile(self, className, namespace):
        return path.dirname(path.realpath(__file__)) + '/../RESOURCE/' + className + '.php'

    def _getCodeRoot(self):
        return path.dirname(path.realpath(__file__)) + '/../RESOURCE'

    def _getPhpConfig(self):
        return Config(self._phpClassToFile, self._getCodeRoot(), 'php')

    def _findClassFileCallback(self, matches):
        self._findClassFileCallbackRun = True
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].getLine(), 'class SimpleClass extends ParentClass {')

    def test_findClassFile(self):
        self._findClassFileCallbackRun = False
        finder = Finder(self._getPhpConfig(), 'extends ParentClass', self._findClassFileCallback)
        finder.join(5)
        self.assertTrue(self._findClassFileCallbackRun, 'Something failed running finder')


if __name__ == '__main__':
    unittest.main()
