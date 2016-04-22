
import os

def fromFile(filePath):
    filename, extension = os.path.splitext(filePath)
    try:
        return File(open(filePath, 'r').read(), extension[1:])
    except IOError:
        raise FileDoesNotExists(filePath)

def fromCode(text, lang):
    return File(text, lang)

class File(object):
    def __init__(self, code, lang):
        self.code = code
        self.lang = lang
        if self.lang not in ('php', 'js'):
            raise LanguageNotSupported(self.lang)
    def getCode(self):
        return self.code
    def getLang(self):
        return self.lang
    def getClasses(self):
        package = 'lang.' + self.getLang() + '.grammar.Class'
        className = 'Extractor'
        Extractor = getattr(__import__(package, fromlist=[className]), className)
        extractor = Extractor(self)
        return extractor.getClasses(self.code)
    def getClass(self, className):
        for parsedClass in self.getClasses():
            if parsedClass.getName() == className:
                return parsedClass
        return None

class FileDoesNotExists(IOError):
    def __init__(self, path):
        self.path = path
    def __str__(self):
        return repr(self.path)

class LanguageNotSupported(Exception):
    def __init__(self, lang):
        self.lang = lang
    def __str__(self):
        return repr(self.lang)
