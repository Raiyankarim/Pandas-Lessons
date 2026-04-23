import pandas as pd

# Sample data
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    'Price': [1000, 500, 300, 150, 50],
    'Stock': [10, 50, 30, 5, 100],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories']
}

df = pd.DataFrame(data)

print(df)

#Conditional Filtering

print(df[df['Price']> 300])

df1 = df[(df['Price'] > 300) & (df['Stock'] >= 50)]

df2 = df.query('Price > 300 & Stock >= 30')

df3 = df[df['Category'].isin(['Electronics'])]

df4 = df[df['Product'].str.contains('Phone')]

df5 = df[df['Price'].between(300, 500)]

print(df5)


