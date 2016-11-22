from file.finder import Finder
from file.pfile import fromFile

class ExtensionFinder(object):
    def __init__(self, config, pclass, callback, errorCallback):
        self.config = config
        self.pclass = pclass
        self.callback = callback
        self.errorCallback = errorCallback
        nameRegex = pclass.getRegexForValidCharactersInName()
        regex = 'class\s+[' + nameRegex + ']+\s+extends\s+' + self.pclass.getName() + '[^' + nameRegex + ']{1}'
        self.thread = Finder(regex, self.config.getCodeRoot(), self.pclass.getExtension(), self._onFindResults, self._onError)

    def join(self, timeout=None):
        return self.thread.join(timeout) if self.thread else None

    def _onFindResults(self, findResults):
        self.thread = None
        classes = []
        for result in findResults:
            file = fromFile(result.getFile())
            for pclass in file.getClasses():
                className = pclass.getExtendsFromName()
                if className and className == self.pclass.getName():
                    classes.append(pclass)
        self.callback(classes)

    def _onError(self, exception):
        self.thread = None
        self.errorCallback(exception)
