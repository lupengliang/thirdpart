"""
实例: 火车票售票系统演示
进程锁:
    涉及到改文件/改数据的 需要加锁,这样会降低效率,但是数据安全

注意事项:
    json类型的字典数据一定要使用"",而不能使用''.
"""
import json
import time
from multiprocessing import Process
from multiprocessing import Lock


# 展示剩余票数
def show(i):
    with open('ticket.txt') as f:
        dic = json.load(f)
    print("余票: %s" % dic['ticket'])


# 买票
def buy_ticket(i, lock):
    lock.acquire()  # 拿钥匙进门
    with open('ticket.txt') as f:
        dic = json.load(f)  # 读取数据,自动还原数据类型
        time.sleep(0.1)
    if dic['ticket'] > 0:
        dic['ticket'] -= 1
        print("\033[32m%s买到票了\033[0m" % i)
    else:
        print("\033[31m%s没买到票了\033[0m" % i)
    with open('ticket.txt', 'w') as f:
        json.dump(dic, f)  # 写入数据,自动判断数据类型
    lock.release()


if __name__ == '__main__':
    person_names = ['lupengliang', 'shangdi', 'qiaobusi', 'biergaici', 'xiongmaoren', 'diyupaoxiao', 'qianxingzhe',
                    'fashi', 'saman', 'kugong']
    for person in person_names:  # 用这个可以控制次数
        p = Process(target=show, args=(person,))
        p.start()
    lock = Lock()
    for person in person_names:
        p1 = Process(target=buy_ticket, args=(person, lock))
        p1.start()
