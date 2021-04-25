"""
开启多进程:第二种方法面向对象
备注:
    自定义类  继承Process类
    必须实现一个run方法,run方法中是在子进程中执行的代码
"""
import os
from multiprocessing import Process


class MyProcess(Process):

    def run(self):
        print(os.getpid())  # 打印当前进程的id


if __name__ == '__main__':
    print("主进程:", os.getpid())
    p1 = MyProcess()
    p1.start()
    p2 = MyProcess()
    p2.start()
