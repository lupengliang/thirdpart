"""
面向对象使用多线程
"""
import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, arg):
        super().__init__()  # 重写父类的__init__方法
        self.arg = arg

    def run(self):
        time.sleep(1)
        print(self.arg)


t = MyThread(10)  # 创建线程对象
t.start()  # 启动线程