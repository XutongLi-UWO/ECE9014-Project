import pandas as pd
import matplotlib.pyplot as plt

df_sales = pd.read_csv('../dimension_fact_tables/salesfacts.csv')
df_time = pd.read_csv('../dimension_fact_tables/timedimension.csv')

df = pd.merge(df_sales, df_time, on='time_key', how='left')

df['year_quarter'] = df['year'].astype(str) + '-Q' + df['quarter'].astype(str)

quarterly_orders = df.groupby('year_quarter')['order_quantity'].sum()

plt.figure(figsize=(10, 6))

plt.plot(quarterly_orders.index, quarterly_orders.values, marker='o', linestyle='-', color='purple')
plt.title('Total Order Quantity by Year-Quarter')
plt.xlabel('Year-Quarter')
plt.ylabel('Total Order Quantity')

plt.show()
