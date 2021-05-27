"""
1. 级联
2. 合并
"""
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# 级联：匹配级联
df1 = DataFrame(data=np.random.randint(0, 100, size=(3,3)), index=['a', 'b', 'c'])
df2 = DataFrame(data=np.random.randint(0, 100, size=(3,3)), index=['a', 'd', 'c'])
print(pd.concat((df1, df1), axis=0))  # 0: 列与列级联

# 级联：不匹配级联
print(pd.concat((df1, df2), axis=0, join='inner'))


# 重点合并： 一对一合并


# 重点合并： 一对一合并
# 重点合并： 一对一合并
# 重点合并： 一对一合并
# 重点合并： 一对一合并

