from tokens import *


class Node:
    """
    Nodes on the Abstract Syntax Tree
    """


class Expr(Node):
    """
    Expressions evaluate to a result, like x + (3 * y)
    """


class Stmt(Node):
    """
    Statements perform an action
    """


class Integer(Expr):
    """
    Example: 17
    """

    def __init__(self, value, line):
        assert isinstance(value, int), value
        self.value = value
        self.line = line

    def __repr__(self):
        return f'Integer({self.value})'


class Float(Expr):
    """
    Example: 3.14
    """

    def __init__(self, value, line):
        assert isinstance(value, float), value
        self.value = value
        self.line = line

    def __repr__(self):
        return f'Float({self.value})'


class UnOp(Expr):
    """
    Example: -x
    """

    def __init__(self, op: Token, operand: Expr, line):
        assert isinstance(op, Token), op
        assert isinstance(operand, Expr), operand
        self.op = op
        self.operand = operand
        self.line = line

    def __repr__(self):
        return f'UnOp({self.op.lexeme!r}, {self.operand})'


class BinOp(Expr):
    """
    Example: x + y
    """

    def __init__(self, op: Token, left: Expr, right: Expr, line):
        assert isinstance(op, Token), op
        assert isinstance(left, Expr), left
        assert isinstance(right, Expr), right
        self.op = op
        self.left = left
        self.right = right
        self.line = line

    def __repr__(self):
        return f'BinOp({self.op.lexeme!r}, {self.left}, {self.right})'


class LogicalOp(Expr):
    """
    Example: x and y
    """

    def __init__(self, op: Token, left: Expr, right: Expr, line):
        assert isinstance(op, Token), op
        assert isinstance(left, Expr), left
        assert isinstance(right, Expr), right
        self.op = op
        self.left = left
        self.right = right
        self.line = line

    def __repr__(self):
        return f'LogicalOp({self.op.lexeme!r}, {self.left}, {self.right})'


class Grouping(Expr):
    """
    Example: (expression)
    """

    def __init__(self, value, line):
        assert isinstance(value, Expr), value
        self.value = value
        self.line = line

    def __repr__(self):
        return f'Grouping({self.value})'


class Identifier(Expr):
    """Example: stuff, data, pi, return_val"""
    def __init__(self, name, line):
        isinstance(name, str), name
        self.name = name
        self.line = line
    def __repr__(self):
        return f'Identifier({self.name})'

class Bool(Expr):
    """
    Example: true, false
    """

    def __init__(self, value, line):
        assert isinstance(value, bool), value
        self.value = value
        self.line = line

    def __repr__(self):
        return f'Bool[{self.value}]'


class String(Expr):
    """
    Example: "This is a string"
    """

    def __init__(self, value, line):
        assert isinstance(value, str), value
        self.value = value
        self.line = line

    def __repr__(self):
        return f'String[{self.value}]'


class Stmts(Node):
    """
    A list of statements
    """

    def __init__(self, stmts, line):
        assert all(isinstance(stmt, Stmt) for stmt in stmts), stmts
        self.stmts = stmts
        self.line = line

    def __repr__(self):
        return f'Stmts({self.stmts})'


class While(Stmt):
    pass


class For:
    pass


class PrintStmt(Stmt):
    """
    Example: print value
    """

    def __init__(self, value, end, line):
        assert isinstance(value, Expr), value
        self.value = value
        self.end = end
        self.line = line

    def __repr__(self):
        return f'PrintStmt({self.value}, end={self.end!r})'


class IfStmt(Stmt):
    """
    if <expression> then <then_stmts> (else <else_stmts>)? end
    """
    def __init__(self, test, then_stmts, else_stmts, line):
        assert isinstance(test, Expr), test
        assert isinstance(then_stmts, Stmts), then_stmts
        assert else_stmts is None or isinstance(else_stmts, Stmts), else_stmts
        self.test = test
        self.then_stmts = then_stmts
        self.else_stmts = else_stmts
        self.line = line
    def __repr__(self):
        return f'IfStmt({self.test}, then:{self.then_stmts}, else:{self.else_stmts})'

class Assignment(Stmt):
    """
    left := right
    x := 5 * (7 + 8)
    """
    def __init__(self, left, right, line):
        assert isinstance(left, Expr), left
        assert isinstance(right, Expr), right
        self.left = left
        self.right = right
        self.line = line
    def __repr__(self):
        return f'Assignment({self.left}, {self.right})'
