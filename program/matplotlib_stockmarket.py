import numpy as np
import matplotlib.pyplot as plt

#initial stock price
stock_price = 5

#number of trading days
days = 52

#Generate daily returns
returns = np.random.rand(days)

#calculate stock prices
stock_prices = stock_price * np.cumprod(1 + returns/100 )

#plot stock prices
plt.plot(stock_prices)
plt.title('Simulated stock price')
plt.show()


