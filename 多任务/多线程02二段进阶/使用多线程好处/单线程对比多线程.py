# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lupengliang
import threading
import time

from 多线程02二段进阶.基础爬虫 import blog_spider
"""
单线程与多线程消耗时间的比对
"""


# 单线程
def single_thread():
    print("single_thread begin")
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print("single_thread end")


# 多线程
def multi_thread():
    print("multi_thread begin")
    threads = []
    for url in blog_spider.urls:
        threads.append(threading.Thread(target=blog_spider.craw, args=(url,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("multi_thread end")


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("single thread cost:", end-start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi thread cost:", end-start, "seconds")
