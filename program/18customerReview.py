# Scenario
# An e-commerce company wants to analyze customer reviews to understand product sentiment,
# identify areas for improvement, and enhance customer satisfaction.
#
# Data
# | Review ID | Product | Review Text | Rating |
# | --------- | ------- | ----------- | ------ |
# | 1         | A       | Great product! | 5      |
# | 2         | B       | Not impressed. | 2      |
# | 3         | A       | Excellent quality! | 5      |
# | ...       | ...     | ...          | ...    |


import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# Create a sample DataFrame
data = {
    'Review ID': [1, 2, 3, 4, 5],
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Review Text': ['Great product!', 'Not impressed', 'Excellent quality!', '300', '250'],
    'Rating': [5,2,5,4,5]
}

df = pd.DataFrame(data)
sales_by_product = df.groupby('Product')['Rating'].mean().reset_index()
print(sales_by_product)

plt.figure(figsize=(10, 6))
#sns.barplot(x='Product', y='Rating', data=sales_by_product, palette='viridis')

plt.bar(sales_by_product['Product'], sales_by_product['Rating'], color='skyblue')

plt.title('Customer reviews')
plt.xlabel('Product')   
plt.ylabel('Rating')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

