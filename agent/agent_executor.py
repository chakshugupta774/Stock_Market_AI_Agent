import os
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage

# Load GROQ_API_KEY from .env file
load_dotenv()

# Import all tools
from tools import (
    company_information,
    last_dividend_and_earnings_date,
    stock_splits_history,
    summary_of_mutual_fund_holders,
    summary_of_institutional_holders,
    stock_grade_updrages_downgrades,
    stock_news,
)

# List of tools used by the agent
tools = [
    company_information,
    last_dividend_and_earnings_date,
    stock_splits_history,
    summary_of_mutual_fund_holders,
    summary_of_institutional_holders,
    stock_grade_updrages_downgrades,
    stock_news,
]

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Try to answer user query using available tools.",
        ),
        MessagesPlaceholder(variable_name="messages"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

# Create agent and executor
finance_agent = create_tool_calling_agent(llm, tools, prompt)
finance_agent_executor = AgentExecutor(agent=finance_agent, tools=tools, verbose=True)

# Exposed function to run queries
def run_query(query: str):
    return finance_agent_executor.invoke({"messages": [HumanMessage(content=query)]})
