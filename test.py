from edgar import *
import pandas as pd
import numpy as np

set_identity("Nikhil Whyte nikhilwhyte@gmail.com")

company = Company("JXN")
bal = company.balance_sheet().to_dataframe().set_index("label", drop=True)
income = company.income_statement().to_dataframe().set_index("label", drop=True)
income.drop(income["label"] == "Liabilities" && income["is_abstract"] == True, inplace=True)
cf = company.cash_flow_statement().to_dataframe().set_index("label", drop=True)

bal.to_csv("./examples/balance_sheet.csv")
income.to_csv("./examples/income_statement.csv")
cf.to_csv("./examples/cashflow_statement.csv")

print(bal.loc["Liabilities"])


