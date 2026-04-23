import pandas as pd
# Create a sample DataFrame with datetime data
data = {
    'Event': ['Conference', 'Meeting', 'Workshop', 'Webinar'],
    'Date': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df) 
# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
print("\nDataFrame after converting 'Date' to datetime:")
print(df)
# Extracting year, month, and day from the 'Date' column
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
print("\nDataFrame after extracting year, month, and day:")
print(df)
# Filtering events that occur in February
feb_events = df[df['Date'].dt.month == 2]
print("\nEvents that occur in February:")
print(feb_events)
