
import unittest
import os
import pprint
from lang.php.grammar.Class import Class, Extractor as ClassExtractor
from lang.php.grammar.Method import Extractor as MethodExtractor

class TestClass(unittest.TestCase):

    def test_extract(self):
        classCode = '\nclass HelloWorld {\n   function myFunc() {\n        echo "hola mundo";\n   }\n}\n'
        methodCode = '   function myFunc() {\n        echo "hola mundo";\n   }\n'
        myFunc = self._getMethodFromClassCode(classCode)
        self.assertEqual('myFunc', myFunc.getName())
        self.assertEqual(methodCode, myFunc.getCode())
        self.assertEqual('HelloWorld', myFunc.getClass().getName())

    def test_keywords(self):
        classCode = '\nclass HelloWorld {\n    function myFunc() {\n        echo "hola mundo";\n    }\n}\n'
        testKeywords = ['', 'private', 'protected', 'public', 'static', 'static public', 'static private', 'static']
        steps = {}
        for prefix in testKeywords:
            prefixedClassCode = classCode.replace('function', prefix + ' function') if prefix else classCode
            myFunc = self._getMethodFromClassCode(prefixedClassCode)
            if 'protected' in prefix.split(' '):
                steps['step1'] = True
                self.assertTrue(myFunc.isProtected())
                self.assertFalse(myFunc.isPrivate())
                self.assertFalse(myFunc.isPublic())
            else:
                steps['step2'] = True
                self.assertTrue((myFunc.isPrivate() and not myFunc.isPublic()) or (myFunc.isPublic() and not myFunc.isPrivate()))
            if 'public' in prefix.split(' ') or ('private' not in prefix.split(' ') and 'protected' not in prefix.split(' ')):
                steps['step3'] = True
                self.assertTrue(myFunc.isPublic())
                self.assertFalse(myFunc.isProtected())
                self.assertFalse(myFunc.isPrivate())
            else:
                steps['step4'] = True
                self.assertFalse(myFunc.isPublic())
                self.assertTrue((myFunc.isPrivate() and not myFunc.isProtected()) or (myFunc.isProtected() and not myFunc.isPrivate()))
            if 'static' in prefix.split(' '):
                steps['step5'] = True
                self.assertTrue(myFunc.isStatic())
            else:
                steps['step6'] = True
                self.assertFalse(myFunc.isStatic())
        self.assertEqual(6, len(steps.keys()), 'Not all combinations of method keywords had been tested')

    def _getMethodFromClassCode(self, code):
        classExtractor = ClassExtractor()
        classes = classExtractor.getClasses(code)
        self.assertTrue(len(classes) > 0, 'Cannot find classes in code: \n' + code)
        methodExtractor = MethodExtractor(classes[0])
        methods = methodExtractor.getMethods()
        self.assertTrue(len(methods) > 0, 'Cannot find methods in class code: \n' + code)
        return methods[0]


if __name__ == '__main__':
        unittest.main()
