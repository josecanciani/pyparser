
from pyparser.file.pfile import fromFile, FileDoesNotExists, LanguageNotSupported
from os import path

class Config(object):
    def __init__(self, classToFileCallback, codeRoot, lang):
        self.classToFileCallback = classToFileCallback
        if not path.isdir(codeRoot):
            raise DirectoryDoesNotExists(codeRoot)
        self.codeRoot = codeRoot
        self.pyparserRoot = path.dirname(path.realpath(__file__))
        if not path.isdir(path.join(self.pyparserRoot, 'lang', lang)):
            raise LanguageNotSupported(lang)
        self.lang = lang
    def getFileForClassName(self, className, namespace):
        filePath = self.classToFileCallback(className, self.lang, namespace)
        if filePath:
            try:
                return fromFile(filePath)
            except (FileDoesNotExists, LanguageNotSupported):
                pass
        return None
    def getLanguageExtension(self):
        return self.lang
    def getCodeRoot(self):
        return self.codeRoot

class DirectoryDoesNotExists(IOError):
    def __init__(self, path):
        self.path = path
    def __str__(self):
        return repr(self.path)
