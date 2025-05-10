import pandas as pd

# Load data
df = pd.read_csv('../data/sales_data.csv')

# Basic cleaning
df['Date'] = pd.to_datetime(df['Date'])
df['TotalSales'] = df['UnitsSold'] * df['UnitPrice']

# Save cleaned data
df.to_csv('../data/cleaned_sales_data.csv', index=False)
print("Cleaned data saved.")
