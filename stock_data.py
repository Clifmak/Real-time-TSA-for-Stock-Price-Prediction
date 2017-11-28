#Download Twitter Data from NASDAQ
import pandas as pd
import csv
stockdata = pd.read_csv('http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx?render=download')
with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
    print(stockdata)


