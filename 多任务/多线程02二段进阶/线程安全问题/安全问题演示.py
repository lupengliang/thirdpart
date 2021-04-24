# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lupengliang
import threading
import time
"""
取钱问题，出现线程安全问题，偶现的问题
"""


class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    if account.balance >= amount:
        time.sleep(0.1)  # sleep进入阻塞，切换线程，因为这种情况是偶现的，所以用sleep使错误出现
        print(threading.current_thread().name, "取钱成功")
        account.balance -= amount
        print(threading.current_thread().name, "余额", account.balance)
    else:
        print(threading.current_thread().name, "取钱失败，余额不足")


if __name__ == '__main__':
    account = Account(1000)
    ta = threading.Thread(name='ta', target=draw, args=(account, 800))
    tb = threading.Thread(name='tb', target=draw, args=(account, 800))
    ta.start()
    tb.start()
