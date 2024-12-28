import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Admin/Desktop/vs-code project/my-py/data.csv')
print(df)

df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
monthly_data = df.resample('M').sum()

print(monthly_data)

plt.figure(figsize=(10,6))
plt.plot(monthly_data.index, monthly_data['value'], marker='o')
plt.title('Monthly Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()