# 单线程
from time import time, sleep

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


for url in urls:
    get_request(url)
print('总耗时: ', time()-start)
