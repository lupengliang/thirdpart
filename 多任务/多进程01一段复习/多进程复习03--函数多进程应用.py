"""
练习1: 使用第一种方法
开启多个子进程
    同步: 0.1*500 = 50
    异步: 500 0.1 = 0.1
    多进程写文件
    首先往文件夹中写文件
    向用户展示写入文件之后文件夹所有的文件名
"""
import os
from multiprocessing import Process


def func(filename, content):
    with open(filename, 'w') as f:
        f.write(content*10*"*")


if __name__ == '__main__':
    p_lst = []
    for i in range(10):
        p = Process(target=func, args=("info%s" % i, 20*i))
        p_lst.append(p)
        p.start()
    [p.join() for p in p_lst]  # 前面为异步,后面为同步
    # 之前的所有进程必须在这里都执行完才能执行下面的代码
    print([i for i in os.walk(r'D:\TOOLS\多任务\多进程01一段复习')])
