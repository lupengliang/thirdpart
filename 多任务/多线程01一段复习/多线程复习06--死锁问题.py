"""
死锁问题演示 -- 科学家吃面
"""
import time
from threading import Lock, Thread  # 互斥锁


noodle_lock = Lock()
fork_lock = Lock()


def eat1(name):
    noodle_lock.acquire()
    print('%s拿到面条啦' % name)
    fork_lock.acquire()
    print('%s拿到叉子了' % name)
    print('%s吃面' % name)
    fork_lock.release()
    noodle_lock.release()


def eat2(name):
    fork_lock.acquire()
    print('%s拿到叉子了' % name)
    time.sleep(1)
    noodle_lock.acquire()
    print('%s拿到面条啦' % name)
    print('%s吃面' % name)
    noodle_lock.release()
    fork_lock.release()


Thread(target=eat1, args=('alex',)).start()
Thread(target=eat2, args=('Egon',)).start()
Thread(target=eat1, args=('Bosslu',)).start()
Thread(target=eat2, args=('Kugong',)).start()
# 结果出现阻塞现象 一个把叉子拿走了,一个把面拿走了
