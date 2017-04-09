# pyparser

Python simple code parser

The objective of this project is to provide a quick and live (no indexed code) parsing of code files.

The first implementation will be used to navigate code in Sublime Text.

# Usage

I started this project to split language parsing logic out of my employers plugin for Sublime text. So of course there's a Sublime plugin you can use to get the benefits of this parser: https://github.com/josecanciani/sublimepyparser. But you can just use it in your projects directly, and here follows some hints.

Since there's no index to match files to classes, a Config object is needed, so you can define how to convert a class name to a file path.

```python
from pyparser.config import Config
from pyparser.navigator.classinspector import ClassInspector

def _phpClassToFile(self, className, lang, namespace):
    """ Converts any class name into a file path where to find it"""
    return os.path.dirname(os.path.realpath(__file__)) + '/../classes/' + className.replace('_', '/') + '.php'

config = Config(_phpClassToFile, '/path/to/your/code/root', 'php')
inspector = ClassInspector(config, 'MyClassNameToInsect')

""" This will give you all methods you can access from MyClassNameToInsect (anything you can use from "$this->")"""
thisMethods = inspector.getInstanceMethods()

""" This returns a raw class (pclass) object """
myClass = inspector.getClass()
```

# About pclass and pfile file names

A "p" prefix was added to avoid using a reserved word.

```
    from file.file import *
ImportError: No module named file
```

# About code parsing

Since we want this code to be fast and work with "broken" -when editing a file that may not even be saved to disk-, we don't use any complex lexical parser.
Instead we just parse the file using rudimentary string processing and some regexps, so we expect the code to be somewhat cleaned:

* indentation is key to identify when a class or method ends

    Good:
    ```php
    function myFunc() {
        ...
    }
    ```

    Bad:
    ```php
    function myFunc() {
        ...
        }
    ```

* method definition cannot span to multiple rows:

    Good:
    ```php
    function myFunc($myPar1, $myPar2) {
    ```

    Bad:
    ```php
    function myFunc(
        $myPar1,
        $myPar2
    ) {
    ```

* For .js files, methods starting with underscore (_) are considered private


# Language support

For now we support EMCA JS (.js files) and PHP (.php).

PHP namespaces are not supported at this time


# Class to file

Since the main objetive is speed and live parsing, we don't create indexes. So we need to be able to translate class names to files, in order to be able to navigate code.

This translation depends on how your code is organized, so you need to provide a callback that will be in charge of the translation.

    ```python
    def classToFile(className, lang, namespace):
        'your code here'
        return filePath
    ```

Note that namespaces are not supported, but may in the future. you need to return an absolute path of the file containing that class.


# Unit testing

Run this on the project parent's folder:

$ python -m unittest discover pyparser/

# Projects using pyparser

* Sublime's pyparser: https://github.com/josecanciani/sublimepyparser Usage the fast parsing capabilities of this library in Sublime Text editor.


