import pandas as pd
import matplotlib.pyplot as plt

df_sales = pd.read_csv('../dimension_fact_tables/salesfacts.csv')
df_products = pd.read_csv('../dimension_fact_tables/productdimension.csv')
df_customers = pd.read_csv('../dimension_fact_tables/customerdimension.csv')

product_order_counts = df_sales.groupby('product_key')['order_quantity'].sum()
product_order_counts = product_order_counts.reset_index()
product_order_counts = product_order_counts.merge(df_products, on='product_key')
product_type_orders = product_order_counts.groupby('product_type_name')['order_quantity'].sum()

customer_order_counts = df_sales.groupby('customer_key')['order_quantity'].sum()
customer_order_counts = customer_order_counts.reset_index()
customer_order_counts = customer_order_counts.merge(df_customers, on='customer_key')
customer_type_orders = customer_order_counts.groupby('customer_type_name')['order_quantity'].sum()

plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1)
plt.pie(product_type_orders, labels=product_type_orders.index, autopct='%1.1f%%', startangle=90)
plt.title('Order Share by Product Type')

plt.subplot(1, 2, 2)
plt.pie(customer_type_orders, labels=customer_type_orders.index, autopct='%1.1f%%', startangle=90)
plt.title('Order Share by Customer Type')

plt.tight_layout()
plt.show()
