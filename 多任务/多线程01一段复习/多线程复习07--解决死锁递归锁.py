"""
递归锁的使用
"""
import time
from threading import RLock  # 递归锁  一串钥匙
from threading import Thread

noodle_lock = fork_lock = RLock()


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
Thread(target=eat1, args=('bossjin',)).start()
Thread(target=eat2, args=('nezha',)).start()
