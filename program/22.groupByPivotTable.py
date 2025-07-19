# More Information on GroupBy and PivotTables

# GroupBy
# Aggregation Functions
# 1. sum(): Calculate the sum of values.
# 2. mean(): Calculate the mean of values.
# 3. max(): Find the maximum value.
# 4. min(): Find the minimum value.
# 5. count(): Count the number of values.

# Example

import pandas as pd

data = {
    'Category': ['A', 'B','A', 'B','A', 'B'],
    'Sales': [10,20,30,40,50,60]
}

df = pd.DataFrame(data)

#group by catefory and calculate multiple aggregation

grouped_by = df.groupby('Category')['Sales'].agg(['sum','mean','count'])

print(grouped_by)


# PivotTables
# Parameters
# 1. values: The column to aggregate.
# 2. index: The column to use as the index.
# 3. columns: The column to use as the columns.
# 4. aggfunc: The aggregation function.

# Example

# import pandas as pd

# # Create a sample DataFrame
# data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
#         'Region': ['North', 'North', 'South', 'South', 'North', 'South'],
#         'Sales': [10, 20, 30, 40, 50, 60]}
# df = pd.DataFrame(data)

# # Create a PivotTable with multiple aggregations
# pivot_table = pd.pivot_table(df, values='Sales', index='Category', columns='Region', aggfunc=['sum', 'mean'])
# print(pivot_table)