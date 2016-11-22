from file.pfile import ClassDoesNotExists

class ClassInspector(object):
    def __init__(self, config, className, namespace = None):
        self.className = className
        self.namespace = namespace
        self.config = config

    def getClass(self, className = None, namespace = None):
        searchClassName = className if className is not None else self.className
        searchNamespace = namespace if className is not None else self.namespace
        try:
            file = self.config.getFileForClassName(searchClassName, searchNamespace)
            return file.getClass(searchClassName)
        except ClassDoesNotExists:
            return None

    def getInstanceMethods(self):
        parsedClass = self.getClass(self.className, self.namespace)
        if parsedClass:
            methods = parsedClass.getMethods()
            return self._addParentMethodsRecursively(parsedClass, methods)
        else:
            return []

    def _addParentMethodsRecursively(self, fromClass, methods):
        className = fromClass.getExtendsFromName()
        if className:
            parsedClass = self.getClass(className, None)
            if parsedClass:
                for method in parsedClass.getInstanceMethods():
                    if not self._isMethodAdded(method, methods):
                        methods.append(method)
                return self._addParentMethodsRecursively(parsedClass, methods)
        return methods

    def _isMethodAdded(self, newMethod, methods):
        for method in methods:
            if method.getName() == newMethod.getName():
                return True
        return False

