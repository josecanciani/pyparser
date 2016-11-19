import unittest
from os import path
import pprint
from shell.command import *

class TestClassCommand(unittest.TestCase):

    def _getPrinter(self):
        return pprint.PrettyPrinter(indent = 2)

    def _dummyCallback(self):
        """ this method should never be called"""

    def _lsRootCallback(self, stdout, stderr):
        self._lsRootCallbackRun = True

    def test_lsRoot(self):
        self._lsRootCallbackRun = False
        command = Command('ls', '/', self._lsRootCallback)
        command.join(5)
        self.assertTrue(self._lsRootCallbackRun, 'Something failed running "ls /" command')

    def _osErrorCallback(self, osErrorException):
        self.assertTrue(isinstance(osErrorException, OSError))
        self._osErrorCallbackRun = True

    def test_osError(self):
        self._osErrorCallbackRun = False
        command = Command('ls', '/invalidDir12345', self._dummyCallback, self._osErrorCallback)
        command.join(5)
        self.assertTrue(self._osErrorCallbackRun, 'Something failed running "ls /invalidDir12345" command')

    def _stdErrCallback(self, stdout, stderr):
        self.assertEqual(stdout, 'this should be stdout')
        self.assertEqual(stderr, 'this should be stderr')
        self._stdErrCallbackRun = True

    def test_stdErr(self):
        self._stdErrCallbackRun = False
        testCommand = path.join(path.dirname(path.realpath(__file__)), '..', 'RESOURCE', 'testCommandOutput.sh')
        command = Command(testCommand, '/', self._stdErrCallback)
        command.join(5)
        self.assertTrue(self._stdErrCallbackRun, 'Something failed running "ls /" command')

if __name__ == '__main__':
    unittest.main()
