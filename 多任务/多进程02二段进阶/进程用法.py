# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lupengliang
"""
素数：
曾称质数。一个大于1的正整数，如果除了1和它本身以外，不能被其他正整数整除，就叫素数。如2，3，5，7，11，13，17…。
"""
import math
import time
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
"""
单线程、多线程、多进程效果对比
多进程与多线程用法一致
"""

PRIMES = [11227231235095293] * 100


# 计算一个数是否为素数
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n+1, 2):
        if n % i == 0:
            return False
    return True


# 单线程
def single_thread():
    for number in PRIMES:
        is_prime(number)


# 多线程
def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


# 多进程
def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


if __name__ == '__main__':
    print(PRIMES)
    start = time.time()
    single_thread()
    end = time.time()
    print('single_thread, cost:', end-start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print('multi_thread, cost:', end-start, "seconds")

    start = time.time()
    multi_process()
    end = time.time()
    print("multi_process, cost:", end-start, "seconds")
