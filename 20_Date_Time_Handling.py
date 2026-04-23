#Date and Time Handling
import pandas as pd

# Create date series
dates = pd.to_datetime(['2025-01-01', '2025-02-15', '2025-03-20'])
# print(dates)

# Create date range
start_date = pd.to_datetime('2025-01-01')
end_date = pd.to_datetime('2025-12-31')
date_range = pd.date_range(start=start_date, end=end_date,freq='M')
# print(date_range)

#Extract Year, Month, and Day
df = pd.DataFrame(date_range, columns=['Date'])
print(df)

df['new_date'] = df['Date'] +pd.Timedelta(days=10)

print(df)

# print(df['Date'].dt.year)
# print(df['Date'].dt.month)
# print(df['Date'].dt.day)

# dt.date
# dt.year
# dt.month

#Generating Data Range
# data = pd.date_range(start='2025-01-01', periods=10,freq="D")
# print(data)

