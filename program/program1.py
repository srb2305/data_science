# Overview
# A company wants to analyze its sales data to identify trends and patterns. 
# They have a dataset containing sales figures for different products across various regions.

# Dataset
# | Product | Region | Sales |
# | --- | --- | --- |
# | A | North | 100 |
# | A | South | 150 |
# | B | North | 200 |
# | B | South | 250 |
# | C | North | 300 |
# | C | South | 350 |

import matplotlib.pyplot as plt
import pandas as pd

#sample data
data = {
    'Product': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Region': ['North', 'South', 'North', 'South', 'North','South'],
    'Sales': [100, 150, 200, 250, 300, 350]
}

df = pd.DataFrame(data)

print(df)

plt.plot(df['Product'], df['Sales'], marker='o')
plt.title('Sales Data')
plt.show()
