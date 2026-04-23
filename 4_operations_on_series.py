import pandas as pd
data = [10, 20, 30, 40]
index = ['a', 'b', 'c', 'd']
series = pd.Series(data,index=index)
print(series)

# addition = series + 2
# print(addition)

# subtraction = series - 2
# print(subtraction)

# multiple_of_three = series.apply(lambda x: x * 3)
# print(multiple_of_three)

mean_series = series.mean()
median_series = series.median()
print(f"Mean: {mean_series}")
print(f"Median: {median_series}")
count_series = series.count()
print(f"Count: {count_series}")