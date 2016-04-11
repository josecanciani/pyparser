
import unittest
import os
import pprint
from lang.js.grammar.Class import Class, Extractor as ClassExtractor
from lang.js.grammar.Method import Extractor as MethodExtractor

class TestClass(unittest.TestCase):

    def test_extract(self):
        classCode = '\nclass HelloWorld {\n   myFunc() {\n        echo "hola mundo";\n   }\n}\n'
        methodCode = '   myFunc() {\n        echo "hola mundo";\n   }\n'
        myFunc = self._getMethodFromClassCode(classCode)
        self.assertEqual('myFunc', myFunc.getName())
        self.assertEqual(methodCode, myFunc.getCode())

    def test_keywords(self):
        classes = [
            {'code': '\nclass HelloWorld {\n    myFunc() {\n        echo "hola mundo";\n    }\n}\n', 'method': 'myFunc'},
            {'code': '\nclass HelloWorld {\n    _myFunc() {\n        echo "hola mundo";\n    }\n}\n', 'method': '_myFunc'}
        ]
        testKeywords = ['', 'static']
        steps = {}
        for c in classes:
            classCode = c['code']
            methodName = c['method']
            for prefix in testKeywords:
                prefixedClassCode = classCode.replace(methodName, prefix + ' ' + methodName) if prefix else classCode
                myFunc = self._getMethodFromClassCode(prefixedClassCode)
                self.assertTrue((myFunc.isPrivate() and not myFunc.isPublic()) or (myFunc.isPublic() and not myFunc.isPrivate()))
                self.assertFalse(myFunc.isProtected())
                if methodName[0] == '_':
                    self.assertTrue(myFunc.isPrivate())
                    self.assertFalse(myFunc.isPublic())
                else:
                    self.assertTrue(myFunc.isPublic())
                    self.assertFalse(myFunc.isPrivate())
                if 'static' in prefix.split(' '):
                    steps['step1'] = True
                    self.assertTrue(myFunc.isStatic())
                else:
                    steps['step2'] = True
                    self.assertFalse(myFunc.isStatic())
            self.assertEqual(2, len(steps.keys()), 'Not all combinations of method keywords had been tested')

    def _getMethodFromClassCode(self, code):
        classExtractor = ClassExtractor()
        classes = classExtractor.getClasses(code)
        self.assertTrue(len(classes) > 0, 'Cannot find classes in code: \n' + code)
        methodExtractor = MethodExtractor()
        methods = methodExtractor.getMethods(classes[0])
        self.assertTrue(len(methods) > 0, 'Cannot find methods in class code: \n' + code)
        return methods[0]


if __name__ == '__main__':
        unittest.main()
