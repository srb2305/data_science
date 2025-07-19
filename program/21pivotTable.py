# PivotTables
# PivotTables are used to summarize and analyze data by creating a spreadsheet-style pivot table.

# Example

# Use Cases
# 1. Sales Analysis: Analyze sales data by product, region, or time period.
# 2. Customer Segmentation: Segment customers based on demographics, behavior, or purchase history.
# 3. Financial Analysis: Analyze financial data by account, department, or time period.

import pandas as pd

data = {
    'Category': ['A','B','A','B','A','B'],
    'Region': ['North','South','North','South','North','South'],
    'Sales': [10,20,30,40,50,60]
}

dataframe = pd.DataFrame(data)

#create a Pivot Table
pivot_table = pd.pivot_table(dataframe, values = 'Sales', index = 'Category', columns= 'Region', aggfunc='sum')

print(pivot_table)