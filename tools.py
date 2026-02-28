from crewai.tools import tool

# -------- TOOL 1: Load Financial Document --------
@tool
def financial_document_tool(file_path: str) -> str:
    """
    Loads and reads financial document text (simulated for now)
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = f.read()
        return data
    except Exception as e:
        return f"Error reading file: {str(e)}"


# -------- TOOL 2: Investment Analysis --------
@tool
def investment_tool(data: str) -> str:
    """
    Performs investment analysis
    """
    if not data:
        return "No data provided for investment analysis."

    return f"Investment Analysis:\n- Growth potential: High\n- Recommendation: Invest carefully\n- Summary based on data length: {len(data)}"


# -------- TOOL 3: Risk Assessment --------
@tool
def risk_tool(data: str) -> str:
    """
    Performs risk assessment
    """
    if not data:
        return "No data provided for risk analysis."

    return f"Risk Assessment:\n- Risk Level: Medium\n- Suggestion: Diversify portfolio\n- Data size: {len(data)}"