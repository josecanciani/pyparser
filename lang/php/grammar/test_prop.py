
import unittest
import os
import pprint
from pyparser.lang.php.grammar.pclass import Class, Extractor as ClassExtractor
from pyparser.lang.php.grammar.prop import Extractor as PropExtractor
from pyparser.file.pfile import fromCode
from pyparser.grammar.pclass import NoMethodInCurrentLine

class TestClass(unittest.TestCase):

    def test_extract(self):
        classCode = '\nclass HelloWorld {\n   $publicVar = 1;\n\n}\n'
        propertyCode = '   $publicVar = 1;\n'
        myProp = self._getPropertiesFromClassCode(classCode)
        self.assertEqual('publicVar', myProp.getName())
        self.assertEqual(propertyCode, myProp.getCode())
        self.assertEqual('HelloWorld', myProp.getClass().getName())

    def test_keywords(self):
        classCode = '\nclass HelloWorld {\n    $pp = "hola";\n}\n'
        testKeywords = ['', 'private', 'protected', 'public', 'static', 'const', 'static private', 'static protected', 'static public']
        steps = {}
        for prefix in testKeywords:
            prefixedClassCode = classCode.replace('$pp', prefix + ' $pp') if prefix else classCode
            myProp = self._getPropertiesFromClassCode(prefixedClassCode)
            if 'protected' in prefix.split(' '):
                steps['step1'] = True
                self.assertTrue(myProp.isProtected())
                self.assertFalse(myProp.isPrivate())
                self.assertFalse(myProp.isPublic())
                self.assertFalse(myProp.isConstant())
            else:
                steps['step2'] = True
                self.assertTrue((myProp.isPrivate() and not myProp.isPublic()) or (myProp.isPublic() and not myProp.isPrivate()) or myProp.isContant())
            if 'public' in prefix.split(' ') or ('private' not in prefix.split(' ') and 'protected' not in prefix.split(' ')):
                steps['step3'] = True
                self.assertTrue(myProp.isPublic())
                self.assertFalse(myProp.isProtected())
                self.assertFalse(myProp.isPrivate())
            else:
                steps['step4'] = True
                self.assertFalse(myProp.isPublic())
                self.assertTrue((myProp.isPrivate() and not myProp.isProtected()) or (myProp.isProtected() and not myProp.isPrivate()) or myProp.isConstant())
            if 'static' in prefix.split(' '):
                steps['step5'] = True
                self.assertTrue(myProp.isStatic())
            else:
                steps['step6'] = True
                self.assertFalse(myProp.isStatic())
            if 'const' in prefix.split(' '):
                steps['step7'] = True
                self.assertTrue(myProp.isConstant())
            else:
                steps['step8'] = True
                self.assertFalse(myProp.isConstant())
        self.assertEqual(8, len(steps.keys()), 'Not all combinations of property keywords had been tested')

    def test_extractNotConfusingMethods(self):
        code = '\nclass MyClass {\n\n   function myMethod() {\n      private $pp = null;\n   }\n   $myProp = "hola";\n}\n'
        file = fromCode(code, 'php', 4)
        myClass = file.getCurrentClass()
        self.assertEqual('MyClass', myClass.getName())
        self.assertEqual(3, myClass.getCurrentLineNumber())
        self.assertEqual(1, len(myClass.getMethods()), 'One method should be found')
        self.assertEqual(1, len(myClass.getProperties()), 'One property should be found')
        self.assertEqual('myMethod', myClass.getMethods()[0].getName())
        self.assertEqual('myProp', myClass.getProperties()[0].getName())

    def _getPropertiesFromClassCode(self, code):
        classExtractor = ClassExtractor()
        classes = classExtractor.getClasses(code)
        self.assertTrue(len(classes) > 0, 'Cannot find classes in code: \n' + code)
        propExtractor = PropExtractor(classes[0])
        properties = propExtractor.getProperties()
        self.assertTrue(len(properties) > 0, 'Cannot find properties in class code: \n' + code)
        return properties[0]


if __name__ == '__main__':
    unittest.main()
