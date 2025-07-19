from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import pandas as pd

#sample data
data = {
    'Bedrooms': [1, 2, 3, 4, 5],
    'SqFt': [500, 1000, 1500, 2000, 2500],
    'Location': ['Urban', 'Suburban', 'Urban', 'Rural', 'Suburban']
}

df = pd.DataFrame(data)

#scaling

scaler = MinMaxScaler()

df[['Bedrooms', 'SqFt']] = scaler.fit_transform(df[['Bedrooms', 'SqFt']])

#encoding
le = LabelEncoder()
df['Location'] = le.fit_transform(df['Location'])

print("Original DataFrame:")
print(data) 
print("\nScaled and Encoded DataFrame:")
print(df)