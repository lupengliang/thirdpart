"""
守护进程
    优化 生产者消费者模型<队列>
    最后有详解
"""
import time
import random
from multiprocessing import Process, Queue, JoinableQueue


# 消费者
def consumer(q, name):
    while True:
        food = q.get()
        if food is None:
            print('获取到了一个空')
            break
        print('\033[322m%s消费了%s' % (name, food))
        time.sleep(random.randint(1, 3))
        q.task_done()  # count - 1


# 生产者
def producer(name, food, q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        f = "%s生产了%s%s" % (name, food, i)
        print(f)
        q.put(f)
    q.join()  # 阻塞 直到一个队列中的所有数据 全部被处理完毕


if __name__ == '__main__':
    q = JoinableQueue(20)
    p1 = Process(target=producer, args=('Egon', '饺子', q))
    p2 = Process(target=producer, args=('wusir', '包子', q))
    c1 = Process(target=consumer, args=(q, 'lupengliang'))
    c2 = Process(target=consumer, args=(q, 'ruhua'))
    p1.start()
    p2.start()
    c1.daemon = True  # 设置为守护进程,主进程中的代码执行完毕之后,子进程自动结束
    c2.daemon = True
    c1.start()
    c2.start()
    p1.join()
    p2.join()  # 感知一个进程的结束

"""
生产者
    在生产者的这一端
        # 第一次生产一个数据
        # 且每一次生产的数据都放到队列中
        # 在队列中刻上一个记号
        # 当生产者全部生产完毕之后
        # 队列join信号: 已经停止生产数据了
                       且要等等之前被刻上记号的被消费完,
                       当数据被处理完时,join阻塞结束
消费者
    consumer 中把所有的任务消耗完
    producer 端的join感知到,停止阻塞
    所有的producer进程结束
    主进程中p.join结束
"""