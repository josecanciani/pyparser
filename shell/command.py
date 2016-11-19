import threading
import subprocess

class Command(object):
    def __init__(self, command, path, callback, errorCallback = None):
        self.command = command if isinstance(command, list) else command.split()
        self.path = path
        self.callback = callback
        self.errorCallback = errorCallback
        self.thread = threading.Thread(target=self._thread)
        self.thread.start()
    def _thread(self):
        try:
            process = subprocess.Popen(self.command, cwd = self.path, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
            stdout, stderr = process.communicate()
            decodedStdout = stdout.decode("UTF-8")
            decodedStderr = stderr.decode("UTF-8")
            self.callback(decodedStdout, decodedStderr)
        except OSError as e:
            if self.errorCallback:
                self.errorCallback(e)
            else:
                raise e
    def join(self, timeout=None):
        return self.thread.join(timeout)
