# 三行启动 Flask 提供服务
# from flask import Flask
#
# app = Flask(__name__)
# app.run()

# HelloWorld
# 六行启动Flask 提供HelloWorld

from flask import Flask, send_file  # 导入Flask 类创建Flask应用对象
from flask import render_template
from flask import redirect
app = Flask(__name__)  # app = application

@app.route("/index")  # 为Flask应用对象增加路由
def index():  # 与路由绑定的视图函数，视图函数名尽可能保持唯一
    return "HelloWorld"  # str 相当于Django中的HttpResponse

@app.route("/home")
def home():
    return render_template("index.html")  # 模板存放路径？

@app.route("/re")
def re():
    return redirect("/home")  # redirect

@app.route("/get_file")
def get_file():
    return send_file("s1.py")  # 保存文件到当前目录


if __name__ == '__main__':
    app.run()  # 启动Flask应用
