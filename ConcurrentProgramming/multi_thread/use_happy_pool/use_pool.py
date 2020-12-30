import concurrent.futures

from multi_thread.use_happy_pool import blog_spider


# craw使用方式一
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)  # 需要提前将任务列表准备好
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

# parse使用方式二
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    for future, url in futures.items():  # 取结果的方式一: 结果按照顺序进行打印
        print(url, future.result())

    # for future in concurrent.futures.as_completed(futures):  # 取结果的方式二: 结果不按照顺序进行打印
    #     url = futures[future]
    #     print(url, future.result())