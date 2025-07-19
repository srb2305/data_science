# read write csv file
import pandas as pd
import matplotlib.pyplot as plt

#create a dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],}   
df = pd.DataFrame(data)


#write the dataframe to a csv file
df.to_csv('people.csv', index=False)

#read the csv file
df_read = pd.read_csv('people.csv')

print(df_read)

#create a new dataframe
new_data = pd.DataFrame(df_read)

plt.figure(figsize=(8, 5))
#plotting the data
plt.bar(new_data['Name'], new_data['Age'], color='blue')
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Bar Plot of Age by Name')
plt.show()
