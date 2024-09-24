import yfinance as yf
ticker = input("enter the ticker: ")
from_data=input("Enter the data (YYYY-MM_DD): : ")
to_date=input("enter tha end data (YYYY-MM_DD): ")
stock_data=yf.download(ticker,start=from_data,end=to_date)
stock_data.to_csv("stock_data.csv")
print("stock data in stockdata.csv")
