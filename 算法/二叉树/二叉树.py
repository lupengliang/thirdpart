# 节点的数据结构
class Node():
    def __init__(self, item):
        self.item = item  # 存放数据
        self.left = None  # 存入左标识的值
        self.right = None  # 存入右标识的值


# 树
class Tree():
    def __init__(self):
        self.root = None  # 根节点

    def addNode(self, item):
        node = Node(item)
        # 如果插入第一个节点的情况
        if self.root == None:
            self.root = node
            return
        15.15