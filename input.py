import json
import sys

from edgar import *
import yfinance as yf
import pandas as pd
import numpy as np
from pandas import DataFrame

set_identity("Nikhil Whyte nikhilwhyte@gmail.com")

# Import list of symbols from file into array
symbols = []
for i in range(0,2):
    df = pd.read_csv("Results_"+str(i)+".csv")
    s = df["Symbol"].to_numpy()
    for i in s:
        symbols.append(i)


# add the information from each company to a dataframe
for ticker in symbols:
    company = Company(ticker)
    bal = company.balance_sheet(periods=5).to_dataframe().set_index("label", drop=True)
    income = company.income_statement(periods=5).to_dataframe().set_index("label", drop=True)
    income.drop(income["label"] == "Liabilities" && income["is_abstract"] == True, inplace=True)
    cf = company.cash_flow_statement(periods=5).to_dataframe().set_index("label", drop=True)

    info = {}
    info["price"] = yf.Ticker(ticker).fast_info["lastPrice"]
    info["shares"] = yf.Ticker(ticker).fast_info["shares"]
    info["market cap"] = info["price"] * info["shares"]

    info["Total Debt"] = bal["liabilities"]

    info["P/E"] = info["market cap"] / (income.loc["Earnings Per Share, Basic", "FY 2025"] - income.loc["Preferred Stock Dividends and Other Adjustments", "FY 2025"])
    info["EV"] = info["market cap"] + ()

