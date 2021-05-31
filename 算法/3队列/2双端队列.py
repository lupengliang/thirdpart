"""
双端队列
特点：队头和队尾都可以插入和取出数据

"""
class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        """向队头添加元素"""
        self.items.insert(0, item)

    def addRear(self, item):
        """向队尾添加元素"""
        self.items.append(item)

    def removeFront(self):
        """从队头取元素"""
        return self.items.pop()

    def removeRear(self):
        """从队尾取元素"""
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Deque()
    q.addFront(1)
    q.addFront(2)
    q.addFront(3)

    print(q.removeRear())
    print(q.removeRear())
    print(q.removeRear())
    """
    双端队列应用案例：回文检查
        回文是一个字符串，读取首尾相同的字符，例如：radar toot madam
    """
    def isHuiWen(s):
        ex = True
        q = Deque()
        for ch in s:
            q.addFront(ch)
        while q.size() > 1:
            if q.removeFront() != q.removeRear():
                ex = False
                break
        return ex
    print('===============================================')
    print(isHuiWen('heeh'))
    ss = [1, 0, 1]