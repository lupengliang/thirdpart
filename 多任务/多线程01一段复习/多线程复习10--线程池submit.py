"""
使用线程池 submit的使用
备注:
    func函数有返回值的情况下,注释shutdown()
"""
import time
from concurrent.futures import ThreadPoolExecutor


def func(n):
    time.sleep(2)
    print(n)
    return n


tpool = ThreadPoolExecutor(max_workers=5)  # max_workers 最大线程数 不要超过cpu个数*5
t_lst = []
for i in range(20):
    t = tpool.submit(func, i)  # 提交了20个任务,一次执行5个线程
    t_lst.append(t)
# tpool.shutdown()  # close 关闭池子,不让任务进来 + join 阻塞直到债务执行完
print('主线程')
for t in t_lst: print('*******', t.result())  # t.result()  取func的返回值
