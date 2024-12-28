import pandas as pd

df = pd.read_csv("C:/Users/Admin/Downloads/employee_data.csv")

#print(df.head())
#print('----------[1]---------')
#print(df.info())
#print('----------[2]---------')
#print(df.describe())
#print('----------[3]---------')
names = df['이름']
#print(names.head())


first_row = df.iloc[0]

older_than_30 = df[df['나이'] > 30]
#print(df['나이'] > 30)
#print(older_than_30.head())

grouped_df = df.groupby('부서')['나이'].mean()
#print(grouped_df)

print(df.isnull().sum());