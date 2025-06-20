from langchain_core.tools import tool
import yfinance as yf

@tool
def stock_splits_history(ticker: str) -> dict:
    """Historical stock splits."""
    return yf.Ticker(ticker).get_splits().to_dict()
