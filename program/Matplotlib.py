import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#sample data
X = np.random.randn(50)
y = np.random.randn(50)

#Matplotlib scatter plot 
plt.scatter(X, y)
plt.title("Scatter Plot")
plt.show()


#Seaborn scatter plot
plt.scatter(X,y)
plt.title('Scatter Plot')
plt.show()


#seaborn scatter plot 
sns.set()
sns.scatterplot(x=X, y=y)
plt.title("Seaborn Scatter Plot")
plt.show()