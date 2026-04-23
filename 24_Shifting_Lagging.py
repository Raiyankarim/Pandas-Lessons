import pandas as pd

# Step 1: Create sample data
data = {
    'Date': pd.date_range(start='2025-01-01', periods=10, freq='D'),
    'Sales': [200, 220, 210, 215, 250, 300, 280, 270, 260, 310]
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# print(df)

# # Step 2: Shift sales data by 1 period (lagging)
df['sales_lagged_1'] = df['Sales'].shift(periods=1)


# # Step 3: Shift sales data by -1 period (leading)
df['Sales_Leading_1'] = df['Sales'].shift(periods=-1)

print(df)

# print("DataFrame with Shifted and Leading Data:")

df['Percent_Change'] = df['Sales'].pct_change()*100
print(df)

# print(df)

