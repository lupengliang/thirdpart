import asyncio
import time

start = time.time()


# 在特殊函数内部的实现中不可以出现不支持异步的模块代码
async def get_request(url):
    await asyncio.sleep(2)  # 使用支持异步的模块
    print('下载成功:', url)

urls = [
    'www.1.com',
    'www.2.com',
]
tasks = []
for url in urls:
    c = get_request(url)  # 协程对象
    task = asyncio.ensure_future(c)  # 任务对象
    tasks.append(task)

loop = asyncio.get_event_loop()  # 创建事件循环对象
# 注意:挂起操作需要手动执行
loop.run_until_complete(asyncio.wait(tasks))
print(time.time()-start)
