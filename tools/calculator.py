import ast
import operator
import math

# ================= SAFE EXPRESSION EVALUATOR ================= #

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}

def _eval_ast(node):
    if isinstance(node, ast.Constant):  # numbers only
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Invalid constant")

    if isinstance(node, ast.BinOp):
        return OPS[type(node.op)](
            _eval_ast(node.left),
            _eval_ast(node.right)
        )

    if isinstance(node, ast.UnaryOp):
        return OPS[type(node.op)](_eval_ast(node.operand))

    raise ValueError("Invalid expression")

def evaluate_expression(expression: str) -> float:
    """
    Safely evaluate a mathematical expression.
    Example: 5 + 6 * (2 - 1)
    """
    tree = ast.parse(expression, mode="eval")
    return round(_eval_ast(tree.body), 6)

# ================= BASIC CALCULATOR ================= #

def calculate(a: float, b: float, operation: str) -> float:
    """
    Perform basic arithmetic operations.
    operation: add | sub | mul | div
    """
    if operation == "add":
        return a + b
    if operation == "sub":
        return a - b
    if operation == "mul":
        return a * b
    if operation == "div":
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    raise ValueError("Invalid operation")

# ================= FINANCIAL CALCULATIONS ================= #

def simple_interest(p: float, r: float, t: float) -> float:
    """
    Simple Interest
    SI = (P * R * T) / 100
    """
    return round((p * r * t) / 100, 2)

def compound_interest(p: float, r: float, t: float, n: int = 1) -> float:
    """
    Compound Interest
    CI = P * (1 + R/(100*n))^(n*T) - P
    """
    amount = p * pow((1 + r / (100 * n)), (n * t))
    return round(amount - p, 2)

def emi(p: float, annual_rate: float, years: float) -> float:
    """
    EMI calculation
    """
    r = annual_rate / (12 * 100)   # monthly interest rate
    n = years * 12                # total months

    if r == 0:
        return round(p / n, 2)

    emi_value = (p * r * pow(1 + r, n)) / (pow(1 + r, n) - 1)
    return round(emi_value, 2)
