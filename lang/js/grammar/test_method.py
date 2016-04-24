
import unittest
import os
import pprint
from lang.js.grammar.class import Class, Extractor as ClassExtractor
from lang.js.grammar.method import Extractor as MethodExtractor
from file.file import fromCode
from grammar.class import NoMethodInCurrentLine

class TestClass(unittest.TestCase):

    def test_extract(self):
        classCode = '\nclass HelloWorld {\n   myFunc() {\n        echo "hola mundo";\n   }\n}\n'
        methodCode = '   myFunc() {\n        echo "hola mundo";\n   }\n'
        myFunc = self._getMethodFromClassCode(classCode)
        self.assertEqual('myFunc', myFunc.getName())
        self.assertEqual(methodCode, myFunc.getCode())
        self.assertEqual('HelloWorld', myFunc.getClass().getName())

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

    def test_getLineNumbers(self):
        code = '\nclass MyClass {\n\n   myFunc() {\n        var pp = "hola mundo";\n   }\n}\n'
        file = fromCode(code, 'js', 4)
        myClass = file.getCurrentClass()
        self.assertEqual('MyClass', myClass.getName())
        self.assertEqual(3, myClass.getCurrentLineNumber())
        myFunc = myClass.getCurrentMethod()
        self.assertEqual('myFunc', myFunc.getName())
        self.assertEqual(1, myFunc.getCurrentLineNumber())
        try:
            fromCode(code, 'js', 1).getCurrentClass().getCurrentMethod()
            self.assertTrue(false, 'Expecting NoMethodInCurrentLine exception, should not be here')
        except NoMethodInCurrentLine as e:
            self.assertEqual('0', str(e))

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
