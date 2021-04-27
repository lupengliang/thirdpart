"""
p = Pool()
p.map(funcname, iterable)  # 默认异步的执行任务,且自带close和join
p.apply  同步调用的,比较少用
p.aaply_async 异步调用的 和主进程完全异步,需要手动close和join
"""
import time
from multiprocessing import Pool


def func(i):
    time.sleep(0.5)
    return i*i


if __name__ == '__main__':
    # apply_async
    p = Pool(5)
    res_1 = []
    for i in range(10):
        res = p.apply_async(func, args=(i,))  # apply的结果就是func的返回值
        res_1.append(res)
    for i in res_1:
        print(i.get())  # 解决  get阻塞等待结果 等眷func的计算结果的一种方式

    # map 的使用
    p = Pool(5)
    ret = p.map(func, range(10))
    print(ret)

"""
超级备注:
    map 与 apply_async的区别:
        map 一次性打印,自带close()和join()
        apply_async(),先打印5个,再打印其它的5个
    使用原则: 先用map解决,不行使用async
"""
