import pandas as pd


# Step 1: Create a fixed sample DataFrame
data = {
    'DateTime': pd.date_range(start='2025-01-01', periods=10, freq='D'),
    'City': ['New York', 'Chicago', 'Los Angeles', 'New York', 'Chicago',
             'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'New York'],
    'Sales': [1200, 800, 1500, 600, 750, 1700, 950, 1800, 500, 1300]
}

df = pd.DataFrame(data)


# print(df.info())
# # Step 2: Convert 'DateTime' column to DateTime format
df['DateTime'] = pd.to_datetime(df['DateTime'])

# # Step 3: Set 'DateTime' column as the index
df.set_index('DateTime', inplace=True)

print(df)

# print("Original DataFrame:")
# print(df)

# Step 4: Filter data for a specific date range
filtered_df = df.loc['2025-01-03':'2025-01-07']
print("Filtered Data (Between 2025-01-03 and 2025-01-07):")
print(filtered_df)

# # Step 5: Access data by year, month, and day
print("Data for January 2025:")
print(df.loc['2025-01'])

# Step 6: Extract specific year and month using attributes
df['Year'] = df.index.year
df['Month'] = df.index.month


# print("DataFrame after extracting Year and Month:")
print(df)