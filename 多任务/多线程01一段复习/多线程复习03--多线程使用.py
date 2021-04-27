"""
多线程初步使用
    join() 用法
"""
import os
from threading import Thread


# 功能: 为了看到print(g) == 0 join用法  这里不用join,结果是错的
def func(a, b):
    global g
    g = 0
    print(g, os.getpid())

g = 100
t_lst = []
for i in range(10):
    t = Thread(target=func, args=(i, 5))  # 创建线程对象
    t.start()  # 启动线程
    t_lst.append(t)
for t in t_lst: t.join()  # 我理解join的意思就是等待大家一直结束后,再执行后续的代码
print(g)


