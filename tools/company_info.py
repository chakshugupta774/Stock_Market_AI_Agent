from langchain_core.tools import tool
import yfinance as yf

@tool
def company_information(ticker: str) -> dict:
    """Get company info like address, sector, officers, financials, etc."""
    ticker_obj = yf.Ticker(ticker)
    return ticker_obj.get_info()
 