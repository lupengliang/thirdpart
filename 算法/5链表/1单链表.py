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


if __name__ == '__main__':
    link = Link()
    link.add(3)
    link.add(4)
    link.add(5)
    link.travel()
