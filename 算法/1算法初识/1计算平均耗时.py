"""
列表中插入元素,下面这种test01算法最快
"""

from timeit import Timer


def test01():
    alist = list(range(1000))
    return alist


if __name__ == '__main__':
    timer = Timer('test01()', 'from __main__ import test01')
    t1 = timer.timeit(1000)  # 执行1000次的平均耗时,效率最高
    print(t1)  # 0.013914627349877437
