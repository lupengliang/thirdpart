"""
1.异步启动进程池
2.初识回调函数
"""
import time
from multiprocessing import Pool
import os


def func(n):
    print('start func %s' % n, os.getpid())
    time.sleep(1)
    print('end func %s' % n, os.getpid())


if __name__ == '__main__':
    p = Pool(5)  # 一般情况下采用cpu数或者+1数
    for i in range(50):
        # p.apply(func, args=(i,))  # 同步提交任务,返回值是func的return值
        p.apply_async(func, args=(i,))  # 异步提交任务,返回值是一个对象,为了用户能获取func的返回值
        # get会阻塞直到对应的func执行完毕拿到结果
        # 使用apply_async给进程池分配任务
        # 需要先close后join来保持多进程和主进程代码的同步性
    p.close()  # 结束进程池接收任务
    p.join()  # 感知进程池的任务执行结束 """这里好好理解下"""


print('=====================================================')
# 回调函数是在主进程中执行的
# 通常情况下,在爬虫这里用的多点,由于网络延迟比较长
from multiprocessing import Pool


def func1(n):
    return n+1


def func2(m):
    print(m)


if __name__ == '__main__':
    p = Pool(5)
    for i in range(10, 20):
        p.apply_async(func1, args=(i,), callback=func2)  # func1的返回值作为参数传递到func2中进行使用
    p.close()
    p.join()