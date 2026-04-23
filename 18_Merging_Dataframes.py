import pandas as pd

# Sample data for DataFrame 1
data1 = {
    'Customer_ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Location': ['New York', 'California', 'Texas', 'Florida']
}

# Sample data for DataFrame 2
data2 = {
    'Customer': [101, 103, 104, 105],
    'Purchase': ['Laptop', 'Tablet', 'Phone', 'Monitor'],
    'Amount': [1000, 300, 600, 150]
}

# Create DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Display DataFrames
print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

#inner join
result = pd.merge(df1,df2,left_on='Customer_ID', right_on='Customer',how='inner')

print("\inner Join Result:",result)

