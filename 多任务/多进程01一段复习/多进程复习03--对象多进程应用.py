"""
应用:面向对象开启多进程

参数不一样的情况不,如何使用for循环创建多个?好好想下
"""
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, arg1, arg2):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2

    def run(self):
        print(self.pid)  # 查看进程号,与os.pid的功能一样
        print(self.name)  # 进程的名字
        print(self.arg1)
        print(self.arg2)


if __name__ == '__main__':
    p1 = MyProcess(1, 2)
    p1.start()
    p2 = MyProcess(4, 1)
    p2.start()
