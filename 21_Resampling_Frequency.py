import pandas as pd

# Step 1: Create a fixed sample DataFrame
data = {
    'DateTime': pd.date_range(start='2025-01-01', periods=10, freq='D'),
    'Sales': [100, 200, 150, 400, 300, 250, 500, 450, 600, 550]
}

df = pd.DataFrame(data)

# print(df)

df.set_index('DateTime', inplace=True)

print(df)

#resampling

df_weekly = df.resample('W').median()

df_daily =df.resample('D')

print(df_daily.agg({'Sales': ['mean']}))



