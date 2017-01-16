
class Statement(object):
    def __init__(self, code, pos):
        self.statement = self._extract(code, pos)

    def get(self):
        return self.statement

    def getStopChars(self, isBefore):
        raise NotImplementedError

    def _extract(self, code, pos):
        statement = ''
        codeLength = len(code)
        if pos < 0 or pos > codeLength:
            return ''
        for i in reversed(range(0, pos)):
            letter = self._processLetter(code, i, True)
            if letter is False:
                break
            else:
                statement += letter
        statement = statement[::-1] # reverse
        if code[pos : pos+1].strip() == '':
            return statement # we are typing, stop here
        for i in range(pos, codeLength):
            letter = self._processLetter(code, i, False)
            if letter is False:
                break
            else:
                statement += letter
        return statement

    def _processLetter(self, code, index, isBefore):
        letter = code[index : index + 1]
        if letter.strip() == '':
            return ''
        if letter in self.getStopChars(isBefore):
            return False
        return letter
