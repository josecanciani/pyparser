
from pyparser.navigator.classinspector import ClassInspector
from pyparser.navigator.extensionfinder import ExtensionFinder
from pyparser.file.pfile import ClassDoesNotExists

class ExtensionTreePrinter(object):
    def __init__(self, config, className, onComplete, onErrorCallback = None):
        self.config = config
        self.onComplete = onComplete
        self.onErrorCallback = onErrorCallback
        self._setClass(self._getClass(className), className)
        if self.pclass:
            self.thread = ExtensionFinder(self.config, self.pclass, None, self._onResults, self._onError)

    def _getClass(self, className):
        inspector = ClassInspector(self.config, className)
        return inspector.getClass(className)

    def _setClass(self, pclass, className):
        if pclass:
            self.pclass = pclass
        else:
            self._onError(ClassDoesNotExists(className), className)

    def join(self, timeout=None):
        return self.thread.join(timeout) if self.thread else None

    def get(self):
        lifo = [self.pclass]
        indent = 0
        tree = self.pclass.getName() + '\n'
        for pclass in self.results:
            if pclass.getExtendsFromName() == lifo[-1].getName():
                indent += 4
            else:
                lifo[:-1]
                indent -= 4
            lifo.append(pclass)
            tree += ''.rjust(indent,' ') + pclass.getName() + '\n'
        return tree

    def _onResults(self, results):
        self.results = results
        self.onComplete(self)

    def _onError(self, err):
        if self.onErrorCallback:
            self.onErrorCallback(self.err)
        else:
            raise err

class ExtensionFullTreePrinter(ExtensionTreePrinter):
    def _setClass(self, pclass, className):
        self.pclass = self._getTopClass(pclass)

    def _getTopClass(self, pclass):
        parent = self._getClass(pclass.getExtendsFromName()) if pclass.getExtendsFromName() else None
        return self._getTopClass(parent) if parent else pclass
