"""
队列:先进先出
"""


class Queue:
    def __init__(self):
        self.items = []

    # 存入数据
    def enqueue(self, item):
        self.items.insert(0, item)

    # 取出数据
    def dequeue(self):
        return self.items.pop()  # 从尾部取

    # 队列的长度
    def peek(self):
        return len(self.items) - 1

    # 判断队列是否为空
    def isEmpty(self):
        return self.items == []

    # 队列的长度
    def size(self):
        return len(self.items)


if __name__ == '__main__':
    # 如何使用两个队列实现一个栈
    alist = [1, 2, 3, 4, 5]
    q1 = Queue()
    for i in alist:
        q1.enqueue(i)
    q2 = Queue()
    while q1.size() > 0:
        # 将q1中的n-1个值取出放入到q2中
        while q1.size() > 1:
            item = q1.dequeue()
            q2.enqueue(item)
        print(q1.dequeue())

        q1, q2 = q2, q1
