"""
分析
1.改变页面中的查询条件,然后点击查询按钮,通过抓包工具捕获相关的数据包,
最终定位到了想要的空气质量数据对应的数据包
2.该数据包中发现:post请求携带了一个动态变化且加密的请求参数d,并且请求
到的相关加密的响应数据也是一级加密的响应数据.
3.发现点击了查询按钮后发起了一个ajax请求,该请求帮我们请求到的相关加密的
响应数据
4.通过火狐定位到搜索按钮绑定的click的点击事件(getData)
5.剖析getData函数的实现:
    -type=="HOUR"
    -getAQIData():getWeatherData(); 发现了这两个函数的调用
6.getAQIData和getWeatherData()函数的剖析
    -这两个函数的实现几乎一致,只有method变量赋值是不一样:CETDETAIL或者GETCITYWEATHER
    -param的字典:有4个键值对(city, starttime, endtime, type)
    -调用了getServerData(method, param, 匿名函数, 0.5) 函数
7.剖析getServerData函数的实现
    -在谷歌的抓包工具中做全局搜索,定位到了getServerData函数的实现.但是
    该函数的实现被加密.该加密方式叫做JS混淆.
8.JS反混淆:将js混淆的密文以原文的形式展示.推荐的解密网址:http://www.bm8.com.cn/jsConfusion/
9.getServerData反混淆后的代码进行剖析:
    -getParam(method, object),该方法的参数二object==param,并且该函数
    的返回值是步骤2中动态变化且加密的请求参数d的value值.
    -decodeData(data):是将加密的响应数据进行解密的
10.需要通过python调用js的相关代码
    -PyExecJS:可以让python对js代码进行模拟运行.
    -pip install PyExecJS
    -安装nodejs环境的安装,不然PyExecJS无法使用
"""


"""
总结:
    -动态变化的请求参数
    -js加密
    -js混淆
"""

