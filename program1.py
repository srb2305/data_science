import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Srb', 'Ram', 'Raj'],
    'Age': [25,36,18,10,5],
    'Country': ['INDIA',  'USA','UK', 'CHINA', 'PAKISTAN']
}

df = pd.DataFrame(data)

print(df)

filtered_df = df[df['Age'] > 20]

print(filtered_df)

groupBy = df.groupby('Country')['Age'].mean()

print(groupBy)