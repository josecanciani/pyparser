
import unittest
from pyparser.common.dto import Dto

class TestClassDto(unittest.TestCase):
    def _getTestDto(self):
        attrs = {
            'myfirstattr': 'hola',
            'mysecondattr': 10
        }
        return Dto(attrs)

    def test_settersAndGetters(self):
        dto = self._getTestDto()
        self.assertEqual('hola', dto.myfirstattr)
        self.assertEqual(10, dto.mysecondattr)

    def test_invalidKey(self):
        dto = self._getTestDto()
        def okcallback():
            return dto.myfirstattr
        def errorcallback():
            return dto.invalidkey
        self.assertEqual('hola', okcallback())
        self.assertRaises(KeyError, errorcallback)

if __name__ == '__main__':
    unittest.main()
