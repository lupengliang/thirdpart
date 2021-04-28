"""
线程池 map的使用
"""
import time
from concurrent.futures import ThreadPoolExecutor


def func(n):
    time.sleep(2)
    print(n)
    return n


tpool = ThreadPoolExecutor(max_workers=5)  # max_workers:最大线程数 默认 不要超过cpu个数*5
tpool.map(func, range(20))