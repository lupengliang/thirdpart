"""
进程池
    效率高
进程池与信号量的区别:
    进程池: 进程池里的进程数据一定,多个任务在外面排队等待
    信号量: 任务一定,进程数据无限,但是进程执行任务后立即消失
    优劣: 进程池相对而言,减少了操作系统的调度时间
备注:
    一般情况下我们不会起用过多的进程去处理问题,而是采用进程池来解决问题
"""
import time
from multiprocessing import Pool, Process


def func(n):
    for i in range(10):
        print(n+1)


def func2(n):
    for i in range(10):
        print(n+2)


if __name__ == '__main__':
    # 优  # 0.5 seconds
    start = time.time()
    p_lst = []
    pool = Pool(5)  # 5个进程
    pool.map(func, range(100))  # 100任务 自带join功能
    pool.map(func2, [])
    end = time.time()
    print('进程池:100个任务耗时: ', end-start)

    # 劣  # 13.5 seconds
    start = time.time()
    for i in range(100):
        p = Process(target=func, args=(i,))
        p_lst.append(p)
        p.start()
    for p in p_lst: p.join()
    end = time.time()
    print('执行100进程耗时: ', end-start)