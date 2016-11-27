
class Dto(object):
    def __init__(self, attrDict):
        for attr in attrDict:
            self._setValue(attr, attrDict[attr])

    def __getattr__(self, attr):
        if not hasattr(self, attr):
            raise KeyError
        return self.__dict__[attr]

    def __setattr__(self, attr, value):
        if not hasattr(self, attr):
            raise KeyError
        self._setValue(attr, value)

    def _setValue(self, attr, value):
        self.__dict__[attr] = value
