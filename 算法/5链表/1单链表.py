"""
单链表
1. 插入
2. 遍历
"""

# 节点
class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


# 链表
class Link():
    def __init__(self):
        # 构造出一个空链表
        # _head存储的只能是空或者第一个节点的地址
        self._head = None

    # 向链表的头部插入一个节点
    def add(self, item):
        # 创建一个新的节点
        node = Node(item)
        node.next = self._head
        self._head = node

    # 遍历链表
    def travel(self):
        # _head在链表创建好之后一定是不变的
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next

    # 判断链表是否为空
    def isEmpty(self):
        return self._head == None

    # 获取链表的长度
    def size(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    # 最后一个位置插入节点
    def append(self, item):
        node = Node(item)
        # 特殊情况
        if self._head == None:
            self._head = node
            return
        cur = self._head
        pre = None
        while cur:
            pre = cur
            cur = cur.next
        pre.next = node

    def search(self, item):
        find = False

        cur = self._head
        while cur:
            if cur.item == item:
                find = True
                break
            cur = cur.next
        return find

    # 插入一个节点
    def insert(self, pos, item):
        node = Node(item)
        cur = self._head
        for i in range(pos):
            pre = cur
            cur = cur.next
        pre.next = node
        node.next = cur

    # 删除元素
    def remove(self, item):
        cur = self._head
        pre = None

        # 删除的是第一个节点
        if cur.item == item:
            self._head = cur.next
            return
        while cur:
            pre = cur
            cur = cur.next
            if cur.item == item:
                pre.next = cur.next
                return


if __name__ == '__main__':
    link = Link()
    link.add(3)
    link.add(4)
    link.add(5)
    link.travel()
    print('+++++++++++++++')
    print(link.isEmpty())
    print("===============")
    print(link.size())
    print("===============")
    print(link.append(1))
    print(link.append(2))
    print(link.search(3))
    print(link.search(4))
    print("================")
    print(link.insert(2, 1.3))


