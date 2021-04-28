"""
栈: 先进后出
队列: 先进先出

线程加锁要自己写代码,使用队列可以比较方便,内置很多锁,保障数据安全
三种都是安全的,在线程中传递数据,发生了数据安全问题,就换成队列
"""
import queue

q = queue.Queue()  # 队列 先进先出
# q.put(1)
# q.get()
# q.put_nowait()
# q.get_nowait()


print('==============================================')
q = queue.LifoQueue()  # 栈 先进后出
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())

print('==============================================')
q = queue.PriorityQueue()  # 优先级队列
q.put((20, 'a'))  # 传入的是一个元组
q.put((10, 'b'))  # 第1个优先级 第2个值 先比较优先级,优先级相同的,再比较值
q.put((30, 'c'))
q.put((1, 'd'))
q.put((1, 'z'))
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())  # 从小到大 优先级 从高到低

