import pandas as pd
data = [10, 20, 30, 40]
index = ['a', 'b', 'c', 'd']
series = pd.Series(data)
# print(series)
print(series.index)
print(series.dtypes)