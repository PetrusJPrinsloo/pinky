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

class Decl(Stmt):
    """
    Declarations are statements to declare a new name for something
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


class ForStmt(Stmt):
    """
    "for" <identifier> ":=" <start> "," <end> ("," <step>)? "do" <body_stmts> "end"
    """
    def __init__(self, ident, start, end, step, body_stmts, line):
        assert isinstance(ident, Identifier), ident
        assert isinstance(start, Expr), start
        assert isinstance(end, Expr), end
        assert isinstance(step, Expr) or step is None, step
        assert isinstance(body_stmts, Stmts), body_stmts
        self.ident = ident
        self.start = start
        self.end = end
        self.step = step
        self.body_stmts = body_stmts
        self.line = line


    def __repr__(self):
        return f'ForStmt({self.ident}, {self.start}, {self.end}, {self.step}, {self.body_stmts})'


class PrintStmt(Stmt):
    """
    Example: 'print' value
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
    'if' <expression> 'then' <then_stmts> ( 'else' <else_stmts> )? 'end'
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


class WhileStmt(Stmt):
    """
    'while' <expression> 'do' <stmts> 'end'
    """

    def __init__(self, test, do_stmts, line):
        assert isinstance(test, Expr), test
        assert isinstance(do_stmts, Stmts), do_stmts
        self.test = test
        self.do_stmts = do_stmts
        self.line = line

    def __repr__(self):
        return f'IfStmt({self.test} do {self.do_stmts})'


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

class LocalAssignment(Stmt):
    """
    local left := right
    x := 5 * (7 + 8)
    """

    def __init__(self, left, right, line):
        assert isinstance(left, Expr), left
        assert isinstance(right, Expr), right
        self.left = left
        self.right = right
        self.line = line

    def __repr__(self):
        return f'LocalAssignment({self.left}, {self.right})'


class FuncDecl(Decl):
    """
    "func" <name> "(" <params>? ")" <body_stmts> "end"
    """
    def __init__(self, name, params, body_stmts, line):
        assert isinstance(name, str), name
        assert all(isinstance(param, Param) for param in params), params
        self.name = name
        self.params = params
        self.body_stmts = body_stmts
        self.line = line
    def __repr__(self):
        return f'FuncDecl({self.name!r}, {self.params}, {self.body_stmts})'


class Param(Decl):
    """
    A single function parameter
    """
    def __init__(self, name, line):
        assert isinstance(name, str), name
        self.name = name
        self.line = line
    def __repr__(self):
        return f'Param[{self.name!r}]'


class FuncCall(Expr):
    """
    <func_call>  ::=  <name> "(" <args>? ")"
    <args> ::= <expr> ( ',' <expr> )*
    """
    def __init__(self, name, args, line):
        self.name = name
        self.args = args
        self.line = line
    def __repr__(self):
        return f'FuncCall({self.name!r}, {self.args})'

class FuncCallStmt(Stmt):
    """
    <func_call>  ::=  <name> "(" <args>? ")"
    <args> ::= <expr> ( ',' <expr> )*
    """
    def __init__(self, expr, line):
        assert isinstance(expr, FuncCall), expr
        self.expr = expr
    def __repr__(self):
        return f'FuncCallStmt({self.expr!r})'

class RetStmt(Stmt):
    """
    "ret" <expr>
    """
    def __init__(self, value, line):
        self.value = value
        self.line = line
    def __repr__(self):
        return f'RetStmt[{self.value}]'