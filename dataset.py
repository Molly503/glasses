import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# 设置随机种子，确保结果可重现
np.random.seed(42)
random.seed(42)

# 生成日期范围（最近6个月）
start_date = datetime.now() - timedelta(days=180)
end_date = datetime.now()
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# 定义基础数据
countries = ['US', 'UK', 'Germany', 'France', 'Japan', 'Australia', 'Canada']
product_categories = ['Prescription Glasses', 'Sunglasses', 'Contact Lenses', 'Reading Glasses', 'Safety Glasses']
traffic_sources = ['Google Ads', 'Facebook Ads', 'Organic Search', 'Email Marketing', 'Direct', 'Affiliate']
device_types = ['Desktop', 'Mobile', 'Tablet']

# 1. 生成网站流量数据
def generate_traffic_data():
    traffic_data = []
    for date in date_range:
        for country in countries:
            for source in traffic_sources:
                for device in device_types:
                    # 模拟季节性和趋势
                    base_sessions = np.random.poisson(100)
                    if source == 'Google Ads':
                        base_sessions *= 1.5
                    elif source == 'Organic Search':
                        base_sessions *= 1.2
                    
                    traffic_data.append({
                        'date': date,
                        'country': country,
                        'traffic_source': source,
                        'device_type': device,
                        'sessions': max(1, int(base_sessions)),
                        'page_views': max(1, int(base_sessions * np.random.uniform(1.2, 3.0))),
                        'bounce_rate': np.random.uniform(0.3, 0.8),
                        'avg_session_duration': np.random.uniform(60, 300)  # 秒
                    })
    
    return pd.DataFrame(traffic_data)

# 2. 生成订单数据
def generate_order_data():
    order_data = []
    order_id = 1
    
    for date in date_range:
        # 每天的订单数量有随机性
        daily_orders = np.random.poisson(50)
        
        for _ in range(daily_orders):
            country = np.random.choice(countries)
            category = np.random.choice(product_categories)
            
            # 不同产品类别的价格区间不同
            if category == 'Prescription Glasses':
                base_price = np.random.uniform(80, 300)
            elif category == 'Sunglasses':
                base_price = np.random.uniform(50, 200)
            elif category == 'Contact Lenses':
                base_price = np.random.uniform(30, 80)
            elif category == 'Reading Glasses':
                base_price = np.random.uniform(20, 60)
            else:  # Safety Glasses
                base_price = np.random.uniform(40, 120)
            
            # 不同国家的价格调整
            country_multiplier = {
                'US': 1.0, 'UK': 0.9, 'Germany': 0.85, 'France': 0.88,
                'Japan': 1.1, 'Australia': 0.95, 'Canada': 0.92
            }
            
            final_price = base_price * country_multiplier[country]
            
            order_data.append({
                'order_id': order_id,
                'date': date,
                'country': country,
                'product_category': category,
                'order_value': round(final_price, 2),
                'quantity': np.random.choice([1, 2, 3], p=[0.7, 0.25, 0.05]),
                'customer_type': np.random.choice(['New', 'Returning'], p=[0.6, 0.4]),
                'payment_method': np.random.choice(['Credit Card', 'PayPal', 'Bank Transfer'], p=[0.6, 0.3, 0.1]),
                'shipping_cost': round(np.random.uniform(5, 25), 2),
                'delivery_days': np.random.choice(range(3, 15))
            })
            order_id += 1
    
    return pd.DataFrame(order_data)

# 3. 生成客户数据
def generate_customer_data():
    customer_data = []
    customer_id = 1000
    
    for _ in range(2000):  # 生成2000个客户
        registration_date = start_date + timedelta(
            days=np.random.randint(0, (end_date - start_date).days)
        )
        
        customer_data.append({
            'customer_id': customer_id,
            'registration_date': registration_date,
            'country': np.random.choice(countries),
            'age_group': np.random.choice(['18-25', '26-35', '36-45', '46-55', '55+']),
            'gender': np.random.choice(['M', 'F', 'Other'], p=[0.45, 0.5, 0.05]),
            'acquisition_channel': np.random.choice(traffic_sources),
            'email_subscribed': np.random.choice([True, False], p=[0.7, 0.3]),
            'total_orders': np.random.poisson(3) + 1,
            'lifetime_value': round(np.random.uniform(50, 800), 2)
        })
        customer_id += 1
    
    return pd.DataFrame(customer_data)

# 4. 生成A/B测试数据
def generate_ab_test_data():
    ab_test_data = []
    
    # 模拟一个产品页面的A/B测试
    for date in date_range[-30:]:  # 最近30天的测试
        for variant in ['A', 'B']:
            sessions = np.random.poisson(200)
            # B版本转化率稍高
            conversion_rate = 0.05 if variant == 'A' else 0.065
            conversions = np.random.binomial(sessions, conversion_rate)
            
            ab_test_data.append({
                'date': date,
                'test_name': 'Product_Page_Redesign',
                'variant': variant,
                'sessions': sessions,
                'conversions': conversions,
                'conversion_rate': conversions / sessions if sessions > 0 else 0,
                'revenue': round(conversions * np.random.uniform(80, 150), 2)
            })
    
    return pd.DataFrame(ab_test_data)

# 生成所有数据集
print("生成网站流量数据...")
traffic_df = generate_traffic_data()

print("生成订单数据...")
orders_df = generate_order_data()

print("生成客户数据...")
customers_df = generate_customer_data()

print("生成A/B测试数据...")
ab_test_df = generate_ab_test_data()

# 保存为CSV文件
traffic_df.to_csv('website_traffic.csv', index=False)
orders_df.to_csv('orders.csv', index=False)
customers_df.to_csv('customers.csv', index=False)
ab_test_df.to_csv('ab_test_results.csv', index=False)

print("\n数据集生成完成！")
print("="*50)
print("数据集概览：")
print(f"1. 网站流量数据: {len(traffic_df)} 行")
print(f"2. 订单数据: {len(orders_df)} 行")  
print(f"3. 客户数据: {len(customers_df)} 行")
print(f"4. A/B测试数据: {len(ab_test_df)} 行")
print("="*50)

# 显示每个数据集的前几行
print("\n各数据集预览：")
print("\n1. 网站流量数据 (前5行):")
print(traffic_df.head())

print("\n2. 订单数据 (前5行):")
print(orders_df.head())

print("\n3. 客户数据 (前5行):")
print(customers_df.head())

print("\n4. A/B测试数据 (前5行):")
print(ab_test_df.head())