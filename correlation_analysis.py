import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
sales_data = pd.read_csv('data/train.csv')
features_data = pd.read_csv('data/features.csv')

# Convert Date to datetime
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
features_data['Date'] = pd.to_datetime(features_data['Date'])

# Merge data on Store and Date
merged_data = pd.merge(sales_data, features_data, on=['Store', 'Date'])

# Calculate correlation matrix
correlation_matrix = merged_data[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']].corr()

# Plot correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation between Sales and Features')

plt.savefig('graphs/correlation_heatmap.png')



# Scatter plots to visualize relationships
features = ['Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
for feature in features:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=merged_data, x=feature, y='Weekly_Sales')
    plt.title(f'Sales vs {feature}')
    plt.xlabel(feature)
    plt.ylabel('Weekly Sales')
    plt.show()
