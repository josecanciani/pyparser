from file.finder import Finder
from file.pfile import fromFile
from common.dto import Dto

class ExtensionFinder(object):
    def __init__(self, config, pclass, options, callback, errorCallback):
        self.config = config
        self.pclass = pclass
        self.callback = callback
        self.errorCallback = errorCallback
        self.options = options if options else Options()
        self.results = []
        self.recursiveException = None
        nameRegex = pclass.getRegexForValidCharactersInName()
        regex = 'class\s+[' + nameRegex + ']+\s+extends\s+' + self.pclass.getName() + '[^' + nameRegex + ']{1}'
        self.thread = Finder(regex, self.config.getCodeRoot(), self.pclass.getExtension(), self._onFindResults, self._onError)

    def join(self, timeout=None):
        return self.thread.join(timeout) if self.thread else None

    def _onFindResults(self, findResults):
        self.thread = None
        for result in findResults:
            file = fromFile(result.getFile())
            for pclass in file.getClasses():
                className = pclass.getExtendsFromName()
                if className and className == self.pclass.getName():
                    self.results.append(pclass)
                    if self.options.recursive:
                        finder = ExtensionFinder(self.config, pclass, self.options, self._onRecursiveFindResults, self._onRecursiveError)
                        finder.join() # avoid running rgrep in parallel
            if self.recursiveException:
                self._onError(self.recursiveException)
                return
        self.callback(self.results)

    def _onError(self, exception):
        self.thread = None
        self.errorCallback(exception)

    def _onRecursiveFindResults(self, results):
        self.results += results

    def _onRecursiveError(self, err):
        self.recursiveException = err

class Options(Dto):
    def __init__(self):
        super(Options, self).__init__({
            'recursive': True
        })
