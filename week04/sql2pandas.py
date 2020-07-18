# coding=utf-8
"""
将以下的 SQL 语句翻译成 pandas 语句
"""
import pandas as pd
import numpy as np

# 数据准备
str = ['xiaomi', 'iPhone', 'huawei', 'vivo']
# 订单表，记录用户订单数据
orders = pd.DataFrame({
    'id': range(1, 11),
    'createdate': pd.date_range('2020-07-01', periods=10),
    'name': [str[x] for x in np.random.randint(1, len(str), 10)],
    'userid': range(1001, 1011)
})
# 用户表，记录用户信息
user = pd.DataFrame({
    'userid': range(1001, 1011),
})

# print(orders)

## 1. SELECT * FROM data;
order_by = orders.sort_values(by='createdate', ascending=False)
# print(order_by)

## 2.SELECT * FROM data LIMIT 10
top_orders = orders.head(10)
# print(top_orders)
top_ordes2 = orders[:10]
# print(top_ordes2)

## 3.SELECT id FROM data;
id_orders = orders['id']
# print(id_orders)

## 4.SELECT COUNT(id) FROM data;
count_id = orders['id'].count()
# print(count_id)

## 5. SELECT * FROM data WHERE id<1000 AND age>30;
##  转化为本地sql  SELECT * FORM orders WHERE id >5 AND name='huawei';

new_order = orders.query('(id>5)&(name=="huawei")')
# print(new_order)

orders1 = orders['id'] > 5
orders2 = orders['name'] == 'huawei'
new_o = orders[orders1 & orders2]
# print(new_o)

new_orders1 = orders['id'].map(lambda x: x > 5)
new_orders2 = orders['name'].map(lambda n: n == 'huawei')
new_orders = orders[new_orders1 & new_orders2]
# print(f'多条件：{new_orders}')



## 6.SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
order6 = orders.groupby('id').agg({'name': 'count'})
# print(order6)

## 7.SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
inndata = pd.merge(orders, user, on='userid', how='inner')
# print(inndata)

## 8.SELECT * FROM table1 UNION SELECT * FROM table2;
data1 = pd.DataFrame({
    'A': ['a', 'b', 'c'],
    'B': [1, 2, 4]
})
data2 = pd.DataFrame({
    'A': ['a', 12, 'c'],
    'B': [1, 2, 'ni']
})

union_data = pd.concat([data1, data2])
# print(union_data)

## 9. DELETE FROM table1 WHERE id=10;
# del_orders = orders.drop(6)
del_orders = orders.drop(orders[orders['id'] == 6].index)
# print(del_orders)

## 10.ALTER TABLE table1 DROP COLUMN column_name;
drop_orders = orders.drop('createdate', axis=1)
# print(drop_orders)
