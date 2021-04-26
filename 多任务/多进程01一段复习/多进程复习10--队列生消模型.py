"""
队列应用:
    经典模型:生产者与消费者模型
    生产者: 进程
    消费者: 进程
"""
import time
import random
from multiprocessing import Process,Queue


# 消费者
def consumer(q, name):
    while True:
        food = q.get()
        if food is None:
            print('获取到了一个空')
            break
        print('\033[31m%s消费了%s\033[0m' % (name, food))
        time.sleep(random.randint(1, 3))


# 生产者
def producer(name, food, q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        f = "%s生产了%s" % (name, food)
        print(f)
        q.put(f)


if __name__ == '__main__':
    q = Queue(20)
    p1 = Process(target=producer, args=('Egon', '包子', q))
    c1 = Process(target=consumer, args=(q, 'lupengliang'))
    p2 = Process(target=producer, args=('wusir', '泔水', q))
    c2 = Process(target=consumer, args=(q, 'ruhua'))
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    p1.join()  # 将生产者进程变为同步,即生产者不生产了,才会往下执行代码
    p2.join()
    q.put(None)
    q.put(None)  # 两个消费进程要拿到None,才会不阻塞
