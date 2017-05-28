
import re
from pyparser.grammar.prop import Prop as BaseProp

class Prop(BaseProp):
    @staticmethod
    def getRegex():
        return r"^[a-z][a-zA-Z0-9-_]*$"
