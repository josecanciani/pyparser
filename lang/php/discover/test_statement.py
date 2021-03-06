
import unittest
from pyparser.lang.php.discover.statement import Statement

class TestClass(unittest.TestCase):
    def _checkCurrentPositionType(self, statement, isVariableExpected):
        self.assertEqual(isVariableExpected, statement.isCurrentPositionAVariable())
    def test_extractClassVar(self):
        code = '\nclass HelloWorld {\n   function myFunc() {\n        $this->he;\n   }\n}\n'
        stmt = Statement(code, code.find('he') + 2)
        self.assertEqual('$this->he', stmt.get())
        self._checkCurrentPositionType(stmt, False)
    def test_extractClassMethod(self):
        code = '\nclass HelloWorld {\n   function myFunc() {\n        $this->hello();\n   }\n}\n'
        stmt = Statement(code, code.find('he') + 2)
        self.assertEqual('$this->hello', stmt.get())
        self._checkCurrentPositionType(stmt, False)
    def test_extractClassMethodX2(self):
        code = '\nclass HelloWorld {\n   function myFunc() {\n        $this->foo()->hello();\n   }\n}\n'
        stmt = Statement(code, code.find('he') + 2)
        self.assertEqual('$this->foo()->hello', stmt.get())
        self._checkCurrentPositionType(stmt, False)
    def test_extractClassMethodX2WithSpaces(self):
        code = '\nclass HelloWorld {\n   function myFunc() {\n        $this\n->foo () ->hello();\n   }\n}\n'
        stmt = Statement(code, code.find('he') + 2)
        self.assertEqual('$this->foo()->hello', stmt.get())
        self._checkCurrentPositionType(stmt, False)
    def test_extractVariable(self):
        code = '\nclass HelloWorld {\n   function myFunc() {\n        $hello = "hola";\n   }\n}\n'
        stmt = Statement(code, code.find('he') + 2)
        self.assertEqual('$hello', stmt.get())
        self._checkCurrentPositionType(stmt, True)
    def test_extractClassStaticMethod(self):
        code = '\nclass HelloWorld {\n   function myFunc() {\n        MyClass::hello();\n   }\n}\n'
        stmt = Statement(code, code.find('he') + 2)
        self.assertEqual('MyClass::hello', stmt.get())
        self._checkCurrentPositionType(stmt, False)
    def test_extractClassMethodX2WithStringLiterals(self):
        code = '\nclass HelloWorld {\n   function myFunc() {\n        $this->foo("string")->hello();\n   }\n}\n'
        stmt = Statement(code, code.find('he') + 2)
        self.assertEqual('$this->foo("string")->hello', stmt.get())
        self._checkCurrentPositionType(stmt, False)
    def test_variableRegex(self):
        testTrueCases = ("$hola", "$a234", "$holaMundo", "$Hi") # $Hi is debatable: variables should be lowercased
        testFalseCases = ("mundo", "como$estas", "$123")
        for test in testTrueCases:
            stmt = Statement(test, len(test) - 1)
            self.assertEqual(True, stmt.isCurrentPositionAVariable())
        for test in testFalseCases:
            stmt = Statement(test, len(test) - 1)
            self.assertEqual(False, stmt.isCurrentPositionAVariable())
    def test_methodRegex(self):
        testTrueCases = ['$myobject->pepe', '$myobject->_pepe', '$this->object->method', '$myobject->mysubobject->mysubsubobject->method', 'myobject->', 'MyClass::pepe', 'MyClass::', 'static::PEPE', 'self::PEPE']
        testFalseCases = ['$myobject', 'MyClass']
        for test in testTrueCases:
            stmt = Statement(test, len(test) - 1)
            self.assertEqual(True, stmt.isCurrentPositionAClassProperty(), 'expecting class property in : ' + test)
        for test in testFalseCases:
            stmt = Statement(test, len(test) - 1)
            self.assertEqual(False, stmt.isCurrentPositionAClassProperty())


if __name__ == '__main__':
    unittest.main()
