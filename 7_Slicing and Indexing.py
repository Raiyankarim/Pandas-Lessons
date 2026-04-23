# import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'City': ['New York', 'Chicago', 'Boston', 'Seattle']
# }

# df = pd.DataFrame(data,index =['A', 'B', 'C', 'D'])

# print(df)

# # # Select a mutiple column
# # print(df[['Name', 'City']])

# # # Using dot notation
# # print(df.Age)

# # Select the first row using iloc
# print(df.iloc[[0,2],[0,2]])



# # # Select row using label with loc
# # print(df.loc['B'])

# # print(df[(df['Age']>=30) & (df['City'].isin(['New York', 'Chicago']))])

# print(df.dtypes)

import pandas as pd

# Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Chicago', 'Boston', 'Seattle'],
    'Salary': [50000.5, 60000.0, 75000.75, 80000.25],
    'Employed': [True, False, True, True]
}

df = pd.DataFrame(data)

# Check data types
print(df.dtypes)

# print(df.select_dtypes(include=['int64', 'float64']))

df['Age']= df['Age'].astype('float64')
print(df.dtypes)