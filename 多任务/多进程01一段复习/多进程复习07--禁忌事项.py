"""
多进程中子进程不能有input,因为pycharm优化过头了,无法看到子进程的命令窗口,
多进程中的报废组件:
    管道 -- 不安全,需要加锁规避,所以不再总结
"""
from multiprocessing import Process


def func():
    try:
        num = input('>>>')
        print(num)
    except EOFError:
        print('子进程不能有 input ')


if __name__ == '__main__':
    Process(target=func).start()
