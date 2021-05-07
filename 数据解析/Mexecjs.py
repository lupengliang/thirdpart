"""
模拟执行js的函数运行
"""
import execjs

node = execjs.get()  # 实例化对象

# js file
file = 'test.js'
ctx = node.compile(open(file, encoding='utf-8').read())  # 编译js代码
result = ctx.eval('js的函数名')  # 执行js代码
print(result)  # 打印结果

