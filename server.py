from mcp.server.fastmcp import FastMCP
from tools.weather import get_weather
from tools.calculator import (
    calculate,
    evaluate_expression,
    simple_interest,
    compound_interest,
    emi
)

mcp = FastMCP("Orchestration MCP Server")

# ================== MATH TOOLS ==================

@mcp.tool()
def math_calculator(a: float, b: float, operation: str) -> float:
    """
    [math]
    Perform a basic arithmetic operation on two numbers.

    Use this tool when the user asks for simple calculations
    like addition, subtraction, multiplication, or division.

    Parameters:
    - a: first number (example: 10)
    - b: second number (example: 5)
    - operation: one of [add, sub, mul, div]

    Example queries:
    - "Add 10 and 5"
    - "Divide 100 by 4"
    """
    return calculate(a, b, operation)


@mcp.tool()
def math_expression(expression: str) -> float:
    """
    [math]
    Evaluate a full mathematical expression following BODMAS rules.

    Use this tool when the user provides a complete expression
    instead of separate numbers.

    Parameters:
    - expression: math expression as a string
      (example: "5 + 6 * (2 - 1)")

    Example queries:
    - "10 + 5 * 3"
    - "(8 + 2) / 5"
    """
    return evaluate_expression(expression.replace("^", "**"))


# ================== FINANCE TOOLS ==================

@mcp.tool()
def finance_simple_interest(p: float, r: float, t: float) -> float:
    """
    [finance]
    Calculate Simple Interest (SI).

    Use this tool when the user asks for simple interest
    based on principal, rate, and time.

    Formula:
    SI = (P × R × T) / 100

    Parameters:
    - p: principal amount (example: 10000)
    - r: annual interest rate in percentage (example: 5)
    - t: time in years (example: 2)

    Example queries:
    - "Simple interest for 10000 at 5% for 2 years"
    """
    return simple_interest(p, r, t)


@mcp.tool()
def finance_compound_interest(p: float, r: float, t: float) -> float:
    """
    [finance]
    Calculate Compound Interest (CI).

    Use this tool when the user asks for compound interest
    over a period of time.

    Parameters:
    - p: principal amount (example: 50000)
    - r: annual interest rate in percentage (example: 8)
    - t: time in years (example: 3)

    Example queries:
    - "Compound interest for 50000 at 8% for 3 years"
    """
    return compound_interest(p, r, t)


@mcp.tool()
def finance_emi(p: float, annual_rate: float, years: float) -> float:
    """
    [finance]
    Calculate monthly EMI (Equated Monthly Installment) for a loan.

    Use this tool when the user asks about loan EMIs,
    home loans, car loans, or monthly payments.

    Parameters:
    - p: loan principal amount (example: 500000)
    - annual_rate: annual interest rate in percentage (example: 8.5)
    - years: loan tenure in years (example: 20)

    Returns:
    - Monthly EMI amount

    Example queries:
    - "EMI for 5 lakh home loan at 8.5% for 20 years"
    """
    return emi(p, annual_rate, years)



# ================== WEATHER TOOLS ==================

@mcp.tool()
def weather_current(city: str) -> str:
    """
    [weather]
    Get the current weather conditions of a city.

    Use this tool when the user asks about weather,
    temperature, humidity, or climate of a place.

    Parameters:
    - city: name of the city (example: "Bangalore")

    Example queries:
    - "Weather in Delhi"
    - "Temperature in Mumbai"
    """
    return get_weather(city)


if __name__ == "__main__":
    mcp.run()
