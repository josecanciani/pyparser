
class ClassInspector(object):
    def __init__(self, config, className, namespace):
        self.className = className
        self.namespace = namespace
        self.config = config
    def getInstanceMethods(self):
        file = self.config.getFileForClassName(self.className, self.namespace)
        parsedClass = file.getClass(self.className)
        methods = parsedClass.getMethods()
        return methods

