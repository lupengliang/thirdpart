

# 单链表
class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


class Link():
    def __init__(self):
        self._head = None

    def append(self, item):
        node = Node(item)
        if self._head == None:
            self._head = node
            return
        cur = self._head
        while cur:
            pre = cur
            cur = cur.next
        pre.next = node

    def travel(self):
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next

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
            if item == cur.item:
                pre.next = cur.next
                return

    def reverse(self):
        cur = self._head
        pre = None
        next_node = cur.next

        while cur:
            cur.next = pre
            pre = cur
            cur = next_node
            if cur:
                next_node = cur.next


if __name__ == '__main__':
    link = Link()
    link.append(1)
    link.append(2)
    link.append(3)
    link.append(4)
    link.append(5)
    link.remove(5)
    link.travel()
