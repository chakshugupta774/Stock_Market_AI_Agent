from agent.agent_executor import run_query

if __name__ == "__main__":
    query = input("Ask your financial stock-related question: ")
    response = run_query(query)
    print("Agent Response:\n", response)
