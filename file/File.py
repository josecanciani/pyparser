
import os

def fromFile(filePath):
    filename, extension = os.path.splitext(filePath)
    try:
        return File(open(filePath, 'r').read(), extension[1:])
    except IOError:
        raise FileDoesNotExists(filePath)

def fromCode(text, lang, currentLine):
    return File(text, lang, currentLine)

class File(object):
    def __init__(self, code, lang, currentLine = 0):
        self.code = code
        self.lang = lang
        self.currentLineNumber = currentLine
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
        raise ClassDoesNotExists(className)
    def getCurrentClass(self):
        for parsedClass in self.getClasses():
            if self.currentLineNumber >= parsedClass.getStartLineNumber() and self.currentLineNumber <= parsedClass.getLastLineNumber():
                return parsedClass
        raise NoClassInCurrentLine(self.currentLineNumber)
    def getCurrentLineNumber(self):
        return self.currentLineNumber

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

class ClassDoesNotExists(Exception):
    def __init__(self, className):
        self.className = className
    def __str__(self):
        return repr(self.className)

class NoClassInCurrentLine(Exception):
    def __init__(self, lineNumber):
        self.lineNumber = lineNumber
    def __str__(self):
        return repr(self.lineNumber)
