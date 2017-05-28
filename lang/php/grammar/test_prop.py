
import unittest
import re
from pyparser.lang.php.grammar.prop import Prop

class TestProp(unittest.TestCase):

    def test_regex(self):
        testTrueCases = ("$hola", "$a234", "$holaMundo", "$Hi") # $Hi is debatable: variables should be lowercased
        testFalseCases = ("mundo", "como$estas", "$123")
        for test in testTrueCases:
            self.assertEqual(True, True if re.match(Prop.getRegex(), test, re.MULTILINE) else False)
        for test in testFalseCases:
            self.assertEqual(False, True if re.match(Prop.getRegex(), test, re.MULTILINE) else False)

if __name__ == '__main__':
    unittest.main()
