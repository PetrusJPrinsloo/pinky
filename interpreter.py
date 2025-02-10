from model import *

class Interpreter:
    def __init__(self):
        pass

    def interpret(self, node):
        if isinstance(node, Integer):
            return float(node.value)

        elif isinstance(node, Float):
            return float(node.value)

        elif isinstance(node, Grouping):
            return self.interpret(node.value)

        elif isinstance(node, BinOp):
            if node.op.token_type == TOK_PLUS:
                return self.interpret(node.left) + self.interpret(node.right)
            elif node.op.token_type == TOK_MINUS:
                return self.interpret(node.left) - self.interpret(node.right)
            elif node.op.token_type == TOK_STAR:
                return self.interpret(node.left) * self.interpret(node.right)
            elif node.op.token_type == TOK_SLASH:
                return self.interpret(node.left) / self.interpret(node.right)

        elif isinstance(node, UnOp):
            if node.op.token_type == TOK_PLUS:
                return +self.interpret(node.operand)
            elif node.op.token_type == TOK_MINUS:
                return -self.interpret(node.operand)
            # elif node.op.token_type == TOK_NOT:
            #     return not self.interpret(node.operand)