from langchain_core.tools import tool
import yfinance as yf

@tool
def summary_of_mutual_fund_holders(ticker: str) -> dict:
    """Top mutual fund holders with % of shares, count, value."""
    return yf.Ticker(ticker).get_mutualfund_holders().to_dict(orient="records")
