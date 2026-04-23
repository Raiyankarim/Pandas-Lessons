import pandas as pd

# Sample data
data = {
    'Date': ['2025-01-01', '2025-01-01', '2025-01-02', '2025-01-02', '2025-01-03'],
    'Region': ['East', 'West', 'East', 'West', 'East'],
    'Product': ['Laptop', 'Tablet', 'Laptop', 'Tablet', 'Phone'],
    'Sales': [1000, 700, 1200, 800, 600]
}

df = pd.DataFrame(data)
print(df)


pivot = pd.pivot_table(df, 
                       values='Sales', 
                       index='Region', 
                       columns='Product', 
                       aggfunc='sum', 
                       fill_value=0,
                       margins=True,
                       margins_name='Total Sales')

print(pivot)

# # Pivot table with multiple aggregation functions
# pivot = pd.pivot_table(df, 
#                        values='Sales', 
#                        index='Region', 
#                        columns='Product', 
#                        aggfunc={'Sales': ['sum', 'mean', 'count']}, 
#                        fill_value=0)

# print(pivot)


# # Pivot table with custom aggregation function
# def custom_sum(x):
#     return sum(x) / len(x)

# pivot = pd.pivot_table(df, 
#                        values='Sales', 
#                        index='Region', 
#                        columns='Product', 
#                        aggfunc=custom_sum, 
#                        fill_value=0)

# print(pivot)