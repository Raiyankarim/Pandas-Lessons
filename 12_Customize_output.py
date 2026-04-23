import pandas as pd

import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'George', 'Henry', 'Ian', 'Jack'],
    'Age': [25, 30, 35, 40, 29, 33, 38, 45, 27, 31],
    'City': ['New York', 'Chicago', 'Boston', 'Seattle', 'Austin', 'Dallas', 'San Francisco', 'Los Angeles', 'Miami', 'Denver'],
    'Salary': [50000.5, 60000.0, 75000.75, 80000.25, 45000.0, 55000.5, 70000.0, 85000.0, 48000.0, 51000.0]
}

df = pd.DataFrame(data)
# print(df)

# # Increase the maximum number of rows displayed
pd.set_option('display.max_rows', 6)

# # print(df)

# # # Increase the maximum number of columns displayed
# pd.set_option('display.max_columns', 2)

# pd.reset_option('display.max_rows')
# pd.reset_option('display.max_columns')

# print(df)

# # Display the DataFrame
# print(df)

print(pd.describe_option())

