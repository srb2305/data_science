# Scenario
# A company wants to analyze its sales data to understand customer behavior, identify trends, and optimize marketing strategies.

# Data
# | Customer ID | Product | Sales Amount | Date       |
# | ----------- | ------- | ------------ | ---------- |
# | 1           | A       | 100          | 2022-01-01 |
# | 2           | B       | 200          | 2022-01-02 |
# | 3           | A       | 150          | 2022-01-03 |
# | ...         | ...     | ...          | ...        |

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Create a sample DataFrame
data = {
    'Customer ID': [1, 2, 3, 4, 5],
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Sales Amount': [100, 200, 150, 300, 250],
    'Date': pd.to_datetime(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'])
}
df = pd.DataFrame(data)
# Group by Product and sum Sales Amount
sales_by_product = df.groupby('Product')['Sales Amount'].sum().reset_index()    
# Plotting the sales data
plt.figure(figsize=(10, 6))
sns.barplot(x='Product', y='Sales Amount', data=sales_by_product, palette='viridis')
plt.title('Total Sales Amount by Product')
plt.xlabel('Product')   
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Plotting sales over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Sales Amount', data=df, marker='o')
plt.title('Sales Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Analyzing customer behavior
customer_behavior = df.groupby('Customer ID')['Sales Amount'].sum().reset_index()   
# Plotting customer behavior
plt.figure(figsize=(10, 6))
sns.barplot(x='Customer ID', y='Sales Amount', data=customer_behavior, palette='coolwarm')
plt.title('Total Sales Amount by Customer')
plt.xlabel('Customer ID')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Saving the DataFrame to a CSV file
df.to_csv('company_sales_data.csv', index=False)
# Reading the CSV file to verify
df_read = pd.read_csv('company_sales_data.csv')
print(df_read)
# Displaying the first few rows of the DataFrame
print(df.head())
# Displaying the sales data summary
print(sales_by_product)
# Displaying customer behavior summary
print(customer_behavior)
# Displaying the DataFrame structure
print(df.info())
# Displaying the DataFrame statistics
print(df.describe())