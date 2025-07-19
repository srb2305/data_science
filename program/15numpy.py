import pandas as pd
import numpy as np

#crae a Dataframe
data = {
    'Name': ['John', 'Anna','Ram', 'Raj'],
    'Age': [25, 30, 18, 10]
}

df = pd.DataFrame(data)

# canculate mean age
mean_age = df['Age'].mean()
print("Mean Age:", mean_age)

#create a numpy array
age_array = np.array([1,2,3,4,5]) 
print("Age Array:", age_array.mean())
