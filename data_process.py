countries = ['US', 'UK', 'Germany', 'France']
user_data = {
    'name': 'John',
    'country': 'US',
    'orders': 5
}

for country in countries:
    if country == 'US':
        print(f"{country}: 主要市场")
    else:
        print(f"{country}: 次要市场");

        import pandas as pd

# 1. 读取我们生成的数据
orders_df = pd.read_csv('orders.csv')

traffic_df = pd.read_csv('website_traffic.csv')

print("数据形状:", orders_df.shape)
print("数据类型:", orders_df.dtypes)
print("缺失值:", orders_df.isnull().sum())
print("数据预览:", orders_df.head())

# 筛选美国订单
us_orders = orders_df[orders_df['country'] == 'US']

print(us_orders)

# 在VSCode中创建新文件，保存为：
