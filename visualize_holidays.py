import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/train.csv')


df['Date'] = pd.to_datetime(df['Date'])


sales_by_date = df.groupby('Date')['Weekly_Sales'].sum().reset_index()

plt.figure(figsize=(15, 7))
plt.plot(sales_by_date['Date'], sales_by_date['Weekly_Sales'], label='Weekly Sales')

holiday_sales = sales_by_date[df['IsHoliday'] == True]
plt.scatter(holiday_sales['Date'], holiday_sales['Weekly_Sales'], color='red', label='Holidays', zorder=5)


plt.title('Weekly Sales (Holidays Highlighted)')
plt.xlabel('Date')
plt.ylabel('Weekly Sales')
plt.legend()


plt.savefig('graphs/weekly_sales_holidays.png')

