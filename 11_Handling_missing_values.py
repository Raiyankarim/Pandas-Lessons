import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, None, 35, 40],
    'City': ['New York', 'Chicago', None, 'Seattle'],
    'Salary': [50000.5, 60000.0, None, 80000.25]
}

df = pd.DataFrame(data)
# print(df)

# print(df.isna())
# print(df.isnull())
# print(df.notna())

## print(df.dropna(axis=1))
df['Age']= df["Age"].fillna(df["Age"].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print(df)

#isna()
#isnull()
#dropna()
#fillna()
#ffill()
#bfill()
#interpolate()
