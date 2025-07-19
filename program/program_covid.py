# COVID-19 Vaccination Rates

# Overview
# A public health organization wants to track COVID-19 vaccination rates across different regions.

# Dataset
# | Region | Vaccination Rate |
# | --- | --- |
# | North | 70% |
# | South | 60% |
# | East | 80% |
# | West | 50% |

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Region': ['North', 'South', 'East', 'West'],
    'Vaccination Rate': [75, 60, 80, 90]
}

df = pd.DataFrame(data)

plt.bar(df['Region'], df['Vaccination Rate'], color='skyblue')
plt.title('COVID-19 Vaccination Rates by Region')
plt.xlabel('Region')
plt.ylabel('Vaccination Rate (%)')
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()
