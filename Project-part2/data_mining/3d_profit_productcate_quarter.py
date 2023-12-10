import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df_sales = pd.read_csv('../dimension_fact_tables/salesfacts.csv')
df_product = pd.read_csv('../dimension_fact_tables/productdimension.csv')
df_time = pd.read_csv('../dimension_fact_tables/timedimension.csv')

df = pd.merge(df_sales, df_product, on='product_key', how='left')

df = pd.merge(df, df_time, on='time_key', how='left')
df['year_quarter'] = df['year'].astype(str) + '-Q' + df['quarter'].astype(str)

def convert_quarter_to_float(year_quarter):
    year, quarter = year_quarter.split('-Q')
    quarter_number = float(quarter)
    return float(year) + (quarter_number - 1) / 4

df['year_quarter_float'] = df['year_quarter'].apply(convert_quarter_to_float)

product_type_mapping = {name: i for i, name in enumerate(df['product_type_name'].unique())}
df['product_type_id'] = df['product_type_name'].map(product_type_mapping)

grouped_data = df.groupby(['year_quarter_float', 'product_type_id', 'product_type_name'])['profit'].sum().reset_index()

print(grouped_data.head())

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for ctype in grouped_data['product_type_id'].unique():
    df_subset = grouped_data[grouped_data['product_type_id'] == ctype]
    ax.scatter(df_subset['year_quarter_float'], df_subset['product_type_id'], df_subset['profit'], label=ctype)

quarter_float_to_str = {float_val: str_val for str_val, float_val in df[['year_quarter', 'year_quarter_float']].drop_duplicates().values}
ax.set_xticks(list(quarter_float_to_str.keys()))
ax.set_xticklabels(list(quarter_float_to_str.values()), rotation=45)

ax.set_yticks(list(product_type_mapping.values()))
ax.set_yticklabels(list(product_type_mapping.keys()))


ax.set_xlabel('Year-Quarter')
ax.set_ylabel('Product Type ID')
ax.set_zlabel('Profit')
plt.title('Profit by product Type and Quarter')

ax.legend()

plt.show()
