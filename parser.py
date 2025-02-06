from _ast import UnaryOp

from tokens import Token, TOK_PLUS, TOK_SLASH, TOK_STAR, TOK_NOT, TOK_MINUS, TOK_INTEGER, TOK_FLOAT, TOK_LPAREN, \
    TOK_RPAREN
from model import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def advance(self):
        self.current += 1

    def peek(self):
        if self.current >= len(self.tokens):
            raise EOFError
        return self.tokens[self.current]


    def is_next(self, expected_type):
        if self.current + 1 >= len(self.tokens):
            return False
        return isinstance(self.tokens[self.current + 1], expected_type)


    def expect(self, expected_type):
        if self.current >= len(self.tokens):
            return False
        return isinstance(self.tokens[self.current], expected_type)


    def match(self, expected_type):
        if self.current >= len(self.tokens):
            return False
        return self.tokens[self.current] if isinstance(self.tokens[self.current], expected_type) else False


    def previous_token(self):
        if self.current > 0:
            return self.tokens[self.current - 1]


    # <primary>  ::=  <integer> | <float> | '(' <expr> ')'
    def primary(self):
        if self.match(TOK_INTEGER): return Integer(int(self.previous_token().lexeme))
        if self.match(TOK_FLOAT): return Float(float(self.previous_token().lexeme))
        if self.match(TOK_LPAREN):
            expr = self.expr()
            if not self.match(TOK_RPAREN):
                raise SyntaxError(f'Error: ")" expected.')
            else:
                return Grouping(expr)


    # <unary>  ::=  ('+'|'-'|'~') <unary>  |  <primary>
    def unary(self):
        if self.match(TOK_NOT) or self.match(TOK_MINUS) or self.match(TOK_MINUS):
            op = self.previous_token()
            operand = self.unary()
            return UnaryOp(op, operand)
        return self.primary()


    def factor(self):
        return self.unary()


    # <term>  ::=  <factor> ( ('*'|'/') <factor> )*
    def term(self):
        expr = self.factor()
        while self.match(TOK_STAR) or self.match(TOK_SLASH):
            op = self.previous_token()
            right = self.factor()
            expr = BinOp(op, expr, right)
        return expr


    # <expr>  ::=  <term> ( ('+'|'-') <term> )*
    def expr(self):
        expr = self.term()
        while self.match(TOK_PLUS) or self.match(TOK_SLASH):
            op = self.previous_token()
            right = self.term()
            expr = BinOp(op, expr, right)
        return expr


    def parse(self):
        ast = self.expr()
        return ast
