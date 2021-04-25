"""
守护进程:
    设置子进程为守护进程,这样主进程的代码执行完毕后,子进程也停止
备注:
    1.守护进程会随着主进程的代码执行完毕而结束
    2.在主进程内结束一个子进程  p.terminate()
        备注: 结束一个进程不是在执行方法之后.而是需要有一个操作系统响应的过程
    3.检验一个进程是否活着的状态 p.is_alive()
    4.获取当前进程的名字 p.name
    5.获取当前进程的进程号 p.pid
"""
import time
from multiprocessing import Process


def func():
    while True:
        time.sleep(0.2)
        print('我还活着')


def func2():
    print('in func2 start')
    time.sleep(8)
    print('in func2 finished')


if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True  # 设置子进程为守护进程,这样主进程的代码执行完毕后,子进程也停止
    p.start()
    p2 = Process(target=func2)
    p2.start()  # 普通进程
    # p2.terminate()  # 结束一个子进程,操作系统并不会立即关闭
    print(p2.is_alive())  # 检验一个进程是否还活着
    time.sleep(5)
    print(p2.is_alive())
    i = 0
    while i < 5:
        print('主进程: 我是socket server')
        time.sleep(1)
        i += 1
