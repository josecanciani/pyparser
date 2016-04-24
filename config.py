
from file.file import fromFile, FileDoesNotExists, LanguageNotSupported

class Config(object):
    def __init__(self, classToFileCallback):
        self.classToFileCallback = classToFileCallback
    def getFileForClassName(self, className, namespace):
        filePath = self.classToFileCallback(className, namespace)
        if filePath:
            try:
                return fromFile(filePath)
            except (FileDoesNotExists, LanguageNotSupported):
                pass
        return None
