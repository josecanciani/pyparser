import threading
import subprocess

class Command(object):
    def __init__(self, command, path, callback, errorCallback):
        self.command = command if isinstance(command, list) else command.split()
        self.path = path
        self.callback = callback
        self.errorCallback = errorCallback
        self.thread = threading.Thread(target = self._thread)
        self.thread.start()

    def _thread(self):
        try:
            process = subprocess.Popen(self.command, cwd = self.path, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
            stdout, stderr = process.communicate()
            decodedStdout = stdout.decode("UTF-8")
            decodedStderr = stderr.decode("UTF-8")
        except OSError as e:
            self.errorCallback(e)
            return
        except Exception as e:
            self.errorCallback(UknownException(str(e)))
            return
        self.callback(decodedStdout, decodedStderr)

    def join(self, timeout=None):
        return self.thread.join(timeout) if self.thread else None

class UknownException(RuntimeError):
    pass
