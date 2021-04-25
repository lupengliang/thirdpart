import time
from multiprocessing import Process
"""
开启多个子进程,第一种方式
"""


def func(arg1, arg2):
    print("*"*arg1)
    time.sleep(5)
    print("*"*arg2)


if __name__ == '__main__':
    # p = Process(target=func, args=(10, 20))  # 创建一个进程对象
    # p.start()  # 启动一个进程
    # p1 = Process(target=func, args=(10, 20))  # 创建...
    # p1.start()  # 启动
    # p2 = Process(target=func, args=(10, 20))  # 创建
    # p2.start()  # 启动
    # p3 = Process(target=func, args=(10, 20))  # 创建
    # p3.start()  # 启动

    p_lst = []
    for i in range(10):
        p = Process(target=func, args=(10*i, 20*i))  # 创建10个进程对象,i控制进程个数
        p_lst.append(p)
        p.start()  # 启动
    [p.join() for p in p_lst]  # 前面的为异步,后面的为同步
    # p.join()  # 变成同步,慢,异步,快
    print('运行完了')
