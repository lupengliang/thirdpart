"""
锁 保障数据安全
"""
import time
from threading import Lock, Thread  # 互斥锁


def func(lock):
    global n
    lock.acquire()
    temp = n
    time.sleep(0.2)
    print('hello world %s' % n)
    n = temp - 1
    lock.release()


n = 10
t_lst = []
lock = Lock()
for i in range(10):
    t = Thread(target=func, args=(lock,))
    t.start()
    t_lst.append(t)
for t in t_lst: t.join()
print(n)