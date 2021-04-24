# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lupengliang
import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 50+1)
]


# 请求抓取数据
def craw(url):
    r = requests.get(url)
    return r.text


# 解析数据
def parse(html):
    # class = "post-item-title"
    soup = BeautifulSoup(html, "html.parser")
    links = soup.findAll('a', class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]


if __name__ == '__main__':
    for result in parse(craw(urls[2])):
        print(result)
