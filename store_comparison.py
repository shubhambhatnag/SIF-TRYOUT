import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('data/train.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Calculate average weekly sales per store
avg_sales_per_store = df.groupby('Store')['Weekly_Sales'].mean().sort_values(ascending=False)

# Visualize average sales per store
plt.figure(figsize=(12, 6))
sns.barplot(x=avg_sales_per_store.index, y=avg_sales_per_store.values)
plt.title('Average Weekly Sales by Store', fontsize=18)
plt.xlabel('Store ID', fontsize=16)
plt.ylabel('Average Weekly Sales', fontsize=16)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('graphs/avg_sales_per_store.png')


# Time series of sales for top 5 stores
top_5_stores = avg_sales_per_store.head().index
plt.figure(figsize=(12, 6))
for store in top_5_stores:
    store_data = df[df['Store'] == store].groupby('Date')['Weekly_Sales'].sum()
    plt.plot(store_data.index, store_data.values, label=f'Store {store}')

plt.title('Weekly Sales Over Time for Top 5 Stores')
plt.xlabel('Date')
plt.ylabel('Weekly Sales')
plt.legend()
plt.tight_layout()
plt.savefig('graphs/top_5_stores_sales.png')