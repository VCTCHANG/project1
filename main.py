import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
stocks = {"TSM", "AAPL"}
stock_data = {ticker:yf.Ticker(ticker).history(period="30d")["Close"]for ticker in stocks}
df= pd.DataFrame(stock_data)

print(df.head())
df.plot(figsize=(10, 5), title="Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid()
plt.show()