
from file.pfile import fromFile, FileDoesNotExists, LanguageNotSupported
from os import path

class Config(object):
    def __init__(self, classToFileCallback, codeRoot):
        self.classToFileCallback = classToFileCallback
        if not path.isdir(codeRoot):
            raise DirectoryDoesNotExists(codeRoot)
        self.codeRoot = codeRoot
    def getFileForClassName(self, className, namespace):
        filePath = self.classToFileCallback(className, namespace)
        if filePath:
            try:
                return fromFile(filePath)
            except (FileDoesNotExists, LanguageNotSupported):
                pass
        return None

class DirectoryDoesNotExists(IOError):
    def __init__(self, path):
        self.path = path
    def __str__(self):
        return repr(self.path)
