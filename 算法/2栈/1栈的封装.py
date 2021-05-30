"""
栈:先进后出
"""

class Stack:
    def __init__(self):
        self.items = []

    # 放元素,先进后出,类似于append
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return len(self.items) - 1

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()  # 实例化一个空栈
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print('栈顶元素下标:', stack.peek())
    print(stack.isEmpty())
    print('元素个数:', stack.size())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
