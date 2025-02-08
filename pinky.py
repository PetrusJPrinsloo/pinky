import sys

from parser import Parser
from tokens import *
from lexer import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit("Usage: pinky <filename>")
    filename = sys.argv[1]
    print(filename)

    with open(filename) as file:
        source = file.read()

        print("LEXER:")
        toks = Lexer(source).tokenize()
        for tok in toks:
            print(tok)

        print("PARSED AST:")
        ast = Parser(toks).parse()
        print(ast)