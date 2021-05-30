"""
队列:先进先出
"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()  # 从尾部取

    def peek(self):
        return len(self.items) - 1

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()  # 实例化一个空队列
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print('栈顶元素下标:', q.peek())
    print(q.isEmpty())
    print('元素个数:', q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
