import pandas as pd
df = pd.read_csv('8_Employee.csv',index_col='name',sep = ',',usecols=['id','name', 'department'])
print(df.head())
