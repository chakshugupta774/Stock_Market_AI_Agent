import streamlit as st
from agent.agent_executor import run_query

st.set_page_config(page_title="Stock Market AI Assistant", layout="wide")
st.markdown("""
    <style>
    .title-style {
        font-size: 3em;
        font-weight: 800;
        color: #1a73e8;
        text-align: center;
        margin-bottom: 20px;
    }
    .question-box {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    .suggestion-title {
        font-size: 1.3em;
        font-weight: 600;
        color: #444;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title-style'>💹 Stock Market AI Assistant</div>", unsafe_allow_html=True)

st.markdown("""
<div class='question-box'>
    <p style='font-size:1.1em;'>
        Ask your financial stock-related question below! You can inquire about company summaries, stock prices, dividends, earnings, institutional holders, stock splits, and more.
    </p>
</div>
""", unsafe_allow_html=True)

query = st.text_input("", placeholder="e.g., What is the business summary of Amazon?")

if st.button("Submit") and query:
    with st.spinner("Thinking..."):
        result = run_query(query)
        st.success("Here's your result:")
        st.write(result)

# Suggested Questions Section
st.markdown("<div class='suggestion-title'>💡 Suggested Questions by Category:</div>", unsafe_allow_html=True)

suggested_queries = {
    "🏢 Company Information": [
        "What is the business summary of Amazon?",
        "Tell me about the company officers of Microsoft.",
        "What industry and sector does Netflix belong to?",
        "What is the official website and address of Tesla?",
        "What is the current market cap and EBITDA of Apple?"
    ],
    "💸 Dividend & Earnings Info": [
        "When was the last dividend paid by Apple?",
        "When is the next earnings release for Nvidia?",
        "Has Tesla recently paid any dividends?",
        "What are the upcoming earnings dates for Microsoft?"
    ],
    "🧾 Mutual Fund Holders": [
        "Who are the top mutual fund holders of Apple?",
        "Which mutual funds own the most shares of Amazon?",
        "How much stake do mutual funds hold in Google?"
    ],
    "🏦 Institutional Holders": [
        "Who are the top institutional investors in Meta?",
        "How much of Tesla is owned by institutions?",
        "What is the value of institutional holdings in Microsoft?"
    ],
    "🔼🔽 Stock Grades / Ratings": [
        "Has Nvidia been upgraded or downgraded recently?",
        "What are the latest stock rating changes for Apple?",
        "Which firms downgraded Tesla this year?",
        "Show me recent grade upgrades of Microsoft."
    ],
    "➗ Stock Splits": [
        "When did Apple last split its stock?",
        "Has Amazon ever had a stock split?",
        "Show me the stock split history of Microsoft."
    ],
    "📰 News": [
        "What are the latest news articles about Tesla?",
        "Show current news coverage on Apple.",
        "Are there any recent headlines about Meta?"
    ]
}

# Display in expandable sections
for category, questions in suggested_queries.items():
    with st.expander(category):
        for q in questions:
            if st.button(q):
                query = q
                with st.spinner("Thinking..."):
                    result = run_query(query)
                    st.success("Here's your result:")
                    st.write(result)
                st.stop()
