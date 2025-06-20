from langchain_core.tools import tool
import yfinance as yf

@tool
def stock_news(ticker: str) -> dict:
    """Latest news related to stock."""
    return yf.Ticker(ticker).get_news()
