import re
from mcp.server.fastmcp import FastMCP
from tools.weather import get_weather
from tools.calculator import (
    evaluate_expression,
    simple_interest,
    compound_interest,
    emi,
    calculate
)

mcp = FastMCP("Orchestration MCP Server")

@mcp.tool()
def agent_router(user_query: str) -> dict:
    q = user_query.lower().strip()

    # ---------- SIMPLE INTEREST ----------
    if q.startswith("si") or "simple interest" in q:
        nums = list(map(float, re.findall(r"\d+\.?\d*", q)))
        if len(nums) != 3:
            return {"result": "Format: SI <Principal> <Rate> <Time>"}

        p, r, t = nums
        return {"result": simple_interest(p, r, t)}

    # ---------- COMPOUND INTEREST ----------
    if q.startswith("ci") or "compound interest" in q:
        nums = list(map(float, re.findall(r"\d+\.?\d*", q)))
        if len(nums) != 3:
            return {"result": "Format: CI <Principal> <Rate> <Time>"}

        p, r, t = nums
        return {"result": compound_interest(p, r, t)}

    # ---------- EMI ----------
    if q.startswith("emi"):
        nums = list(map(float, re.findall(r"\d+\.?\d*", q)))
        if len(nums) != 3:
            return {"result": "Format: EMI <Principal> <Rate> <Years>"}

        p, r, t = nums
        return {"result": emi(p, r, t)}

    # ---------- CALCULATOR ----------
    math_expr = q.replace(" ", "").strip()

    if re.match(r"^[0-9+\-*/().^]+$", math_expr) and any(op in math_expr for op in "+-*/"):
        try:
            result = evaluate_expression(math_expr.replace("^", "**"))
            return {"result": result}
        except Exception:
            return {"result": "Invalid mathematical expression."}

    # ---------- WEATHER ----------
    if re.search(r"\b(weather|temperature|temp)\b", q):
        match = re.search(r"(?:weather|temperature|temp)\s*(?:in|of)?\s*([a-zA-Z\s]{2,25})", q)
        if not match:
            return {"result": "Please specify a city name."}

        city = match.group(1)
        city = re.sub(r"[^a-zA-Z\s]", "", city)
        city = " ".join(city.split()[:3]).title()

        return {"result": get_weather(city)}

    return {"result": "Sorry, I could not understand the request."}


if __name__ == "__main__":
    mcp.run()
