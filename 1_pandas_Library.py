import pandas as pd
print(pd.__version__)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

dataframe = pd.DataFrame(data)
print(dataframe)
