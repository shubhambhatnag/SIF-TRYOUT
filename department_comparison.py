import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('data/train.csv')

# Aggregate sales by department
dept_sales = df.groupby('Dept')['Weekly_Sales'].sum().sort_values(ascending=False)

# Time series for top 5 departments
top_5_depts = dept_sales.head(5).index

# Prepare data for time series plot
df['Date'] = pd.to_datetime(df['Date'])
df_top5 = df[df['Dept'].isin(top_5_depts)]

# Aggregate weekly sales for top 5 departments
weekly_sales = df_top5.groupby(['Date', 'Dept'])['Weekly_Sales'].sum().unstack()

# Plot time series
plt.figure(figsize=(15, 7))
for dept in top_5_depts:
    plt.plot(weekly_sales.index, weekly_sales[dept], label=f'Dept {dept}')

plt.title('Weekly Sales Trends for Top 5 Departments')
plt.xlabel('Date')
plt.ylabel('Weekly Sales ($)')
plt.legend()
plt.tight_layout()

plt.savefig('graphs/top_5_depts_sales.png')