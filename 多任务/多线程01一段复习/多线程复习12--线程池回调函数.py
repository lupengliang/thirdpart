"""
线程池回调函数
"""
import time
from concurrent.futures import ThreadPoolExecutor


def func(n):
    time.sleep(2)
    print(n)
    return n


def call_back(m):
    print('结果是%s' % m.result())
    return m


tpool = ThreadPoolExecutor(max_workers=5)
t_lst = []
for i in range(20):
    t = tpool.submit(func, i)
    t.add_done_callback(call_back)  # 提交了20个任务,一次性执行5个线程
    t_lst.append(t)
# tpool.shutdown() # close 关闭池子 + join 将线程变为同步
print('主线程')
for t in t_lst: print('*******', t.result())
