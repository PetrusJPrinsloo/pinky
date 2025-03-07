import unittest
from utils import *
from tokens import *
from lexer import *
from parser import *
from interpreter import *
import inspect


class TestExpressions(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    def test_number_primary(self):
        source = '''7.7'''
        expected_output = (TYPE_NUMBER, 7.7)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interpreter().interpret(ast)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
