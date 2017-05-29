import re

class Statement(object):
    def __init__(self, code, pos):
        self.code = code
        self.pos = pos
        self.statement = self._extract()

    def get(self):
        return self.statement

    def getStopChars(self, isBefore):
        raise NotImplementedError

    def _extract(self):
        statement = ''
        inString = False
        inFunctionParamBlock = 0
        codeLength = len(self.code)
        if self.pos < 0 or self.pos > codeLength:
            return ''
        for i in reversed(range(0, self.pos)):
            letter = self.code[i : i + 1]
            inString = self._assertLiteralString(letter, self.code[i - 1: i] if i > 0 else None, inString)
            inFunctionParamBlock = self._assertInFunctionParamBlock(letter, inString, inFunctionParamBlock)
            if not inString and inFunctionParamBlock == 0 and letter in self.getStopChars(True):
                break
            if not inString and letter.strip() == '':
                continue
            statement += letter
        statement = statement[::-1] # reverse
        if self.code[self.pos : self.pos + 1].strip() == '':
            return statement # we are typing, stop here
        for i in range(self.pos, codeLength):
            letter = self.code[i : i + 1]
            if letter.strip() == '' or letter in self.getStopChars(False):
                break
            else:
                statement += letter
        return statement

    def _processLetter(self, index, isBefore):
        letter = self.code[index : index + 1]
        if letter.strip() == '':
            return ''
        if letter in self.getStopChars(isBefore):
            return False
        return letter

    def _assertLiteralString(self, letter, previousLetter, inString):
        if letter in self.getStringDelimiters():
            if inString:
                if letter == inString and (previousLetter is None or previousLetter != self.getStringDelimiterEscape()):
                    return False # not in string anymore
            else:
                return letter
        return inString

    def _assertInFunctionParamBlock(self, letter, inString, inFunctionParamBlock):
        if inString:
            return inFunctionParamBlock
        if letter == '(' and inFunctionParamBlock > 0:
            return inFunctionParamBlock - 1
        if letter == ')':
            return inFunctionParamBlock + 1
        return inFunctionParamBlock

    def getStringDelimiters(self):
        return ["'", '"']

    def getStringDelimiterEscape(self):
        return '\\'

    def getHelper(self):
        raise NotImplementedError

    def isCurrentPositionAVariable(self):
        return True if re.match(self.getHelper().getVariableRegex(), self.get(), re.MULTILINE) else False
