
import pandas as pd
import program.numpyProgram as np

data = {
    'Name': ['John', 'Anna', np.nan, 'Ram', 'Raj'],
    'Age': [25, np.nan, 18, 10, 5]
}

df = pd.DataFrame(data)

df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].mean())

df = df.drop_duplicates()

print("Cleaned DataFrame:")
print(df)
