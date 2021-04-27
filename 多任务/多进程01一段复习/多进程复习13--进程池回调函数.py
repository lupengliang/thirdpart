"""
进程池 回调函数的使用
"""
from multiprocessing.pool import Pool
import requests


def get(url):
    response = requests.get(url)
    if response.status_code == 200:
        return url, response.content.decode('utf-8')


def call_back(args):
    url, content = args
    print(url, len(content))


if __name__ == '__main__':
    url_list = [
        'http://www.baidu.com',
        'http://www.suhu.com',
        'https://www.cnblogs.com/',
        'https://www.sogou.com/'
    ]
    p = Pool(5)
    for url in url_list:
        p.apply_async(get, args=(url,), callback=call_back)  # 注意call_back函数只能有一个参数
    p.close()  # 关闭进程池
    p.join()  # 使所有进程同步结束,我理解的
