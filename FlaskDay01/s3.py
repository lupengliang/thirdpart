# jinjia2往html中传递参数

from flask import Flask, render_template

STUDENT = {'name': 'Old', 'age': 38, 'gender': '中'}

STUDENT_LIST = [
    {'name': 'Old', 'age': 38, 'gender': '中'},
    {'name': 'Boy', 'age': 73, 'gender': '男'},
    {'name': 'EDU', 'age': 84, 'gender': '女'},
]

STUDENT_DICT = {
    1: {'name': 'Old', 'age': 38, 'gender': '中'},
    2: {'name': 'Boy', 'age': 73, 'gender': '男'},
    3: {'name': 'EDU', 'age': 84, 'gender': '女'},
}

app = Flask(__name__)

@app.template_global()
def ab(a, b):
    return a+b

# 1.查看STUDENT 放在studentinfo页面
@app.route("/stu")
def stu():
    return render_template("stuinfo.html", funcab=ab, stu_info=STUDENT, stu_list=STUDENT_LIST, stu_dict=STUDENT_DICT)


if __name__ == '__main__':
    app.run("0.0.0.0")