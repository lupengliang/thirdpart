# 进程与进程之间的数据隔离问题,多进程之间数据不经过处理,数据是隔离的
# 就是说父进程的变量与子进程的变量不是一个值,例子如下
"""
结论: 子进程的变量与主进程的变量不是同一个值
"""
import os
from multiprocessing import Process


def func():
    global n
    n = 0
    print('子进程pid: %s' % os.getpid(), n)


if __name__ == '__main__':  # windows下的多进程必须写这个
    n = 100
    p1 = Process(target=func)
    p1.start()
    print("主进程pid:", os.getpid(), n)
