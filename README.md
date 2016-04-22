# pyparser

Python simple code parser

The objective of this project is to provide a quick and live (no indexed code) parsing of code files.

The first implementation will be used to navigate code in Sublime Text.

# About code parsing

Since we want this code to be fast and work with "broken" -when editing a file that may not even be saved to disk-, we don't use any complex lexical parser.
Instead we just parse the file and we expect the code to be somewhat cleaned:

* indentation is key to identify when a class or method ends

    OK:
    ```PHP
    function myFunc() {
        ...
    }
    ```

    NOK:
    ```
    function myFunc() {
        ...
        }
    ```

* method definition cannot span to multiple rows:

    OK:
    ```
    function myFunc($myPar1, $myPar2) {
    ```

    NOK:
    ```
    function myFunc(
        $myPar1,
        $myPar2
    ) {
    ```

# Unit testing

Run this on the project folder:

$ python -m unittest discover
