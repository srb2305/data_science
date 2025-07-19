# An investor wants to analyze the daily returns of a stock to understand its volatility.

# Dataset
# | Date | Stock Price |
# | --- | --- |
# | 2022-01-01 | 100 |
# | 2022-01-02 | 105 |
# | 2022-01-03 | 110 |
# | ... | ... |

import numpy as np

mean_price = np.array([100, 105, 110, 115]).mean()
print("Mean Stock Price:", mean_price)  # 107.5
std_dev = np.array([500, 600, 700, 800]).std()
print("Standard Deviation of Stock Price:", std_dev)  # 1.118033


