# agents.py

import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_openai import ChatOpenAI

# Import tool instances (not classes)
from tools import financial_document_tool, investment_tool, risk_tool

# Load environment variables
load_dotenv()

# Define LLM
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)

# ---------- Financial Analyst Agent ----------
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents and provide risks, opportunities, and recommendations.",
    backstory="You are an experienced financial analyst with deep knowledge of compliance and document review.",
    verbose=True,
    memory=True,
    llm=llm,
    tools=[financial_document_tool, investment_tool, risk_tool],
    max_iter=2,
    max_rpm=2,
    allow_delegation=False
)

# ---------- Investment Advisor Agent ----------
investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide investment advice and highlight opportunities based on financial documents.",
    backstory="You are a seasoned investment advisor who connects financial ratios to market opportunities.",
    verbose=True,
    memory=True,
    llm=llm,
    tools=[investment_tool],
    max_iter=2,
    max_rpm=2,
    allow_delegation=False
)

# ---------- Risk Assessor Agent ----------
risk_assessor = Agent(
    role="Risk Assessor",
    goal="Evaluate risks in financial documents and provide detailed risk scenarios.",
    backstory="You specialize in identifying extreme risks and volatility in financial markets.",
    verbose=True,
    memory=True,
    llm=llm,
    tools=[risk_tool],
    max_iter=2,
    max_rpm=2,
    allow_delegation=False
)