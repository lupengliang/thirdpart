# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lupengliang
from time import sleep
from tqdm import tqdm


# 里面存一个可迭代的对象
for i in tqdm(range(1, 50)):
    # 模拟你的任务
    sleep(0.01)


# 这里会分4个阶段0~25%显示a, 1/4等
bar = tqdm(["a", "b", "c", "d"])
for char in bar:
    bar.set_description("Processing %s" % char)  # 添加描述
    sleep(1)
