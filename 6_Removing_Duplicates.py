import pandas as pd

data = {
    'ID': [1, 2, 1, 3, 4, 4],
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'David', 'David'],
    'Age': [25, 30, 25, 35, 40, 40]
}

df = pd.DataFrame(data)
print(df)

#Removing and Identifying Duplicates

print(df.duplicated())

print(df.drop_duplicates())
