"""
事件:
    通过一个信号 来控制 多个进程 同时 执行或者阻塞
    实例: 红绿灯事件
e = Event()   # 事件
print(e.is_set())  # 查看一个事件的状态,默认设置成阻塞False
e.set()  # 将这个事件的状态改为True
print(e.is_set())
e.wait()  # 是依据e.is_set()的值决定是否阻塞的
print(123456)
e.clear()  # 将这个事件的状态改为False
print(e.is_set())
e.wait()
print('*' * 10)
备注:
    set 和 clear 分别用来修改一个事件的状态, True或者False
    is_set 用来查看一个事件的状态
    wait 是依据事件的状态来决定自己是否阻塞
        False 阻塞 True 不阻塞
    # 一个信号可以使所有的进程都进入阻塞状态,也可以控制所有的进程解除阻塞
    # 一个事件被创建之后,默认是阻塞状态
"""
import random
from multiprocessing import Event, Process
import time


def cars(e, i):
    if not e.is_set():
        print('car%i在等待' % i)
        e.wait()  # 阻塞,直到得到一个状态变为True的信号
    print('\033[1;32;40m cat%i通过\033[0m' % i)


def light(e):
    while True:
        if e.is_set():
            e.clear()
            print('\033[31m红灯亮了\033[0m')
        else:
            e.set()
            print('\033[32m绿灯亮了\033[0m')
        time.sleep(2)


if __name__ == '__main__':
    e = Event()
    traffic = Process(target=light, args=(e,))
    traffic.start()
    for i in range(20):  # 表示有20个车
        car = Process(target=cars, args=(e, i))
        car.start()
        time.sleep(random.random())

