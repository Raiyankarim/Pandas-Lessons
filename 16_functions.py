import pandas as pd

# Sample data
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    'Price': [1000, 500, 300, 150, 50],
    'Stock': [10, 50, 30, 5, 100]
}

df = pd.DataFrame(data)

# Display DataFrame
print(df)

#Apply functions to each column
# Calculate the total value of stock for each product
df['Total Value'] = df['Price'] * df['Stock']
print("\nDataFrame after calculating total value of stock:")
print(df)
# Apply a custom function to calculate the price category
def price_category(price):
    if price >= 1000:
        return 'Expensive'
    elif price >= 500:
        return 'Moderate'
    else:
        return 'Affordable'
df['Price Category'] = df['Price'].apply(price_category)
print("\nDataFrame after categorizing price:")
print(df)








