import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000.5, 60000.0, 75000.75, 80000.25],
    'Join_Date': ['2023-01-10', '2022-11-15', '2021-06-21', '2021-06-21']
}

df = pd.DataFrame(data)
# print(df)

# df.convert_dtypes(errors='coerce')
print(df.dtypes)

df['Age'] = df['Age'].astype('str')

print(df.dtypes)

print(df)

# astype()
# to_numeric()
# to_datetime()
# to_string()
# convert_dtypes()