from tokens import Token
from model import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def primary(self):
        pass

    def unary(self):
        pass

    def factor(self):
        pass

    def term(self):
        pass

    def expr(self):
        pass

    def parse(self):
        ast = self.expr()
        return ast