from model import *
from state import Environment
from utils import *
import codecs


TYPE_NUMBER = 'TYPE_NUMBER'
TYPE_STRING = 'TYPE_STRING'
TYPE_BOOL = 'TYPE_BOOL'

class Interpreter:
    def __init__(self):
        pass

    def interpret(self, node, env):
        if isinstance(node, Integer):
            return TYPE_NUMBER, float(node.value)

        elif isinstance(node, Float):
            return TYPE_NUMBER, float(node.value)

        elif isinstance(node, Bool):
            return TYPE_BOOL, node.value

        elif isinstance(node, String):
            return TYPE_STRING, str(node.value)

        elif isinstance(node, Grouping):
            return self.interpret(node.value, env)

        elif isinstance(node, Identifier):
            value = env.get_var(node.name)
            if value is None:
                runtime_error(f'Undeclared identifier {node.name!r}', node.line)
            if value[1] is None:
                runtime_error(f'Uninitialized identifier {node.name!r}', node.line)
            return value


        if isinstance(node, Assignment):
            """
            Left := Right
            """
            # Evaluate the right-hand side expression
            righttype, rightval = self.interpret(node.right, env)
            # Update the value of the left-hand side variable or create a new one
            env.set_var(node.left.name, (righttype, rightval))


        elif isinstance(node, BinOp):
            lefttype, leftval = self.interpret(node.left, env)
            righttype, rightval = self.interpret(node.right, env)
            if node.op.token_type == TOK_PLUS:
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return TYPE_NUMBER, leftval + rightval
                elif lefttype == TYPE_STRING or righttype == TYPE_STRING:
                    return TYPE_STRING, str(leftval) + str(rightval)
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.', node.op.line)
            elif node.op.token_type == TOK_MINUS:
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return TYPE_NUMBER, leftval - rightval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.', node.op.line)
            elif node.op.token_type == TOK_STAR:
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return TYPE_NUMBER, leftval * rightval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.', node.op.line)
            elif node.op.token_type == TOK_SLASH:
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return TYPE_NUMBER, leftval / rightval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.', node.op.line)
            elif node.op.token_type == TOK_MOD:
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return TYPE_NUMBER, leftval % rightval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.', node.op.line)
            elif node.op.token_type == TOK_CARET:
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return TYPE_NUMBER, leftval ** rightval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.', node.op.line)

            elif node.op.token_type == TOK_GT:
                if (lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER) or (
                        lefttype == TYPE_STRING and righttype == TYPE_STRING):
                    return TYPE_BOOL, leftval > rightval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.',node.op.line)

            elif node.op.token_type == TOK_GE:
                if (lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER) or (
                        lefttype == TYPE_STRING and righttype == TYPE_STRING):
                    return TYPE_BOOL, leftval >= rightval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.', node.op.line)

            elif node.op.token_type == TOK_LT:
                if (lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER) or (
                        lefttype == TYPE_STRING and righttype == TYPE_STRING):
                    return TYPE_BOOL, leftval < rightval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.', node.op.line)

            elif node.op.token_type == TOK_LE:
                if (lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER) or (
                        lefttype == TYPE_STRING and righttype == TYPE_STRING):
                    return TYPE_BOOL, leftval <= rightval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.', node.op.line)

            elif node.op.token_type == TOK_EQEQ:
                if (lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER) or (
                        lefttype == TYPE_STRING and righttype == TYPE_STRING) or (
                        lefttype == TYPE_BOOL and righttype == TYPE_BOOL):
                    return TYPE_BOOL, leftval == rightval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.', node.op.line)

            elif node.op.token_type == TOK_NE:
                if (lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER) or (
                        lefttype == TYPE_STRING and righttype == TYPE_STRING) or (
                        lefttype == TYPE_BOOL and righttype == TYPE_BOOL):
                    return TYPE_BOOL, leftval != rightval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} between {lefttype} and {righttype}.', node.op.line)

        elif isinstance(node, UnOp):
            operandtype, operandval = self.interpret(node.operand, env)
            if node.op.token_type == TOK_PLUS:
                if operandtype == TYPE_NUMBER:
                    return TYPE_NUMBER, +operandval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} with {operandtype}.', node.op.line)
            elif node.op.token_type == TOK_MINUS:
                if operandtype == TYPE_NUMBER:
                    return TYPE_NUMBER, -operandval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} with {operandtype}.', node.op.line)
            elif node.op.token_type == TOK_NOT:
                if operandtype == TYPE_BOOL:
                    return TYPE_BOOL, not operandval
                else:
                    runtime_error(f'Unsupported operator {node.op.lexeme!r} with {operandtype}.', node.op.line)

        elif isinstance(node, LogicalOp):
            lefttype, leftval = self.interpret(node.left, env)
            if node.op.token_type == TOK_OR:
                if leftval:
                    return lefttype, leftval
            elif node.op.token_type == TOK_AND:
                if not leftval:
                    return lefttype, leftval
            return self.interpret(node.right, env)

        elif isinstance(node, Stmts):
            for stmt in node.stmts:
                self.interpret(stmt, env)

        elif isinstance(node, PrintStmt):
            exprtype, exprval = self.interpret(node.value, env)
            print(codecs.escape_decode(bytes(str(exprval), "utf-8"))[0].decode("utf-8"), end=node.end)

        elif isinstance(node, IfStmt):
            testtype, testval = self.interpret(node.test, env)
            if testtype != TYPE_BOOL:
                runtime_error("Condition test is not a boolean expression", node.line)
            if testval:
                self.interpret(node.then_stmts, env.new_env())
            else:
                self.interpret(node.else_stmts, env.new_env())

        elif isinstance(node, WhileStmt):
            new_env = env.new_env()
            while True:
                testtype, testval = self.interpret(node.test, env)
                if testtype != TYPE_BOOL:
                    runtime_error(f"While test is not a boolean expression", node.line)
                if not testval:
                    break
                self.interpret(node.do_stmts, new_env)



    def interpret_ast(self, node):
        env = Environment()
        self.interpret(node, env)
