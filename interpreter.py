from model import *
from utils import *

TYPE_NUMBER = 'TYPE_NUMBER'
TYPE_STRING = 'TYPE_STRING'
TYPE_BOOL = 'TYPE_BOOL'

class Interpreter:
    def __init__(self):
        pass

    def interpret(self, node):
        if isinstance(node, Integer):
            return TYPE_NUMBER, float(node.value)

        elif isinstance(node, Float):
            return TYPE_NUMBER, float(node.value)

        elif isinstance(node, Grouping):
            return self.interpret(node.value)

        elif isinstance(node, BinOp):
            lefttype, leftval = self.interpret(node.left)
            righttype, rightval = self.interpret(node.right)
            if node.op.token_type == TOK_PLUS:
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return leftval + rightval
                elif lefttype == TYPE_STRING and righttype == TYPE_STRING:
                    return TYPE_STRING, str(leftval) + str(rightval)
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.', node.op.line)
            elif node.op.token_type == TOK_MINUS:
                return leftval - rightval
            elif node.op.token_type == TOK_STAR:
                return leftval * rightval
            elif node.op.token_type == TOK_SLASH:
                return leftval / rightval

        elif isinstance(node, UnOp):
            if node.op.token_type == TOK_PLUS:
                return +self.interpret(node.operand)
            elif node.op.token_type == TOK_MINUS:
                return -self.interpret(node.operand)
            # elif node.op.token_type == TOK_NOT:
            #     return not self.interpret(node.operand)