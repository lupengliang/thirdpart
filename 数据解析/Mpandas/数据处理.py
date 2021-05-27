"""
1. 数据过滤 drop_duplicates
2. 映射 map/apply
3. 对异常值的清洗和过滤 drop
4. 排序：随机抽样出一部分数据进行排序 take
5. 分组：groupby
"""
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

df = DataFrame(data=np.random.randint(0, 100, size=(10, 6)))  # 10行6列的2维数组

# 手动将df的某几行设置成相同的内容
df.iloc[1] = [1, 1, 1, 1, 1, 1]
df.iloc[3] = [1, 1, 1, 1, 1, 1]
df.iloc[7] = [1, 1, 1, 1, 1, 1]

df.drop_duplicates(keep='first')


# 单值替换
df.replace(to_replace=4, value='four')  # 将数据4替换成four
df.replace(to_replace={3: 1}, value='one')  # 将列头为3的一列中的1替换成one


# map作映射
dic = {
    'name': ['周杰伦', '张三', '周杰伦'],
    'salary': [20000, 12000, 20000]
}
df = DataFrame(data=dic)
# 映射关系表
dic = {
    '周杰伦': 'jay',
    '张三': 'tom'
}
df['e_name'] = df['name'].map(dic)  # 新增名称对应的英文名列
print(df)

# map和apply都可以作为一种基于Series的运算工具，并且apply比map更快
# 超过300部分的钱缴纳50%的锐
def after_sal(s):
    return s - (s-3000)*0.5


# df['after_sal'] = df['salary'].map(after_sal)
df['after_sal'] = df['salary'].apply(after_sal)
print(df)


# 对异常值的清洗和过滤
# 创建一个1000行3列的df范围(0-1),求其每一列的标准差
df = DataFrame(data=np.random.random(size=[1000, 3]), columns=['A', 'B', 'C'])  # 列索引
# 对df应用筛选条件，去除标准差太大的数据，假设过滤条件为C列数据大于两倍的C列标准差
std_twice = df['C'].std()*2
indexs = df.loc[df['C'] > std_twice].index
df.drop(labels=indexs, axis=0, inplace=True)  # 0:表示行 过滤掉异常值的行
print(df)

# 总结
"""
数据清洗
1 清洗空值
    df.dropna()
    df.fillna()
2 清洗重复值
    df.drop_duplicates()
3 清洗异常值
    异常值判定的条件
    异常值对应的行数据进行删除
"""


# 排序：随机抽样出一部分数据进行排序
# 打乱数据,随机抽样 jupyter中是成功的
# s = df.take(np.random.permutation(3), axis=1).take(np.random.permutation(1000), axis=0)[0:10]  # 这里0是行，1是列
# print(s)


# 分组
df = DataFrame({'item': ['Apple', 'Banana', 'Orange', 'Banana', 'ORange', 'Apple'],
                'price': [4, 3, 3, 2.5, 4, 2],
                'color': ['red', 'yellow', 'yellow', 'green', 'green', 'green'],
                'weight': [12, 20, 50, 30, 20, 44]})
a = df.groupby(by='item', axis=0).groups  # 对item进行分组 # 使用groups查看分组的结果
print(a)
# 进行映射
s = df.groupby(by='item', axis=0)['price'].mean()  # 对item进行分组 # 使用mean查看每种水果的平均价格
print(s.to_dict())
df['mean_price'] = df['item'].map(s.to_dict())
print(df)
# 查看各种颜色水果的平均价格 24.34
