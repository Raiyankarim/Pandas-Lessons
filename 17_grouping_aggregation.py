import pandas as pd

# Sample data
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Headphones', 'Phone', 'Tablet', 'Laptop'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories', 'Accessories', 'Electronics', 'Electronics', 'Electronics'],
    'Price': [1000, 500, 300, 150, 50, 20, 80, 600, 250, 1100],
    'Stock': [10, 50, 30, 5, 100, 150, 50, 40, 20, 5]
}

df = pd.DataFrame(data)

# Display DataFrame
print(df)

#Groupby and Aggregation

df1 = df.groupby(['Category','Product']).agg({'Price':['mean','sum'], 'Stock':['sum','count']}).reset_index()

print(df1)