# task.py
from crewai import Task
from agents import financial_analyst
from tools import financial_document_tool, investment_tool, risk_tool

document_analysis = Task(
    description="Analyze financial documents and extract key risks, opportunities, and recommendations.",
    expected_output="A detailed financial analysis report.",
    agent=financial_analyst,
    tools=[financial_document_tool],   #  StructuredTool instance
    async_execution=False
)

investment_analysis = Task(
    description="Perform investment analysis based on the financial documents.",
    expected_output="Investment risks, opportunities, and recommendations.",
    agent=financial_analyst,
    tools=[investment_tool],           # StructuredTool instance
    async_execution=False
)

risk_assessment = Task(
    description="Conduct risk analysis based on the financial documents.",
    expected_output="Detailed risk analysis with financial jargon and projections.",
    agent=financial_analyst,
    tools=[risk_tool],                 #  StructuredTool instance
    async_execution=False
)