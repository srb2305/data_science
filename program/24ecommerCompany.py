# Scenario
# An e-commerce company wants to analyze its sales data to understand 
# product performance, customer behavior, and sales trends.

# Analysis
# 1. Product Performance: Calculate total sales and quantity sold for each product.
# 2. Customer Behavior: Analyze customer purchase frequency and average order value.
# 3. Sales Trends: Identify seasonal sales patterns and trends.

import pandas as pd

data = pd.DataFrame({
    'Order ID':  [1,2,3],
    'Product Id': ['A001', 'B002', 'A001'], 
    'Product Name': ['iPhone','Samsung','iPhone'],
    'Customer Id': ['C001','C002','C003'],
    'Order Date': ['2022-01-01', '2022-01-05', '2022-01-10'],
    'Quantity': [2,1,1],
    'Sales': [1000,800,500]
})

#Calculate total sales and quantity sold for each product.
product_performance = data.groupby('Product Id')[['Sales','Quantity']].sum()
#print(product_performance)

# Analyze customer purchase frequency and average order value.
customer_behaviour = data.groupby('Customer Id')[['Sales']].mean()
#print(customer_behaviour)

#Identify seasonal sales patterns and trends.
sales_trends = data.groupby('Order Date')['Product Name'].describe()
print(sales_trends)