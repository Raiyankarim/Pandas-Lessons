import pandas as pd

data = {
    'Country': ['USA', 'USA', 'India', 'India', 'Canada', 'Canada'],
    'City': ['New York', 'Chicago', 'Mumbai', 'Delhi', 'Toronto', 'Vancouver'],
    'Population': [8500000, 2700000, 20000000, 18000000, 2900000, 2500000]
}

df = pd.DataFrame(data)
# print(df)

#multi-level indexing
df.set_index(['Country', 'City'],inplace=True)

# print(df.reset_index(inplace=True))

print(df)
