import yfinance as yf
import pandas as pd

tickers = ["HSBA.L", "BP.L", "AZN.L", "BARC.L", "VOD.L"]

data = yf.download(tickers, start="2023-01-01", end=None, group_by='ticker', auto_adjust=True)

frames = []
for ticker in tickers:
    df = data[ticker].copy()
    df['Ticker'] = ticker
    df['Date'] = df.index
    frames.append(df)

final_df = pd.concat(frames)
final_df.to_csv("ftse100_stocks.csv", index=False)

print("✅ Saved ftse100_stocks.csv from Jan 2023")