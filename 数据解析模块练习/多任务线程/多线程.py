# 多线程
from time import time, sleep

from multiprocessing.dummy import Pool

urls = [
    'www.1.com',
    'www.2.com',
    'www.3.com',
]
start = time()


def get_request(url):
    print('正在下载:', url)
    sleep(2)
    print('下载结束:', url)


pool = Pool(3)
pool.map(get_request, urls)  # 传函数  传列表
print('总耗时: ', time()-start)
