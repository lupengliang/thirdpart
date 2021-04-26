# IPC(Inter-Process Communication)
# 队列 先进先出
"""
from multiprocessing import Queue
q = Queue(5)  # 队列的长度为5
q.put(1)  # 往队列里塞值
q.put(2)
q.put(3)
q.put(4)
q.put(5)  # 如果里面装潢了,就阻塞,程序停在那里,一直运行空
print(q.full())  # 查看队列中是否为满
print(q.get())  # 从队列中取值
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())  # 如果从里面中取完了,再进行取值,就阻塞
print(q.empty())  # 判断是否为空
q.get_nowait()
print(q.get())
q.put(6)
for i in range(6):
    q.put(i)
"""
from multiprocessing import Queue, Process


def produce(q):
    q.put('hello')


def consume(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue()
    p = Process(target=produce, args=(q,))
    p.start()
    c = Process(target=consume, args=(q,))
    c.start()
