import pandas as pd
import matplotlib.pyplot as plt

df_sales = pd.read_csv('../dimension_fact_tables/salesfacts.csv')
df_time = pd.read_csv('../dimension_fact_tables/timedimension.csv')

df = pd.merge(df_sales, df_time, on='time_key', how='left')

df['year_quarter'] = df['year'].astype(str) + '-Q' + df['quarter'].astype(str)

quarterly_sales = df.groupby('year_quarter')['sale_amount'].sum()
quarterly_costs = df.groupby('year_quarter')['purchase_cost'].sum()
quarterly_profit = df.groupby('year_quarter')['profit'].sum()

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(quarterly_sales.index, quarterly_sales.values, marker='o', color='blue')
plt.title('Total Sales Amount by Year-Quarter')
plt.ylabel('Total Sales Amount')

plt.subplot(3, 1, 2)
plt.plot(quarterly_costs.index, quarterly_costs.values, marker='o', color='orange')
plt.title('Total Purchase Cost by Year-Quarter')
plt.ylabel('Total Purchase Cost')

plt.subplot(3, 1, 3)
plt.plot(quarterly_profit.index, quarterly_profit.values, marker='o', color='green')
plt.title('Total Profit by Year-Quarter')
plt.xlabel('Year-Quarter')
plt.ylabel('Total Profit')

plt.tight_layout()
plt.show()
