import seaborn as sns
import matplotlib.pyplot as plt 

#load the tips dataset
tips = sns.load_dataset("tips")

#Create a scatter plot
sns.scatterplot(x = "total_bill", y="tip", data=tips)

#show the plot
plt.show()