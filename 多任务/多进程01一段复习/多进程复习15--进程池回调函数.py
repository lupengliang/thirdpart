"""
回调函数
将func1的返回值作为回调函数的参数,回调参数本身没有参数
"""
import os
from multiprocessing import Pool


def func1(n):
    print('in func1', os.getpid())
    return n*n

def func2(nn):
    print('in func2', os.getpid())
    print(nn)
    

if __name__ == '__main__':
    print('主进程:', os.getpid())
    p = Pool(5)
    for i in range(10):
        p.apply_async(func1, args=(10,), callback=func2)
    p.close()
    p.join()
