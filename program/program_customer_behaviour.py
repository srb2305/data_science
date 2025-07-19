# An e-commerce company wants to analyze customer purchase behavior to identify trends, preferences, and opportunities for growth.

# Dataset
# | Customer ID | Product Category | Purchase Amount | Purchase Date |
# | --- | --- | --- | --- |
# | 1 | Electronics | 100 | 2022-01-01 |
# | 1 | Fashion | 50 | 2022-01-15 |
# | 2 | Electronics | 200 | 2022-02-01 |
# | 3 | Home Goods | 150 | 2022-03-01 |
# | ... | ... | ... | ... |

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Customer ID': [1, 2, 3, 4],
    'Product Category': ['Electronics', 'Fashion', 'Electronics', 'Home Goods'],
    'Purchase Amount': [100, 50, 200, 150],
    'Purchase Date': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01']
}

df = pd.DataFrame(data)
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
plt.figure(figsize=(10, 5))
plt.bar(df['Customer ID'], df['Purchase Amount'], color='lightgreen')
plt.title('Customer Purchase Behavior')
plt.xlabel('Customer ID')   
plt.ylabel('Purchase Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Customer Behavior Analysis
