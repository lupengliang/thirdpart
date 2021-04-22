# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lupengliang
"""
join 用来感知一个子进程的结束
"""
import time
from multiprocessing import Process


def func(arg1, arg2):
    print('*' * arg1)
    time.sleep(5)
    print('*' * arg2)


if __name__ == '__main__':
    p = Process(target=func, args=(10, 20))
    p.start()
    print('hello world')  # 这行代码与func函数是异步的
    p.join()  # 感知一个子进程的结束，将异步的程序变为了同步
    print('====================: 运行完了')  # 由于join的存在，和之前的保持为同步
