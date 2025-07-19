import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#sample data
data = {'Feature1': [10, 20, 30, 40, 50],
        'Feature2': [100, 200, 300, 400, 500]
        }

df = pd.DataFrame(data)

#create a MinMaxScaler object
scaler = MinMaxScaler()

#Fit and transform the data
scaled_data = scaler.fit_transform(df)

#convert back to DataFrame
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

print("Original DataFrame:")
print(df)   
print("\nScaled DataFrame:")
print(scaled_df)