# -- 协程
#       在函数(特殊的函数)定义的时候,如果使用了async修饰的话,则改函数调用后会返回一个协程对象,并且函数内部的实现语句不会被立即执行
# -- 任务对象
#       任务对象就是对协程对象的进一步封装.任务对象=高级的协程对象=特殊的函数
#       任务对象时必须要注册到事件循环对象中
#       给任务对象绑定回调:爬虫的数据解析
# -- 事件循环
#       当作一个容器,容器中必须存放任务对象
#       当启动事件循环对象后,则事件对象会对其内部存储任务对象进行异步的执行.
# >> aiohttp模块:支持异步网络请求的模块
import asyncio
import time

import aiohttp

s = time.time()
urls = [
    'http://www.baidu.com',
    'http://www.taobao.com',
]


# aiohttp处理多任务的固定写法
async def get_request(url):
    async with aiohttp.ClientSession() as s:
        async with await s.get(url=url) as response:
            page_text = await response.text()
    return page_text


tasks = []
for url in urls:
    c = get_request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()  # 创建事件循环对象
# 注意:挂起操作需要手动执行
loop.run_until_complete(asyncio.wait(tasks))
print(time.time()-s)
