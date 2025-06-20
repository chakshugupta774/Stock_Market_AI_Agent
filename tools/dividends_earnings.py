from langchain_core.tools import tool
import yfinance as yf

@tool
def last_dividend_and_earnings_date(ticker: str) -> dict:
    """Get last dividend and earnings release date."""
    return yf.Ticker(ticker).get_calendar()
