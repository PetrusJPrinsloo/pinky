from tokens import Token

class Expr:
    """
    Expressions evaluate to a result, like x + (3 * y)
    """

class Stmt:
    """
    Statements perform an action
    """

class Integer(Expr):
    """
    Example: 17
    """
    def __init__(self, value):
        assert isinstance(value, int), value
        self.value = value
    def __repr__(self):
        return f'Integer[{self.value})]'

class Float(Expr):
    """
    Example: 3.14
    """
    def __init__(self, value):
        assert isinstance(value, float), value
        self.value = value
    def __repr__(self):
        return f'Float[{self.value})]'

class UnOp(Expr):
    """
    Example: -x
    """
    def __init__(self, op: Token, operand: Expr):
        assert isinstance(op, Token), op
        assert isinstance(operand, Expr), operand
        self.op = op
        self.operand = operand
    def __repr__(self):
        return f'UnOp[{self.op.lexeme!r}, {self.operand}]'


class BinOp(Expr):
    """
    Example: x + y
    """
    def __init__(self, op: Token, left: Expr, right: Expr):
        assert isinstance(op, Token), op
        assert isinstance(left, Expr), left
        assert isinstance(right, Expr), right
        self.op = op
        self.left = left
        self.right = right
    def __repr__(self):
        return f'BinOp[{self.op.lexeme!r}, {self.left}, {self.right}]'

class Grouping(Expr):
    """
    Example: (expression)
    """
    def __init__(self, value):
        assert isinstance(value, Expr), value
        self.value = value
    def __repr__(self):
        return f'Grouping[{self.value}]'

class While(Stmt):
    pass

class Assignment(Stmt):
    pass