import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


df = pd.read_csv('companies.csv', encoding='latin-1')

# columns_to_remove = ["Country","Category Name",'Exchange','Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12']
columns_to_remove = ["Name","Category Name",'Exchange','Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12']

# Remove the specified columns
df = df.drop(columns=columns_to_remove)
df.replace(np.nan, 'Not available', inplace=True)
filtered_df = df[df['Country'].isin(['India'])]


tickers = filtered_df["Ticker"].values.tolist()
print(len(tickers))
try:
    stock_data = yf.download(tickers[:1000], period="10y")
except Exception as e:
        print(f"Failed to fetch data from yahoo: {str(e)}")

adj_close_data = {}
for ticker_symbol in tickers:
        try:
            adj_close_data[ticker_symbol] = stock_data['Adj Close'][ticker_symbol]
        except:
            continue
        # print(f"Fetched data for {ticker_symbol}", stock_data['Adj Close'])
    

# Convert the data to a single DataFrame
table = pd.DataFrame(adj_close_data)
table.to_csv("test.csv")