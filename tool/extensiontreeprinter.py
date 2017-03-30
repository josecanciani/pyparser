
from navigator.classinspector import ClassInspector
from navigator.extensionfinder import ExtensionFinder

class ExtensionTreePrinter(object):
    def __init__(self, config, className, onComplete, onErrorCallback = None):
        self.config = config
        self.className = className
        self.onComplete = onComplete
        self.onErrorCallback = onErrorCallback
        inspector = ClassInspector(self.config, self.className)
        self.pclass = inspector.getClass(className)
        self.thread = ExtensionFinder(self.config, self.pclass, None, self._onResults, self._onError)

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

