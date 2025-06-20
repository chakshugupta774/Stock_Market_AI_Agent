from langchain_core.tools import tool
import yfinance as yf
from datetime import date

@tool
def stock_grade_updrages_downgrades(ticker: str) -> dict:
    """Stock rating upgrades/downgrades since Jan 1 of current year."""
    curr_year = date.today().year
    df = yf.Ticker(ticker).get_upgrades_downgrades()
    df = df.loc[df.index > f"{curr_year}-01-01"]
    df = df[df["Action"].isin(["up", "down"])]
    return df.to_dict(orient="records")
