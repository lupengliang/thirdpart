import asyncio


def callback(task):  # 作为任务对象的回调函数
    print('i am callback and ', task.result)


async def test():
    print('i am test()')
    return 'bobo'  # 回调函数用task.result()来接收这个返回值


c = test()  # 协程对象
task = asyncio.ensure_future(c)  # 封装了一个任务对象
task.add_done_callback(callback)
loop = asyncio.get_event_loop()  # 创建一个事件循环的对象
loop.run_until_complete(task)
print(c)
