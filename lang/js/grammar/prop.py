
import re
from pyparser.grammar.prop import Prop as BaseProp

class Prop(BaseProp):
    def getRegex(self):
        return r"^[a-z][a-zA-Z0-9-_]*$"
