"""
线程模块 thread threading Queue  中,threading更为优秀一点
"""
import time
from threading import Thread


# 多线呢并发
def func(n):
    time.sleep(1)
    print(n)


for i in range(10):  # 共0个线程
    t = Thread(target=func, args=(i,))  # 创建线程对象
    t.start()  # 开启线程,实现并发