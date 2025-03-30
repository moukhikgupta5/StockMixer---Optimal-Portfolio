import pandas as pd
import numpy as np
import yfinance as yf
import sys
import json

# yf.pdr_override()

selected = sys.argv[1:]
# selected = ['GOOG', 'F', 'WMT', 'GE', 'TSLA']
# print(selected)
# Fetch adjusted close prices for all tickers
for i in range(5):
    try:
        stock_data = yf.download(selected, progress=False, period="10y", auto_adjust=True)
        break
    except Exception as e:
        print(f"Failed to fetch data from yahoo: {str(e)}")
        exit(1)
# print(stock_data['Adj Close']['F'])
adj_close_data = {}
for ticker_symbol in selected:
        try:
            adj_close_data[ticker_symbol] = stock_data['Close'][ticker_symbol]
        except:
            exit(1)
        # print(f"Fetched data for {ticker_symbol}", stock_data['Adj Close'])
    

# Convert the data to a single DataFrame
table = pd.DataFrame(adj_close_data)
# print(table)
# table.to_csv("test.csv")
# print(table)    

returns_daily = table.pct_change()
returns_annual = returns_daily.mean() * 250

# get daily and covariance of returns of the stock
cov_daily = returns_daily.cov()
cov_annual = cov_daily * 250

# empty lists to store returns, volatility and weights of imiginary portfolios
port_returns = []
port_volatility = []
stock_weights = []

# set the number of combinations for imaginary portfolios
num_assets = len(selected)
num_portfolios = 50000

# populate the empty lists with each portfolios returns,risk and weights
for single_portfolio in range(num_portfolios):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    returns = np.dot(weights, returns_annual)
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_annual, weights)))
    port_returns.append(returns)
    port_volatility.append(volatility)
    stock_weights.append(weights)

# a dictionary for Returns and Risk values of each portfolio
portfolio = {'Returns': port_returns,
             'Volatility': port_volatility}

# extend original dictionary to accomodate each ticker and weight in the portfolio
for counter,symbol in enumerate(selected):
    portfolio[symbol] = [weight[counter] for weight in stock_weights]

# make a nice dataframe of the extended dictionary
df = pd.DataFrame(portfolio)

# get better labels for desired arrangement of columns
column_order = ['Returns', 'Volatility'] + [stock for stock in selected]

# reorder dataframe columns
df = df[column_order]

# min volatilitys
min_vol_port = df.iloc[df['Volatility'].idxmin()].to_dict()

# print(min_vol_port)

# max return
max_ret_port = df.iloc[df['Returns'].idxmax()].to_dict()
# print(max_ret_port)

#sharp ratio on risk free rate
rf=0.05 #risk free rate , get from user ?
optimal_port = df.iloc[((df['Returns']-rf)/df['Volatility']).idxmax()].to_dict()
# print(optimal_port)

# plt.subplots(figsize=(8,8))
# plt.scatter(df['Volatility'], df['Returns'], marker='o',s=10, alpha=0.3,color='green')
# plt.scatter(min_vol_port[1], min_vol_port[0], color='y', marker='*',s=500)
# plt.scatter(optimal_port[1], optimal_port[0],color='b',marker='*',s=500)
# plt.scatter(max_ret_port[1], max_ret_port[0],color='r',marker='*',s=500)
# plt.show()

# Print the results as JSON
result_json = [json.dumps(min_vol_port), json.dumps(max_ret_port), json.dumps(optimal_port)]
print('\n'.join(result_json))