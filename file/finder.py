from file.pfile import File
from shell.command import Command

class Finder(object):
    def __init__(self, config, pattern, callback):
        self.callback = callback
        include = '--include=*.' + config.getLanguageExtension()
        self.command = Command(['rgrep', pattern, config.getCodeRoot(), include], config.getCodeRoot(), self._matchCallback)
    def join(self, timeout=None):
        return self.command.join(timeout)
    def _matchCallback(self, stdout, stderr):
        if not stdout.strip():
            return []
        results = []
        for line in stdout.splitlines():
            data = line.split(':', 1)
            results.append(FileResult(data[0], data[1]))
        self.callback(results)


class FileResult(object):
    def __init__(self, file, line):
        self.file = file
        self.line = line
    def getFile(self):
        return self.file
    def getLine(self):
        return self.line
