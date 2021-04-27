"""
守护线程的使用

注意:守护线程与守护进程的区别
"""
import time
from threading import Thread


def func1():
    while True:
        print('*' * 10)
        time.sleep(1)


def func2():
    print('in func2')
    time.sleep(5)

t = Thread(target=func1,)
t.daemon = True  # 设置为守护线程
t.start()

t2 = Thread(target=func2,)
t2.start()
print('主线程')

# 备注:
# 守护进程随着主进程代码的执行结束而结束
# 守护线程会在主线程结束之后等等其它子线程的结束后才结束