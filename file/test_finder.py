
import unittest
from os import path
from pyparser.config import Config
from pyparser.file.finder import Finder

class TestClassFinderConstructor(unittest.TestCase):

    def _getCodeRoot(self):
        return path.dirname(path.realpath(__file__)) + '/../RESOURCE'

    def _findClassFileCallback(self, matches):
        self._findClassFileCallbackRun = True
        self.assertEqual(len(matches), 3)
        matches.sort(key = lambda x: x.getLine())
        self.assertEqual(matches[0].getLine(), 'class SimpleClass extends ParentClass {')
        self.assertEqual(matches[1].getLine(), 'class SimpleClass2 extends ParentClass {')
        self.assertEqual(matches[2].getLine(), 'class ZSimpleClass extends ParentClass {')

    def _findClassFileErrorCallback(self, exception):
        raise exception

    def test_findClassFile(self):
        self._findClassFileCallbackRun = False
        finder = Finder('extends ParentClass', self._getCodeRoot(), 'php', self._findClassFileCallback, self._findClassFileErrorCallback)
        finder.join(5)
        self.assertTrue(self._findClassFileCallbackRun, 'Something failed running finder')


if __name__ == '__main__':
    unittest.main()
