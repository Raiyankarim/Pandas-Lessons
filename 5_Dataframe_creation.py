import pandas as pd
data = [
    {'ID': 1, 'Name': 'Alice', 'Age': 25},
    {'ID': 2, 'Name': 'Bob', 'Age': 30},
    {'ID': 3, 'Name': 'Charlie', 'Age': 35}
]
df = pd.DataFrame(data)
# print(df)

# Adding a new column
df['City'] = ['New York', 'San Francisco', 'Los Angeles']
# print(df)

#adding a new row
df.loc[3] = {'ID': 4, 'Name': 'David', 'Age': 40, 'City': 'Chicago'}
print(df)

#delete a column

df.drop("City",axis=1,inplace=True)

print(df)

# delete a row


df.drop(3,axis=0,inplace=True)
print(df)
