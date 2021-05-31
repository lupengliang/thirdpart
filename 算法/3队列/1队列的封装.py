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
    """
    案例：烫手的山竽
        烫手山竽游戏介绍：6个孩子围成一个圈，排列顺序孩子们自己指定。第一个孩子
        手里有一个烫手的山芋，需要在计时器1秒后将山芊传递给下一个孩子，依次类推。
        规则是，在计时器每计时7时，手里有山芊的孩子退出游戏。该游戏直到剩下一个
        孩子时结束，最后剩下的孩子获胜。请使用队列实现该游戏策略。排在第几个位置
        最终会获胜。
        准则：手里有山芊的孩子永远排在队列的头部
    """
    kids = ['A', 'B', 'C', 'D', 'E', 'F']
    queue = Queue()
    for kid in kids:
        queue.enqueue(kid)  # A对头F队尾
    while queue.size() > 1:
        for i in range(6):  # 每循环一次，山芋传递一次，手里有山芊的孩子永远在对头位置
            kid = queue.dequeue()  # 出队列
            queue.enqueue(kid)  # 进队列
        queue.dequeue()

    print('获取的选手是：', queue.dequeue())

