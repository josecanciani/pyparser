
from file.File import ClassDoesNotExists

class ClassInspector(object):
    def __init__(self, config, className, namespace):
        self.className = className
        self.namespace = namespace
        self.config = config

    def getInstanceMethods(self):
        parsedClass = self._getClassFromName(self.className, self.namespace)
        methods = parsedClass.getMethods()
        return self._addParentMethodsRecursively(parsedClass, methods)

    def _addParentMethodsRecursively(self, fromClass, methods):
        className = fromClass.getExtendsFromName()
        if className:
            parsedClass = self._getClassFromName(className, None)
            if parsedClass:
                for method in parsedClass.getInstanceMethods():
                    if not self._isMethodAdded(method, methods):
                        methods.append(method)
                return self._addParentMethodsRecursively(parsedClass, methods)
        return methods

    def _getClassFromName(self, className, namespace):
        try:
            file = self.config.getFileForClassName(className, namespace)
            return file.getClass(className)
        except ClassDoesNotExists:
            return None

    def _isMethodAdded(self, newMethod, methods):
        for method in methods:
            if method.getName() == newMethod.getName():
                return True
        return False

