from file.pfile import File
from shell.command import Command

class Finder(object):
    def __init__(self, pattern, path, fileExtension, callback, errorCallback):
        self.callback = callback
        self.errorCallback = errorCallback
        command = ['rgrep', '-E', pattern, path]
        if fileExtension:
            command.append('--include=*.' + fileExtension)
        self.thread = Command(command, path, self._matchCallback, self._errorCallback)

    def join(self, timeout=None):
        return self.thread.join(timeout) if self.thread else None

    def _matchCallback(self, stdout, stderr):
        self.thread = None
        if not stdout.strip():
            self.callback([])
            return
        results = []
        for line in stdout.splitlines():
            data = line.split(':', 1)
            results.append(FileResult(data[0], data[1]))
        self.callback(results)

    def _errorCallback(self, exception):
        self.thread = None
        self.errorCallback(exception)


class FileResult(object):
    def __init__(self, file, line):
        self.file = file
        self.line = line
    def getFile(self):
        return self.file
    def getLine(self):
        return self.line
