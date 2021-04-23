# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lupengliang
import os
import time
from multiprocessing import Process


def func(arg, args2):
    print(arg, args2)
    time.sleep(1)
    print('子进程：', os.getpid())
    print(54321)


if __name__ == '__main__':
    # p是一个进程对象，还没有启动进程
    p = Process(target=func, args=('参数1', '参数2'))  # 注册 多个参数
    p.start()  # 开启了一个子进程
    print('*' * 10)  # 与函数同时执行
    print('父进程: ', os.getpid())  # 查看当前进程的进程号
    print('父进程的父进程：', os.getppid())  # 查看当前进程的父进程号，就是pycharm的进程号
