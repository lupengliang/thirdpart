"""
多进程中的组件
信号量
使用场景:
    ktv 上厕所
    4 个
    一套资源,同一时间 只能被n个人访问
    某一段代码 同一时间 只能被n个进程执行
"""
import time
import random
from multiprocessing import Process
from multiprocessing import Semaphore


def ktv(i, sem):
    sem.acquire()  # 获取钥匙
    print('\033[1;32m%s走进ktv\033[0m' % i)
    time.sleep(random.randint(1, 5))
    print('\033[1;31m%s走出ktv\033[0m' % i)
    sem.release()  # 还钥匙


if __name__ == '__main__':
    sem = Semaphore(4)  # 这里的这个数字,相当于一个门有4把钥匙,这个房间只能当其中的1个人出来时,第5个人才能进去
    for i in range(20):
        p = Process(target=ktv, args=(i, sem))
        p.start()
