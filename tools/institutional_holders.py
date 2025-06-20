from langchain_core.tools import tool
import yfinance as yf

@tool
def summary_of_institutional_holders(ticker: str) -> dict:
    """Top institutional holders with % of shares, count, value."""
    return yf.Ticker(ticker).get_institutional_holders().to_dict(orient="records")
