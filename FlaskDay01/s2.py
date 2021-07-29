import os

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "(&&($$@$@^(@$@$^(@$*#($@#*&$*^@$^$(@)"
app.debug = True


@app.route("/login", methods=["GET", "POST"])  # 405 请求方式不被允许
def login():
    # 从request中取出请求方式
    print(request.method)
    if request.method == "GET":
        # 在 Django request.GET 取出URL中的参数
        # 在Flask 获取URL 中的参数
        # print(request.url)  # 请求方式
        # print(request.url_charset)  # URL 编码方式
        # print(request.url_root)  # 请求地址 完整请求地址host
        # print(request.url_rule)  # 路由地址
        print(request.values)  # 接收所有（GET, POST）请求中的数据,包含了URL和FormData的数据
        return render_template("login.html")
    if request.method == "POST":
        # 在 Django request.POST 取出FormData（Form表单）
        # 在Flask 获取FormData request.form
        # print(request.form.get("username"))
        # print(request.form.to_dict())

        # print(request.files.get("my_file"))  # 感觉上是提取文件
        # print(request.args.get("id"))  # 获取URL中的数据 字符串
        # # 获取一个FileStorage Flask文件特殊对象
        # my_file = request.files.get("my_file")
        # new_file = os.path.join("xht", my_file.filename)
        # my_file.save(new_file)


        # 获取其他数据
        # request.cookies
        # request.headers
        # request.path == request.url_rule
        # request.host == "127.0.0.1:9527"
        # request.host_url == "http://127.0.0.1:9527"

        # 特殊的提交方式数据获取
        # Content-Type:application/json
        # request.json 获取Content-Type:application/json时提交的数据
        # Content-Type 无法被识别或不包含Form字眼
        # request.data 获取原始请求体中的数据b""
        if request.form.get("username")  == "123":
            session["user"] = request.form.get("username")
            return redirect("/")


        return "200 OK"


@app.route("/")
def index():
    print(session.get("user"))
    return render_template("index.html")


if __name__ == '__main__':
    app.run("0.0.0.0", 9527)
