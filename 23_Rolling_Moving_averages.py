import pandas as pd
import matplotlib.pyplot as plt
# Step 1: Create sample data
data = {
    'Date': pd.date_range(start='2025-01-01', periods=10, freq='D'),
    'Sales': [200, 220, 210, 215, 250, 300, 280, 270, 260, 310]
}

df = pd.DataFrame(data)

# Step 2: Set 'Date' column as the index
df.set_index('Date', inplace=True)

# Step 3: Calculate rolling average with a window size of 3
df['Rolling_Avg'] = df['Sales'].rolling(window=3).mean()

print("DataFrame with Rolling Average:")
print(df)

##Exponential Moving Average

df['EMA'] = df['Sales'].ewm(span=3, adjust=False).mean()

print(df)

print(plt.plot(df['Sales'], label='Sales'))

##print rolling average and EMA in same plot

print(plt.plot(df['Rolling_Avg'], label='Rolling Average'))
print(plt.plot(df['EMA'], label='EMA'))


plt.legend()

