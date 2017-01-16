
import unittest
from lang.php.discover.statement import Statement

class TestClass(unittest.TestCase):
    def test_extractClassVar(self):
        code = '\nclass HelloWorld {\n   function myFunc() {\n        $this->he;\n   }\n}\n'
        stmt = Statement(code, code.find('he') + 2)
        self.assertEqual('$this->he', stmt.get())
    def test_extractClassMethod(self):
        code = '\nclass HelloWorld {\n   function myFunc() {\n        $this->hello();\n   }\n}\n'
        stmt = Statement(code, code.find('he') + 2)
        self.assertEqual('$this->hello(', stmt.get())
    def test_extractVariable(self):
        code = '\nclass HelloWorld {\n   function myFunc() {\n        $hello = "hola";\n   }\n}\n'
        stmt = Statement(code, code.find('he') + 2)
        self.assertEqual('$hello', stmt.get())
    def test_extractClassStaticMethod(self):
        code = '\nclass HelloWorld {\n   function myFunc() {\n        MyClass::hello();\n   }\n}\n'
        stmt = Statement(code, code.find('he') + 2)
        self.assertEqual('MyClass::hello(', stmt.get())


if __name__ == '__main__':
    unittest.main()