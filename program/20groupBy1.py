# Data Analysis with GroupBy and PivotTables

# GroupBy
# GroupBy is used to group data by one or more columns and perform aggregation operations.

import pandas as pd

data = {
    'Category' : ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sales' : [10,20,30,40,50,60]
}

df = pd.DataFrame(data)

#group by category and calulate sum of sales

group_df = df.groupby('Category')['Sales'].sum()

print(group_df)